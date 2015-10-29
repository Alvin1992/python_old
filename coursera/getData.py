# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 22:01:50 2015

@author: fanrongxin
"""

import urllib
import re
dStr = urllib.urlopen('http://finance.yahoo.com/q/cp?s=%5EDJI+Components') \
.read()
m = re.findall('<tr><td class=\"yfnc_tabledata1\"><b><a href=\".*?\">\
(.*?)</a></b></td><td class=\"yfnc_tabledata1\">(.*?)</td>.*?<b>(.*?)</b>.*?</tr>', dStr)

if m:
    print m
    print '\n'
    print len(m)
else:  
    print 'not match'