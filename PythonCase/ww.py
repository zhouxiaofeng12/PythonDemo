#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
a=b=0
for i in os.listdir('/Users/wangshijie/Documents'):
    if os.path.isfile(i):
        a+=1
    elif os.path.isdir(i):
        b+=1
    else:
        print '其他'

print a,b