# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import referly
version = referly.__version__

setup(
    name='referly',
    version=version,
    author='',
    author_email='noblenara@gmail.com',
    packages=[
        'referly',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['referly/manage.py'],
)