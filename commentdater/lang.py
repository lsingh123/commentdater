#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 12:10:06 2019

@author: lavanyasingh
"""
from enum import Enum
from pycparser import c_parser, c_ast, parse_file

COMMENTS = {"py_multiline_open": "'", "py_multiline_close":"'", "py_single": "#", 
                "c_multiline_open": "/*", "c_multiline_close":"*/", "c_single": "//"}

class FuncDefVisitor(c_ast.NodeVisitor):
    def __init__(self, lang):
        self.lang = lang
        
    def visit_FuncDef(self, node):
        self.lang.function_defs.append((node.decl.name, node.decl.coord))

# type to represent the language of a file
class Lang(Enum):
    c = 1
    java = 2
    python = 3
    
    def __init__(self, Enum):
        self.function_defs = None
    
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
    
    def is_function(self, line):
        if self is Lang.python:
            self.python_is_function(self, line)
        if self is Lang.c:
            self.c_is_function(self, line)
        if self is Lang.java:
            self.java_is_function(self, line)
    
    def set_filename(self, file):
        self.filename = file
    
    # TODO: wtf am i gonna do about errors
    # this is completely broken jesus 
    def c_is_function(self, line):
        print(self.function_defs)
        if self.function_defs is None:
            self.function_defs = []
            ast = parse_file(self.filename, use_cpp=True,
                     cpp_args=r'-Iutils/fake_libc_include')
            v = FuncDefVisitor(self)
            v.visit(ast)
            print(self.function_defs)
        return line in self.function_defs
    
    def python_is_function(self, line):
        # use the ast library to parse
        return None
        

        