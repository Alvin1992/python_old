# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 22:28:51 2015

@author: fanrongxin
"""

def f(x):
    global a
    print a
    a = 5
    print a + x

a = 3

f(8)

print a