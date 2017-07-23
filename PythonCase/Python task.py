#!/user/bin/python
#-*- coding:UTF-8 -*-
#
#1.输入1-127的ascii码并输出对应字符
#方法1:
# code=0
# s=''
# for i in range(128):
#     s+=chr(code+i)
# print s

#方法2:
# for i in range(1,128):
#     print chr(i)
#

#2.输入a，b，c，d4个整数，计算a+b-c*d的结果
# def count(a,b,c,d):
#     cou= int(a+b-c*d)
#     print str(cou)
#     return
#
# count(0,3,5,6)
#
#3.计算一周有多少分钟、多少秒钟,计算出多少秒钟,入参为周
# def week_to_sec(wek):
#     sec=wek*7*24*60*60
#     print str(wek)+'周有'+str(sec)+'s'
#
# 计算出多少分钟
# def week_to_mi(min):
#     xx=min*7*24*60
#     print str(min)+'周有'+str(xx)+'m'
#
# week_to_mi(1)   #一周有多少分钟
# week_to_sec(1)  #一周有多少秒

#方法2:
# days_in_a_week=7
# hours_in_a_day=24
# mins_in_a_hour=60
# secs_in_a_minute=60
# print  days_in_a_week*hours_in_a_day* mins_in_a_hour*secs_in_a_minute

#4.3个人在餐厅吃饭，想分摊饭费。总共花费35.27美元，他们还想给15%的小费。每个人该怎么付钱，

# def halve(number):
#     zz=(float(35.27)+float((35.27)*0.15))/3
#     yy='%.2f' % zz       #'%.2f' % a 方式最好,保留小数的两位
#     print yy
# halve(3)
#
# a=35.27*(1+0.15)*100/3/100
# print '%.2f'%a  #保持2位小数
# print '%.1f'%a #保持1位小数
# print round(a) ##四舍五入

#5.计算一个12.5m X 16.7m的矩形房间的面积和周长
# def area(x,y):
#     print '求出来周长'+str((x+y)*2)
#
# def gir(z,w):
#  print '求出来面积'+ str(z*w)
#
# area(12.5,16.7)
# gir(12.5,16.7)

# ##圆的面积
# import math
# r=2
# pi=math.pi
# s=pi*pow(r,2)
# print '面积为%.2f'%s  #保持两位小数





# #6.怎么得到9 / 2的小数结果
# def div(x,y):
#     print float(x/y)
#
# div(9,2)

#7.python计算中7 * 7 *7 * 7，可以有多少种写法
# i=0
# str=1
# while i<4:
#     str*=7
#     i=i+1
# print str
#
# print pow(7,4)
#
# print 7**4
#
# print eval('%s*%s*%s*%s' %(7,7,7,7))  #把里面的表达式最计算
#
# a=7
# for i in range(3):
#     a*=7
#
# "*7" * 4
# ("*7" * 4)[1:]
# eval(("*7" * 4)[1:])
# 2401
#
#
# a=['7']*4
# "*".join(a)
# eval("*".join(['7']*4))

# #8.写程序将温度从华氏温度转换为摄氏温度。转换公式为C = 5 / 9*(F - 32)
# def Operating(F):
#     C=float(5.0/ 9*(F - 32))
#     print '当前的摄氏%.2f'%C
#
# Operating(100)



#9.一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，如果
#购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣(10%或20%)和最终价格。
# price=float(raw_input("please input a number:"))
# if (price>=50 and price<=100):
#     print '打折后的价格为%f'%round(price*0.9)
# elif (price>100):
#     j=round(price * 0.8)
#     print '打折后的价格为%.2f' % j
# else:
#     print '当前程序不支持此价格'
#
#     # coding=utf-8
#
#     customer_price = float(raw_input("please input pay money:"))
#     if customer_price >= 50 and customer_price <= 100:
#         print "disconunt 10%% ,after discount you shoud pay %s" \
#               % (customer_price * (1 - 0.1))
#     elif customer_price > 100:
#         print "disconunt 20%% ,after discount you shoud pay %s" \
#               % (customer_price * (1 - 0.2))
#     else:
#         print "disconunt 0%% ,after discount you shoud pay %s" \
#               % customer_price
#

# 10.判断一个数n能否同时被3和5整除
# x=input('input an number:')
# if x%3==0 and x%5==0:
#     print '%d 数据同时能被3/5整除' %x
# else:
#     print '%d 数据不能同时能被3/5整除'%x


#11.求1 + 2 + 3 +....+100之和
# num=0
# for i  in  range(1,100):
#     num+=i
# print num
#
# i=0
# while i<101:
#     i=i+1
# print i

#12.交换两个变量的值
# temp=''
# x=raw_input('请输入你想输入的值A：')
# y=raw_input('请输入你想输入的值B：')
# temp = x
# x=y
# y=temp
#
# print '请输入你想输入的值A:'+x
# print '请输入你想输入的值B:'+y




#13.一个足球队在寻找年龄在10到12岁的小女孩(包括10岁和12岁)加入。
# # 编写一个程序，询问用户的性别(m表示男性，f表示女性)和年龄，
# # 然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数
# #
# count=0
# while count<3:
#     count = count + 1
#     age = input('你的年纪是:')
#     sex = raw_input('你的性别是:')
#     if sex=='f' and 10<=age<=12:
#         print '满足条件'
#     else:
#         print '不满足条件'

