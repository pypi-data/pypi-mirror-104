#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from os import path
import sys
here = path.abspath(path.dirname(__file__))

sys.path.append(here)
import pkglic.authinfo as pkglic


# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=pkglic.PROGRAM_NAME,
    version=pkglic.VERSION,
    author=pkglic.AUTHOR,
    author_email='jspr.hgstrm@gmail.com',
    license='MIT',
    keywords="license, package, javascript, python, csharp",
    url="https://github.com/jhogstrom/pkglic",
    # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    platforms=[
        "Operating System :: OS Independent",
        ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: C#",
        "Programming Language :: Python",
        "Programming Language :: JavaScript",
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Build Tools"
        ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pkglic = pkglic.pkglic:main'
        ]
    },
    description='Script to get the licenses of components used by js, py or c# apps.',
    long_description_content_type="text/markdown",
    long_description=long_description,
    install_requires=[
        'requests',
        'lxml'
        ],
    zip_safe=True,
    )
