#!/usr/bin/env python

from setuptools import setup

version = open("files/version.txt").read().strip()
long_description = open("README.md").read().strip()

setup(
    name='MaxPhisher',
    version=version,
    description='A python phishing script for login phishing, image phishing video phishing an many more!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Psycho-Sanjay',
    author_email='hackerdk357@gmail.com',
    license="MIT",
    url='https://github.com/Psycho-Sanjay/MaxPhisher/',
    scripts=['maxphisher'],
    install_requires=["requests", "rich"]
)
