#!/user/bin/python
#-*- coding:UTF-8 -*-
s = "abaaaceadgescdwesjgdk"
for i in s:
    pass
count={}
for i in s:
    if count.has_key(i):
        count[i]=count[i]+1
    else:
        count[i]=1
print count