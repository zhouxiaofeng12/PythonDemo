#!/user/bin/python
#-*- coding:UTF-8 -*-


#encoding=utf-8

def fromkeys(keys,value=None):
    d={}
    if isinstance(keys,(str,list,tuple)):
        for s in keys:
            d[s]=value

    return d

print fromkeys("abc","x")
print fromkeys(['a','b','c'],"z")
print fromkeys(('a','b','c'),"m")
print fromkeys(('a','b','c'),"")
print fromkeys(('a','b','c'),None)
print fromkeys('abc')   #不输入value的值,默认为None,必须传入两个值



