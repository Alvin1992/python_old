# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 22:30:29 2015

@author: fanrongxin
"""

from random import randint

x = randint(0, 300)

for count in range(0, 5):
    print 'please input a number between 0 and 300'
    digit = input()
    if x == digit:
        print 'bingo'
    elif x > digit:
        print 'too small and try agin'
    else:
        print 'too large and try again'