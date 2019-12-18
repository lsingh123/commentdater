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

    # run git diff in a child process to get diffs
    # put the diffs in diffs.txt
    def get_diffs(self):
        pid = os.fork()
        
        # set up the child process
        if (pid == 0):
            args = ["git", "diff", "HEAD~1", "-U0", self.file]
            
            # set up outfile
            outfile = open("diffs.txt", "w+")
            os.dup2(outfile.fileno(), sys.stdout.fileno())
            
            r = os.execvp(args[0], args)
            
            # raise an exception and exit if child failed
            if (r != 0):
                print("child process failed to execvp")
                os._exit(1)
        
        # wait for child to finish
        r = os.waitpid(pid, 0)
        
    
    ## parse a diff line to get line number
    def parse_line(self, line):
        line = line[line.find("+")+1:]
        end = line.find(",") 
        if end == -1:
            end = line.find(" @")
        return line[:end]
        
    # return list of changed lines in diff_file
    def find_lines(self, diff_file):
        with open(diff_file, "r") as fd:
            lines = list(iter(fd.readline, ''))
        lines = list(filter(lambda s: s.find("@@") != -1, lines))
        for i in range(len(lines)):
           lines[i] = self.parse_line(lines[i])
        lines = list(map(lambda s: int(s), lines))
        return lines
            
            
        
if __name__ == '__main__':
    path = "test.cc"    
    dater = CommentDater(path)
    dater.get_diffs()
    dater.find_lines()
        
            
    