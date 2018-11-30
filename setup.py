#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright © 2016-2018 Cyril Desjouy <ipselium@free.fr>
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
# Creation Date :
# Last Modified : mer. 11 avril 2018 00:15:49 CEST
"""
-----------
DOCSTRING

@author: Cyril Desjouy
"""

from setuptools import setup, find_packages
import sys
import nfomiss

if sys.version_info < (2,7):
    raise NotImplementedError(
        "Sorry, you need at least Python 2.7 to use nfomiss.")

setup(
    name='nfomiss',
    description='Look for missing nfo/artworks in media library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    version=nfomiss.__version__,
    license='GPL',
    url='https://github.com/ipselium/nfomiss',
    author='Cyril Desjouy',
    author_email='cyril.desjouy@univ-lemans.fr',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Programming Language :: Python :: 3.5',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    ],
    entry_points={
        'console_scripts': [
            'nfomiss = nfomiss.nfomiss:main',
        ],
    }
)
