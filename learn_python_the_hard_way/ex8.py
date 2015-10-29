# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 16:51:48 2015

@author: fanrongxin
"""

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)

print formatter % ('one', 'two', 'three', 'four')

print formatter % (True, False, False, True)

print formatter % (formatter, formatter, formatter, formatter)

print formatter % (
        "I had this thing.",
        "That you could type up right.",
        "But it did't sing.",
        "So I siad goodnight."
)

print formatter % ("This is a trial", "I will use Chinese", 
                   "Let's check the result", "我是中文")              

formatter = "%s %s %s %s"

print formatter % ("This is a trial", "I will use Chinese", 
                   "Let's check the result", "我是中文")