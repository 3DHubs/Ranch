#!/usr/bin/env python

from setuptools import setup

setup(
    name='Ranch',
    version='0.1.0',
    description='Ranch does addressing in Python',
    author='Martijn Arts',
    author_email='martijn@3dhubs.com',
    url="https://github.com/3DHubs/ranch",
    packages=['ranch'],
    scripts=['scripts/ranch-download'],
    install_requires=['beautifulsoup4', 'flake8', 'requests'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
    ]
)
