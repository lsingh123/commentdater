#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 15:06:55 2019

@author: lavanyasingh
"""

 
"""setup.py: setuptools control."""
 
 
import re
from setuptools import setup
 
 
version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('commentdater/src.py').read(),
    re.M
    ).group(1)
 
 
with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")
 
 
setup(
    name = "cmdline-commentdater",
    packages = ["commentdater"],
    entry_points = {
        "console_scripts": ['commentdater = commentdater.src:main']
        },
    version = version,
    description = "Python command line tool to check for out of date comments.",
    long_description = long_descr,
    author = "Lavanya Singh",
    author_email = "lsingh@college.harvard.edu"
    )