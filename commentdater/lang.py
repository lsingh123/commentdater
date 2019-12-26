#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 12:10:06 2019

@author: lavanyasingh
"""
from enum import Enum

COMMENTS = {"py_multiline_open": "'", "py_multiline_close":"'", "py_single": "#", 
                "c_multiline_open": "/*", "c_multiline_close":"*/", "c_single": "//"}

# type to represent the language of a file
class Lang(Enum):
    c = 1
    java = 2
    python = 3
    
    def get_multiline_start(self):
        if self is Lang.c:
            return COMMENTS['c_multiline_open']
        if self is Lang.java:
            return COMMENTS['java_multiline_open']
        if self is Lang.python:
            return COMMENTS['py_multiline_open']
    
    def get_multiline_end(self):
        if self is Lang.c:
            return COMMENTS['c_multiline_close']
        if self is Lang.java:
            return COMMENTS['java_multiline_close']
        if self is Lang.python:
            return COMMENTS['py_multiline_close']
    
    def get_single(self):
        if self is Lang.c:
            return COMMENTS['c_single']
        if self is Lang.java:
            return COMMENTS['java_single']
        if self is Lang.python:
            return COMMENTS['py_single']