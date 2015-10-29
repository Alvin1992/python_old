# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 22:43:24 2015

@author: fanrongxin
"""

from random import randint

x = randint(0, 300)

go = 'y'

while (go == 'y'):
    print 'please input a number between 0 and 300'
    digit = input()
    if x == digit:
        print 'bingo'
        break
    elif x > digit:
        print 'too small and try again'
    else:
        print 'too large and try again'
    print "if you don't want to continue, please input 'n' otherwise please input 'y'"
    go = raw_input('n or y')
    
else:
    print 'goodbye'