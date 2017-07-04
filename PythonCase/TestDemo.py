#!/usr/bin/python
# -*- coding: UTF-8 -*-
##题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
w=0
list=[1,2,3,4]
for i in list:
	for y in list:
		for z in list:
			if (i==y)or(y==z)or(i==z):
				continue
			print str(i)+str(y)+str(z)
			w+=1
print w
