#!/user/bin/python
#-*- coding:UTF-8 -*-

#题目1：请写代码实现字典的fromkeys函数方法


dict={}
def fromkeys(key,values=None):
    if isinstance(key,str):
        for i in key:
            dict[i]=values
    elif isinstance(key,list):
        for f in key:
            dict[f]=values
    elif isinstance(key,tuple):
        for w in key:
            dict[w] = values
    else:
        dict[key] = values
    return dict


# print fromkeys((122112,1,'hfhfha',11212,'diaiifif'),2)
# print fromkeys([1,23,23],2)
print fromkeys('fffff')


#方法二：

###题目1：请写代码实现字典的fromkeys函数方法
dict={}
def fromkeys(key,values):
	if isinstance(key,(str,list,tuple)):
		for i in key:
			dict[i]=values
	else:
		dict[key]=values
	return dict

print fromkeys([1,2],23)
