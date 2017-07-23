# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
#
#
# import re
#
# a=re.compile(r'\D+')
#
# if a.match('abc123'):
# 	print a.match('hello1123').group()  ##在第一个位置进行搜搜
#     print a.search('hello1123').group() ##在全局里面搜索,但是只匹配一个地方
# else:
# 	print 'match nothing
#
str1 = "abcdefabcdefgghj"
listStr = []
for eachStr in str1:
    countStr = str1.count(eachStr)
    print eachStr+':'+str(countStr)
    numStr = eachStr + ":" + str(countStr)
    if numStr not in listStr :
        listStr.append(numStr)
for i in listStr:
    print i