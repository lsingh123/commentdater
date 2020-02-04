#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 13:17:40 2020

@author: lavanyasingh
"""

from lang import Lang
from pycparser import c_parser, c_ast, parse_file


class FuncDefVisitor(c_ast.NodeVisitor):
    def __init__(self, lang):
        self.lang = lang
        
    def visit_FuncDef(self, node):
        self.lang.function_defs.append((node.decl.name, node.decl.coord))

class Parser:
    def __init__(self, lang, file):
        self.lang = lang
        self.file = file 
        self.function_defs = None
        
    def is_function(self, line):
        if self is Lang.python:
            self.python_is_function(self, line)
        if self is Lang.c:
            self.c_is_function(self, line)
     