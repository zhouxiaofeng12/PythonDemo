#!/usr/bin/python
#-*- coding: UTF-8 -*-

#有一个字符串,我们想通过一个循环按照这样的形式显示它,每次都把位于最后的字符砍掉
a='adbdfbdkafhlkadf'
for i in  range(-1,-len(a),-1):
    print a[:i]

# print a[:-1]  #反转
# print a[1:]
# print a[0:]
# print a[:]    #全部列表
# print a[-len(a):-1]
# print a[::2]
# print a[::3]
# print a[::6]
# print a[::-1]
print  range(1,5)  ##代表从1到5(不包含5)
print range(-1,-len(a),-1)   ##返回从-1 到 头的角标

