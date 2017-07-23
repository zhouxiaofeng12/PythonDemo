# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
#英文一个句子，用正则表达式统计一下有几个单词？


import re

#方法1:
stringA=raw_input('英文一个句子:')
ListA=re.findall(r'\w+',stringA)
y=0
for i in ListA:
    y+=1
print y

#方法2:
stringA=raw_input('英文一个句子:')
ListA=re.findall(r'\w+',stringA)
print len(ListA)