# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 11:02:54 2015

@author: fanrongxin
"""


import math
def fun(num):
    if num<0:
        print '-',
        num = -num
    if num/10:
        fun(num/10)
    print chr(num%10+48)
    
fun(-1234)