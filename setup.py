#!/usr/bin/env python
from setuptools import setup, find_packages
import os, re

PKG='multiauth'
version = "0.1.0"

setup(name=PKG,
      version=verstr,
      description="multiple authentication support for django",
      author="Arif Widi Nugroho",
      author_email="arif@sainsmograf.com",
      url="https://github.com/arifwn/django-multiauth",
      packages = find_packages(),
      install_requires = ['setuptools', 'oauth2'],
      license = "MIT License",
      keywords="multiauth",
      zip_safe = True)
