#!/user/bin/python
#-*- coding:UTF-8 -*-

dict = {'Alice': '2341', 'Test': 9102, 'Cecil': 3258,'A':1,'A':2}
print dict.keys()   #以列表返回一个字典所有的值


for key in dict:
    print key

for key in dict.keys():
    print key

for value in dict.values():
    print value

for key,value in dict.items():
     print key,value

dict.setdefault('Test',1)
print dict


dict.fromkeys([1,2,3],'a')
print dict


#
# >>> x.setdefault("a",1)
# 1
# >>> x
# {'a': 1}
# >>> x.setdefault("a",1000)
# 1
# >>> print x
# {'a': 1}