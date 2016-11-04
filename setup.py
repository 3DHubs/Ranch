#!/usr/bin/env python
from setuptools import setup
from ranch.address import _get_latest_export

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except ImportError:
    long_description = 'Ranch does addressing in Python'

setup(
    name='Ranch',
    version='0.2.7',
    description='Ranch does addressing in Python',
    long_description=long_description,
    author='Martijn Arts',
    author_email='martijn@3dhubs.com',
    url="https://github.com/3DHubs/ranch",
    packages=['ranch'],
    scripts=['scripts/ranch-download'],
    data_files=[('data', [_get_latest_export()])],
    install_requires=['beautifulsoup4', 'flake8', 'requests', 'progressbar2',
                      'percache'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
    ]
)
