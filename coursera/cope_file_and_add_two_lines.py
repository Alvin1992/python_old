# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 22:04:27 2015

@author: fanrongxin
"""

f = open(r'./src.txt')

content = f.readlines()

f.close()

t = open(r'./dest.txt', 'w') # a+ 也可以

t.write("How many roads must a man walk down\n\nBefore they call him a man\n\n")

t.writelines(content)

t.close()
