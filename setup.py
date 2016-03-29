#!/usr/bin/env python

from setuptools import setup

setup(
    name='Ranch',
    version='0.1.0',
    description='Addressing done right',
    author='Martijn Arts',
    author_email='martijn@3dhubs.com',
    packages=['ranch'],
    scripts=['scripts/ranch-download'],
    install_requires=['beautifulsoup4', 'flake8', 'requests']
)
