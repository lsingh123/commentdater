#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:53:52 2019

@author: lavanyasingh
"""

import os
import sys

class CommentDater:
    
    def __init__(self, file):
        self.file= file

    def get_diffs(self):
        pid = os.fork()
        
        # set up the child process
        if (pid == 0):
            args = {"git", "git diff HEAD~1 -U0 %s".format(self.file)}
            
            # set up outfile
            outfile = open("diffs.txt")
            os.dup2(outfile, sys.stdout)
            
            r = os.execvp(args[0], args)
            
            # raise an exception and exit if child failed
            if (r != 0):
                print("child process failed to execvp")
                os._exit(1)
        
        # wait for child to finish
        r = os.waitpid(pid)
        
        diffs = open("diffs.txt")
        print(diffs.read())
        
if __name__ == '__main__':
    path = "test.cc"    
        
            
    