#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='django-site-maintenance',
    version='1.0.1',
    url="https://github.com/harryjmoss/django-site-maintenance-py3",
    author="Original: Stefano Apostolico, Current maintainer: Harry Moss",
    license="MIT License",
    packages=find_packages(),
    install_requires=['Django>=2.2.16'],
)
