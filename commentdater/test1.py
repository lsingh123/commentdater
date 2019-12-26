#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 15:50:35 2019

@author: lavanyasingh
"""
import src
if __name__ == '__main__':
    dater = src.CommentDater("test/test_infile.cc")
    dater.parse()