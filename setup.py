#!/usr/bin/env python
import os
from setuptools import setup
from ranch.specs import _get_latest_export

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except ImportError:
    long_description = 'Ranch does addressing in Python'

setup(
    name='Ranch',
    version='1.0.7',
    description='Ranch does addressing in Python',
    long_description=long_description,
    author='Martijn Arts',
    author_email='martijn@3dhubs.com',
    url="https://github.com/3DHubs/ranch",
    packages=['ranch'],
    package_dir={'ranch': 'ranch'},
    package_data={'ranch': [_get_latest_export()]},
    scripts=['scripts/ranch-download'],
    install_requires=['beautifulsoup4', 'flake8', 'requests', 'progressbar2',
                      'percache'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
    ]
)
