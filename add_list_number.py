# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 18:17:25 2015

@author: fanrongxin
"""

test = open(r'./scompany.txt')

cNames = test.readlines()

for i in range(0, len(cNames)):
    cNames[i] = str(i+1) + ' ' + cNames[i]
test.close()
test1 = open(r'./scompany1.txt', 'w')
test1.writelines(cNames)
test1.close()