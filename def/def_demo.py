#!/user/bin/python
#-*- coding:UTF-8 -*-

##函数==
def printme(str):
    '打印传入的字符串到标准显示设备上'
    print str
    return

printme('我要调用用户自定义函数')
printme('再次调用同一个数据')


##python传入不可变对象实例
def ChangeInt(a):
    a=10
b=2
ChangeInt(2)
print b

def changeme(mylist):
    mylist.append([2,3223,133]);
    print "函数内取值",mylist
    return


mylist=[10,23,23,2424];
changeme(mylist);
print '函数外取值',mylist

