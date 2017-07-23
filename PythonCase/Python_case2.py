#!/user/bin/python
#-*- coding:UTF-8 -*-

#1.使用尽可能多的方法实现list去重
listA=[1,2,3,4,1,2,3,4]
listC=[]
for i in listA:
    if i not in listC:
        listC.append(i)

print listC


#2.成绩等级判断 利用条件运算符的嵌套来完成此题:
# 学习成绩>=90分的同学用A表示, 60-89分之间的用B表示,60分以下的用C表示
score=input('请输入成绩:')
if score>=90:
    print 'A'
elif 60<score<89:
    print 'B'
else:
    print 'C'

#3.实现数学中多项式求和公式的打印
#比如:a6x^6 + a5x^5 + a4x^4 + a3x^3 + a2x^2 + a1x^1 + a0




#4.统计名字列表中,各名字的首字母在名字列表中出现的次数
namelist=['zhoufeng','zhouzimeng','zhouzimo','wangshijie','wangzhang','mize']
strA=''
for i in namelist:
    countStr=1
    for z in i[0]:
        strA=strA+z
print strA  #zzzwwm
for eachStr in strA:
    countStr = strA.count(eachStr)
    print eachStr + ':' + str(countStr)


# #5.输入三个数，判断是否能构成三角形
# # 能构成三角形三边关系:
# #    三边都大于零
# #   两边之和大于第三边，两边之差小于第三边
x=input('输入第一个数:')
y=input('输入第二个数:')
z=input('输入第三个数:')
if (x>0 and y>0 and z>0) and x+y>z and x-y<z:
    print '可以构成三角形'
else:
    print '不可以构成三角形'




#6.实现字典的fromkeys方法
#例如:
#seq = ('name', 'age', 'sex')
#dict = dict.fromkeys(seq, 10)
#print "New Dictionary : %s" % str(dict)
#结果:New Dictionary : {'age': 10, 'name': 10, 'sex': 10}



#7.键盘读入一字符串，逆序输出
keyword=raw_input('raw input char')
s=[keyword]
i=len(keyword)
print s[-1:-i:-1]

# #8.读入一个整数n，输出n的阶乘
def fac(n):
    result = 1
    if n<2:
        return 1
    else:
        for i in range(1,n+1):
            result*=i
        return result

print fac(4)
print fac(1)


##9.打印1/2, 1/3, 1/4,....1/10

for i in range(2,11):
    print str(1)+'/'+str(i)

#10.写一个函数实现一个数学公式
def fum(x,y):
    sum=x+y
    return sum

print fum(2,3)

#11.输入数字a，n，如a，4，则打印a+aa+aaa+aaaa之和
def sum(x,y):
    result = ''
    a =''
    for i in range(1,y+1):
        result=x*i
        a=a+'+'+result
        #b+bb+bbb+
    print a[1:]

sum('b',4)

# #求100个随机数之和，随机数要求为0—9的整数
# import random
#
# def sum():
#     for i in random.randint(0, 9):
#         print i2

#13.要求在屏幕上分别显求1到100之间奇数之和与偶数之和



#14.输入10个数，并显示最大的数与最小的数
i = 0
a=[]
while i<10:
    x=input('请输入一个数:')
    a.append(x)
    i+=1
print max(a)
print min(a)



