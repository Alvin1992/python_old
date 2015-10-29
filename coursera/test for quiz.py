# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 12:54:54 2015

@author: fanrongxin
"""

def f(x):
    # print a
    #如果有上面这一句就会报错
    #因为局部变量会屏蔽外部变量
    #当有print a 的时候a还没赋值会报
    #local variable 'a' referenced before assignment的错误
    a = 7
    print a + x
    
a = 5

f(3)

print a