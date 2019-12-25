#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 12:25:15 2019

@author: lavanyasingh
"""

import unittest
import sys
from src import CommentDater

class Tester(unittest.TestCase):
    
    def __init__(self):
        # redirect stdout
        sys.stdout = open("test_output.txt", "w")
        
    def pytest(self):
        dater = CommentDater("test_infile2.py")
        dater.parse()
        with open("test_output.txt", "r") as fd:
            output = fd.read()
        
        # check outdated single line comment (file modified line 11)
        self.assertNotEqual(output.find("possible outdated comment at test_infile2.py:9"), -1)
        
        # check that modified comments aren't included in output 
        # (file modified at line 13 and line 14)
        self.assertEqual(output.find("possible outdated comment at test_infile2.py:13"), -1)
        
        # check that multiline comments are handled (file modified at line 18)
        self.assertNotEqual(output.find("possible outdated comment at test_infile2.py:16"), -1)
    
    def ctest(self):
        dater = CommentDater("test_infile1.cc")
        dater.parse()
        with open("test_output.txt", "r") as fd:
            output = fd.read()
        
        # check outdated single line comment (file modified line 3)
        self.assertNotEqual(output.find("possible outdated comment at test_infile1.cc:1"), -1)
        
        # check that modified comments aren't included in output 
        # (file modified at line 6 and line 7)
        self.assertEqual(output.find("possible outdated comment at test_infile1.cc:6"), -1)
        
        # check that multiline comments are handled (file modified at line 12)
        self.assertNotEqual(output.find("possible outdated comment at test_infile1.cc:9"), -1)
        
if __name__ == '__main__':
    unittest.main()