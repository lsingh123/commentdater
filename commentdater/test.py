#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 12:25:15 2019

@author: lavanyasingh
"""

import unittest
import os
import importlib
import src
importlib.reload(src)


class Tester(unittest.TestCase):
        
    def test_py(self):
        with open("test/test_output.txt", "w") as fd:
            dater = src.CommentDater("test/test_infile.py", output = fd)
            dater.parse()
        with open("test/test_output.txt", "r") as fd:
            output = "".join(list(fd.readlines()))
        
        # check outdated single line comment (file modified line 11)
        self.assertNotEqual(output.find("possible outdated comment at test/test_infile.py:9"), -1)
        
        # check that modified comments aren't included in output 
        # (file modified at line 13 and line 14)
        self.assertEqual(output.find("possible outdated comment at test/test_infile.py:13"), -1)
        
        # check that multiline comments are handled (file modified at line 19)
        self.assertNotEqual(output.find("possible outdated comment at test/test_infile.py:16"), -1)
    
    def test_c(self):
        with open("test/test_output.txt", "w") as fd:
            dater = src.CommentDater("test/test_infile.cc", output = fd)
            dater.parse()
        with open("test/test_output.txt", "r") as fd:
            output = "".join(list(fd.readlines()))
        
        # check outdated single line comment (file modified line 3)
        self.assertNotEqual(output.find("possible outdated comment at test/test_infile.cc:1"), -1)
        
        # check that modified comments aren't included in output 
        # (file modified at line 6 and line 7)
        self.assertEqual(output.find("possible outdated comment at test/test_infile.cc:6"), -1)
        
        # check that multiline comments are handled (file modified at line 12)
        self.assertNotEqual(output.find("possible outdated comment at test/test_infile.cc:9"), -1)
        
if __name__ == '__main__':
    unittest.main()
    os.remove("test/test_output.txt")