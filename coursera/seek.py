# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 19:10:31 2015

@author: fanrongxin
"""

s = "add some bad companies such as Tencent, Alibaba, Baidu"

f = open(r'./scompany.txt', 'a+')

f.writelines('\n')

f.writelines(s)

f.seek(0, 0)

x = f.readlines()

print x

f.close()