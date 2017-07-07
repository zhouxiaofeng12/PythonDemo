#!/user/bin/python
#-*- coding:UTF-8 -*-

import os

# ####创建100个文件夹
# import os
# i=1
# while i<101:
# 	f=open('/Users/zhoufeng/Desktop/file/file%d'%i,'w')
# 	i+=1


##文件的定位逻辑
fo =open('/Users/zhoufeng/Desktop/java.txt','a+')
info1=fo.read()
# tmp=info1.decode("ascii").encode("utf-8")
# fo.write(tmp)
fo.seek(0,0)
print fo.read(6)

##循环列表
for i in fo:
    print i

