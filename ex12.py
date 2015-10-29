# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 16:51:43 2015

@author: fanrongxin
"""

age = raw_input("How old are you ")
height = raw_input("How tall are you ")
weight = raw_input("How much do you weigh? ")

print "So, you are %r old, %r tall and %r weight" % (age, height, weight)

#raw_input(...)
#    raw_input([prompt]) -> string
    
#     Read a string from standard input.  The trailing newline is stripped.
#     If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
#     On Unix, GNU readline is used if enabled.  The prompt string, if given,
#     is printed without a trailing newline before reading.
    
#input(...)
#    input([prompt]) -> value
    
#    Equivalent to eval(raw_input(prompt)).