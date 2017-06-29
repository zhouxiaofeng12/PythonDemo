#!/user/bin/python
#-*- coding:UTF-8 -*-

####创建100个文件夹
import os
i=1
while i<101:
	f=open('/Users/zhoufeng/Desktop/file/file%d'%i,'w')
	i+=1