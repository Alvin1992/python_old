# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 22:50:22 2015

@author: fanrongxin
"""

def scoreLevel():
    x = input()
    if x >= 90 and x <= 100:
        print 'A \n you are certainly a geneous'
    elif x >= 70 and x <= 89:
        print 'B \n pretty good'
    elif x >= 60 and x <= 69:
        print 'C \n good'
    elif x >= 50 and x <= 59:
        print 'D \n keep going'
    else:
        print 'Invalid score \n please give me a number between 0 and 100'

go = 'y'

while (go):
    scoreLevel()
    print 'if you want to continue to test other score, please input y otherwise please input any other key'
    go = raw_input('y or n')
else:
    print 'Hope you use this function next time'