#14.长途旅行中，刚到一个加油站，距下一个加油站还有200km，而且以后每个加油站之间距离都是200km。编写一个程
#序确定是不是需要在这里加油，还是可以等到接下来的第几个加油站再加油。
#程序询问以下几个问题:
#1)你车的油箱多大，单位升 2)目前油箱还剩多少油，按百分比算，比如一半就是0.5 3)你车每升油可以走多远(km)
#提示:
#油箱中包含5升的缓冲油，以防油表不准。





# 15.现有面包、热狗、番茄酱、芥末酱以及洋葱，数字显示有多少种订购组合，其中面包必订，0不订，1订，比如10000， 表示只订购面包
# bread=100
# dog=200
# tomato=50
# mustard=31
# Onion=1
# # for bread in ['1']:
# #     for hot in ['0','1']:
# #         for jam in ['0','1']:
# #             for jiemo in ['0','1']:
# #                 for onino in ['0','1']:
# #                     print "*" * 50
# #
# #                     print bread+hot+jam+jiemo+onino
# #                     print int(bread)*bread+int(hot)*dog + int(jam)*tomato + int(jiemo)*mustard + int(onino)*Onion
# #                     print
#
#                     # coding=utf-8
#
#                     cal_in_bread = 1
#                     cal_in_hotdog = 1
#                     cal_in_jam = 1
#                     cal_in_jiemo = 1
#                     cal_in_onion = 1
#
#                     for bread in ["1"]:
#                         for hotdog in ["1", "0"]:
#                             for jam in ["1", "0"]:
#                                 for jiemo in ["1", "0"]:
#                                     for onion in ["1", "0"]:
#                                         print "*" * 50
#                                         print bread + hotdog + jam + jiemo + onion
#                                         print int(bread) * cal_in_bread + int(hotdog) * cal_in_hotdog + int(
#                                             jam) * cal_in_jam + int(jiemo) * cal_in_jiemo + int(onion) * cal_in_onion


# 16.基于上题:给出每种食物的卡路里(自定义)，再计算出每种组合总共的卡路里
# bread=100
# dog=200
# tomato=50
# mustard=31
# Onion=1
#
# xx=bread*dog*tomato*mustard*Onion



#17.输入5个名字，排序后输出
# a=[]
# i=0
# while(i<5):
#     x=raw_input('请输入你的名字:')
#     a.append(x)
#     i+=1
# print '输入的名字依次是:'+str(a)


# 18.实现一个简单的单词本 功能:
# 可以添加单词和词义，当所添加的单词已存在，让用户知道;
# 可以查找单词，当查找的单词不存在时，让用户知道;
# 可以删除单词，当删除的单词不存在时，让用户知道;
#  以上功能可以无限制操作，直到用户输入bye退出程序。

# WordsBook=[]
# while True:
#     word=raw_input('请输入你想输入的单词:')
#     if  word == 'bye':
#          break
#     elif word in WordsBook:
#         print '该字符已经存在于单词本里面了'
#     elif word not in WordsBook:
#         prin  '该字符不存在于单词本里面了'
#         WordsBook.append(word)
#
#     else:
#         try:
#             del WordsBook[word]
#         except:
#             print '该单词无法删除'
#         WordsBook.append(word)
#
#
#19.输入一个正整数,输出其阶乘结果
# num = int(input("请输入一个数字: "))
# factorial = 1
# # 查看数字是负数，0 或 正数
# if num < 0:
#     print("抱歉，负数没有阶乘")
# elif num == 0:
#     print("0 的阶乘为 1")
# else:
#     for i in range(1, num + 1):
#         factorial = factorial * i
#     print("%d 的阶乘为 %d" % (num, factorial))
#


# ##20 计算存款利息 4种方法可选:活期,年利率为r1;一年期定息,年利率为r2;存两次半年期定期,年利率为r3两年期定息,年利率为r4
# #现有本金1000元,请分别计算出一年后按4种方法所得到的本息和。
# #提示 :本息= 本金+ 本金* 年利率* 存款期
# r1=1
# r2=2
# r3=3
# r4=4
# current=fixed=half_fixed= xx = yy=0
# current1=1000+1000*r1*1
# fixed=1000 + 1000 * r2 *1
# half_fixed=1000 + 100 * r3 *1
# xx = 1000 + 1000 * r4 * 0.5
# yy=current+fixed+half_fixed+xx
#
# print yy


# #21.输入3个数字,以逗号隔开,输出其中最大的数
# A1 = raw_input("请输入一个数字:")
# A2 = raw_input("请输入一个数字:")
# A3 = raw_input("请输入一个数字:")
# # print max(A1,A2,A3)
#


#22输入一个年份,输出是否为闰年是闰年的条件:能被4整数但不能被100整除,或者能被400整除的年份都是闰年
# # year= input("请输入一个年份:")
# # if  year%4==0 and year%100!=0 or year%400==00:
# #     print '今年是闰年'
# # else:
# #     print '今年不是闰年'
#
# # #23.求两个正整数m和n的最大公约数
# def hcf(x, y):
# # 获取最小值
#     if x > y:
#         smaller=y
#         biger=x
#     else:
#         smaller=x
#         biger=y
#     if biger%smaller==0:
#         hcf=smaller
#     else:
#         for i in range(1,(smaller + 1)/2):
#             if((x % i == 0) and (y % i == 0)):
#                 hcf = i
#     return hcf
#
#
# # 用户输入两个数字
# num1 = int(input("输入第一个数字: "))
# num2 = int(input("输入第二个数字: "))
#
# print num1,"和", num2,"的最大公约数为", hcf(num1, num2)