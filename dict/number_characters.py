#!/user/bin/python
#-*- coding:UTF-8 -*-

#获取字符串中，数量相同的字符，计算出来个数
str='aasdfghasdfgh'
dict1={}
for i  in str:
    if dict1.has_key(i):
        dict1[i]=dict1[i]+1
    else:
        dict1[i]=1
print dict1


