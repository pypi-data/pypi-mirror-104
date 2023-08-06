#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from distutils.core import setup, Extension

from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'description.txt'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pkglic',
    version='1.0',
    author='Jesper Högström',
    author_email='jspr.hgstrm@gmail.com',
    license='MIT',
    keywords="license, package, javascript, python, csharp",
    # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    platforms=[
        "Operating System :: OS Independent",
        ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pkglic = pkglic.pkglic:main'
        ]
    },
    # packages=['pkglic'],
    # url='',
    description='Script to get the licenses of components used by js, py or c# apps.',
    long_description=long_description,
    install_requires=[
        'requests',
        'lxml'
        ],
    zip_safe=True,
    )
