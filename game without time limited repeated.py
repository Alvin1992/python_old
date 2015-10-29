# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 15:29:46 2015

@author: fanrongxin
"""

from random import randint

x = randint(0, 300)

go = 'y'

while (go == 'y'):
    print 'please input a number between 0 and 300'
    digit = input()
    if digit == x:
        print 'bingo'
        break
    elif digit > x:
        print 'too large and try again'
    else:
        print 'too small and try again'
    print 'if you want to continue, please input "y" otherwise please input any key'
    go = raw_input('yes or not')
    
else:
    print 'goodbye'