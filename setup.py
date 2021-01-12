#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='django-site-maintenance',
    version='1.0.0',
    url="https://github.com/harryjmoss/django-site-maintenance/",
    author="Harry Moss",
    author_email="h.moss@ucl.ac.uk",
    license="MIT License",
    packages=find_packages(),
    install_requires=['Django>=2.2.16'],
)
