#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:53:52 2019

@author: lavanyasingh
"""

__version__ = "0.1.0"

import os
import sys
import argparse
from lang import Lang

class CommentDater:
    
    DIFF_FILE = "diffs.txt"
    LANG = None

    # file: input file
    # output_len: lenght of the output
    def __init__(self, file, output_len = 50, output = sys.stdout):
        self.file = file
        self.diffs = []
        self.comments = []
        self.find_lines()
        self.output_len = output_len
        self.set_lang(file)
        self.output = output
    
    # determine language of the input file
    # raise ValueError if incorrect file format
    def set_lang(self, file):
        if file.find(".py") != -1:
            self.LANG = Lang.python
        elif file.find(".cc") != -1:
            self.LANG = Lang.c
        elif file.find(".java") != -1:
            self.LANG = Lang.java
        else:
            raise ValueError('''file must end in one of the following extensions:
                .cc, .py, .java''' )
            

    # run git diff in a child process to get diffs
    # put the diffs in diffs.txt
    def get_diffs(self):
        pid = os.fork()
        
        # set up the child process
        if (pid == 0):
            args = ["git", "diff", "HEAD~1", "-U0", self.file]
            
            # set up outfile
            outfile = open(self.DIFF_FILE, "w+")
            os.dup2(outfile.fileno(), sys.stdout.fileno())
            
            r = os.execvp(args[0], args)
            
            # raise an exception and exit if child failed
            if (r != 0):
                print("child process failed to execvp")
                os._exit(1)
        
        # wait for child to finish
        r = os.waitpid(pid, 0)
        
    # return list of changed lines in diff_file
    # handle the case of subsequent lines that have been edited
    def find_lines(self, diff_file=None):
        self.get_diffs()
        if not diff_file:
            diff_file = self.DIFF_FILE
        with open(diff_file, "r") as fd:
            lines = list(iter(fd.readline, ''))
        lines = list(filter(lambda s: s.find("@@") != -1, lines))
        for i in range(len(lines)):
           lines[i] = self.parse_line(lines[i])
        lines = list(map(lambda s: int(s), lines))
        self.diffs = lines
        return lines
        
    # parse a diff line to get line number
    def parse_line(self, line):
        line = line[line.find("+")+1:]
        end = line.find(",") 
        if end == -1:
            end = line.find(" @")
        return line[:end]
    
    # return True if line contains a comment
    # char is the comment delimiter
    def is_comment(self, line, char):
        return line.find(char) != -1 and line.count('"', 0, line.find(char)) % 2 == 0            
    
    ''' returns a list of line numbers of affected comments 
           a comment is affected if a line of code after it but before the next 
           comment has been modified
    '''
    # TODO: make comment finder algorithm more fine grained
    def find_comments(self):
        print(self.diffs)
        with open(self.file, "r") as fd:
            
            
            # a list of tuples in the form (comment_line, comment, diff_line, diff)
            comments = []
            lineno = 1
            last_comment = None
            multiline = False 
            
            # iterate over the lines in the file
            lines = list(iter(fd.readline, ''))
            for line in lines:
                
                # found the start of a multiline comment 
                if self.is_comment(line, self.LANG.get_multiline_start()):
                    multiline = True
                    last_comment = lineno
                
                # ignore contents of a multiline comment
                elif multiline:
                    pass
                
                # found end of a multiline comment
                elif self.is_comment(line, self.LANG.get_multiline_end()):
                    multiline = False 
                
                # found a singleline comment
                elif self.is_comment(line, self.LANG.get_single()):
                    last_comment = lineno
                
                # found a diff with an unedited comment
                elif (lineno in self.diffs and last_comment and 
                      last_comment not in self.diffs):
                    comments.append((last_comment,lines[last_comment-1], lineno, line))
                    last_comment = None
                    
                lineno += 1
        self.comments = list(comments)
    
    # print output string
    def build_output(self):
        
        if len(self.comments) == 0:
            return 
                
        string = "\n"
        output_len = self.output_len

        for comment in self.comments:
            string += ("possible outdated comment at " + self.file + ":" + str(comment[0]) + ':\n\t "')
            string += comment[1][0:output_len].replace("\n", "").strip()
            if (len(comment[1]) > output_len):
                string += "..."
            string += ('"\nfor diff at ' + self.file + ":" + str(comment[2]) + ':\n\t "')
            string += comment[3][0:output_len].replace("\n", "").strip()
            if (len(comment[3]) > output_len):
                string += "..."
            string += '"\n\n'
        print(string, end="", file=self.output)
    
    # parse a file
    def parse(self):
        self.find_comments()
        self.build_output()
        #os.remove(self.DIFF_FILE)

# handle arguments
def create_parser():
    argp = argparse.ArgumentParser(
            description='Check if your comments are out of date')
    argp.add_argument('-f', '--file', type=str, help='file to check', required=True)
    return argp


#entry point        
def main():
    argp = create_parser()
    args = argp.parse_args()  
    dater = CommentDater(args.file)
    dater.parse()
        
            
    