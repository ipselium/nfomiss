#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright © 2016-2018 Cyril Desjouy <cyril.desjouy@univ-lemans.fr>
#
# This file is part of nfomiss
#
# nfomiss is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# nfomiss is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with nfomiss. If not, see <http://www.gnu.org/licenses/>.
#
#
# Creation Date : 2018-11-29 - 20:56:24
"""
-----------

nfomiss :

    List missing nfo or artwork in a media database

@author: Cyril Desjouy
"""

import os
import re
import sys
import argparse


def regex(name, extension='jpg'):
    """
    Build regex such as :

        name - begining of the string
        extension - end of the string
    """
    return re.compile(r"^{}.*{}$".format(re.escape(name), re.escape(extension)))


def check_path(dirname):
    """
    Check if path exists
    """
    if not os.path.isdir(dirname):
        print('Directory does not exist!')
        sys.exit(0)
    else:
        return dirname


def trunc(string, max_length=59):
    if len(string) <= max_length:
        return string
    else:
        return string[:56] + '...'


def main():
    parser = argparse.ArgumentParser(description='List missing nfo/artwork in a media database.')
    parser.add_argument('path', type=check_path)
    parser.add_argument('-j', '--jpg', help='List only missing artwork', action="store_true")
    parser.add_argument('-i', '--nfo', help='List only missing nfo', action="store_true")
    parser.add_argument('-v', '--version', help='Display version number', action="store_true")

    args = parser.parse_args()

    if args.version:
        print(23*'-')
        print('| vdnfo version {} |'.format(__version__))
        print(23*'-')
        sys.exit(0)

    if args.path:
        path = args.path
    else:
        print('Path missing!')
        sys.exit(0)


    folder = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    basenames = [os.path.splitext(name)[0] for name in folder
                 if '.jpg' not in name and '.nfo' not in name]

    nonfo = [i for i in basenames if "{}.nfo".format(i) not in folder]
    nojpg = [i for i in basenames if not list(filter(regex(i).match, folder))]


    if args.nfo:
        nonfo.sort()
        template = '| {:68} | {:^5} |'
        print(80*'-')
        print(template.format('Title ({} files)'.format(len(nonfo)), 'nfo'))
        print(80*'-')
        for i in nonfo:
            print(template.format(i, 'False'))
        print(80*'-')

    if args.jpg:
        nojpg.sort()
        template = '| {:68} | {:^5} |'
        print(80*'-')
        print(template.format('Title ({} files)'.format(len(nojpg)), 'jpg'))
        print(80*'-')
        for i in nojpg:
            print(template.format(i, 'False'))
        print(80*'-')

    if not args.jpg and not args.nfo:
        nonfo.sort()
        nojpg.sort()
        template = '| {:60} | {:^5} | {:^5} |'
        allmissings = list(set(nonfo + nojpg))
        allmissings.sort()
        print(80*'-')
        print(template.format('Title', 'nfo', 'jpg'))
        print(80*'-')
        for i in allmissings:
            nfo = str(i not in nonfo)
            jpg = str(i not in nojpg)
            print(template.format(trunc(i), nfo, jpg))
        print(80*'-')

if __name__ == "__main__":
    main()

