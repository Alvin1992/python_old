# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 23:02:25 2015

@author: fanrongxin
"""

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a lsit:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

test = ''' can I do this? '''

print "%r" % test