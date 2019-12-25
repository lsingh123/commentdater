#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 12:10:06 2019

@author: lavanyasingh
"""
from enum import Enum

# type to represent the language of a file
class Lang(Enum):
    c = 1
    java = 2
    python = 3
    COMMENTS = {"py_multiline_open": "'", "py_multiline_close":"'", "py_single": "#", 
                "c_multiline_open": "/*", "c_multiline_close":"*/", "c_single": "//"}
    
    def __init__(self, lang):
        self.LANGUAGE = lang
    
    def get_multiline_open(self):
        if self.LANGUAGE == Lang.c:
            return self.COMMENT['c_multiline_open']
        if self.LANGUAGE == Lang.java:
            return self.COMMENT['java_multiline_open']
        if self.LANGUAGE == Lang.python:
            return self.COMMENT['py_multiline_open']
    
    def get_multiline_close(self):
        if self.LANGUAGE == Lang.c:
            return self.COMMENT['c_multiline_close']
        if self.LANGUAGE == Lang.java:
            return self.COMMENT['java_multiline_close']
        if self.LANGUAGE == Lang.python:
            return self.COMMENT['py_multiline_close']
    
    def get_single(self):
        if self.LANGUAGE == Lang.c:
            return self.COMMENT['c_single']
        if self.LANGUAGE == Lang.java:
            return self.COMMENT['java_single']
        if self.LANGUAGE == Lang.python:
            return self.COMMENT['py_single']