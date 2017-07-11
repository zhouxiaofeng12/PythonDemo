# #!/user/bin/python
# #-*- coding:UTF-8 -*-
#
#
#
# # # #计算一周有多少分钟、多少秒钟
# # #
# # # #计算出多少秒钟,入参为周
# # # def week_to_sec(wek):
# # #     sec=wek*7*24*60*60
# # #     print str(wek)+'周有'+str(sec)+'s'
# # #
# # # #计算出多少分钟
# # # def week_to_mi(min):
# # #     xx=min*7*24*60
# # #     print str(min)+'周有'+str(xx)+'m'
# # #
# # # week_to_mi(1)   #一周有多少分钟
# # # week_to_sec(1)  #一周有多少秒
# #
# #
# # #
# # # #3个人在餐厅吃饭，想分摊饭费。总共花费35.27美元，他们还想给15%的小费。每个人该怎么付钱，
# # #
# # # def halve(number):
# # #     xx=float((35.27/number)*0.15)
# # #     yy='%.2f' % xx  #'%.2f' % a 方式最好,保留小数的两位
# # #     print yy
# # #
# # # halve(3)
# #
# # # #计算一个12.5m X 16.7m的矩形房间的面积和周长
# # def area(x,y):
# #     print '求出来周长'+str((x+y)*2)
# #
# # def gir(z,w):
# #  print '求出来面积'+ str(z*w)
# #
# # area(12.5,16.7)
# # gir(12.5,16.7)
# #
# # #怎么得到9 / 2的小数结果
# # def div(x,y):
# #     print x/y
# #
# # div(9,2)
#
#python计算中7 * 7 *7 * 7，可以有多少种写法
#第一种
i=0
str=1
while i<4:
    str*=7
    i=i+1
print str

# #写程序将温度从华氏温度转换为摄氏温度。转换公式为C = 5 / 9*(F - 32)
def Operating(F):
    C=5 / 9*(F - 32)
    print C

Operating(33)


# # #一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，如果
# # # 购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣(10%或20%)和
# # #最终价格。
# # price=raw_input("please input a number:")
# # jiage=int(price)
# # if (jiage>50 and jiage<100):
# #     j=jiage*0.01
# # elif (jiage<100):
# #     j=jiage * 0.02
#
#
# # #求1 + 2 + 3 +....+100之和
# # num=0
# # for i  in  range(1,100):
# #     num+=i
# # print num
# #
#
# # #判断一个数n能否同时被3和5整除
# # x=input('input an number:')
# # if x%3==0 and x%5==0:
# #     print '%d 数据同时能被3/5整除' %x
# # else:
# #     print '%d 数据不能同时能被3/5整除'%x
#
#
# # #交换两个变量的值
# # temp=''
# # x=raw_input('请输入你想输入的值A：')
# # y=raw_input('请输入你想输入的值B：')
# # temp = x
# # x=y
# # y=temp
# #
# # print '请输入你想输入的值A:'+x
# # print '请输入你想输入的值B:'+y
#
# ###一个足球队在寻找年龄在10到12岁的小女孩(包括10岁和12岁)加入。编写一个程序,询问用户的性别(m表示男性,
# ###f表示女性)和年龄,然后显示一条消息指出这个人是否可以加入球队,询问10次后,输出满足条件的总人数。
# # i=0
# # a=0
# # while i<10:
# #     sex = raw_input('请输入你的性别：')
# #     age = raw_input('请输入你的年纪：')
# #     if sex=='f' and '10'<=age<='12':
# #         print '能加入球队'
# #         a+=1
# #         i+=1
# #     else:
# #         print '不能加入球队'
# #         i+=1
# # print '满足要求的球队为%d'%a
#
#
#
#长途旅行中,刚到一个加油站,距下一个加油站还有200km,而且以后每个加油站之间距离都是200km。编写一个程
#序确定是不是需要在这里加油,还是可以等到接下来的第几个加油站再加油。
#程序询问以下几个问题:
# 1)你车的油箱多大,单位升
# 2)目前油箱还剩多少油,按百分比算,比如一半就是0.5
# 3)你车每升油可以走多远(km)
#提示:
#油箱中包含5升的缓冲油,以防油表不准。
#1升汽油大约可以行驶12.5公里
# oil_big = raw_input('请检查一下你的油箱有多大：')
# oil_volume = raw_input('请检查一下油箱剩多少油：')
# oil_km = raw_input('请确定每升油可以走多远')
# Km=(oil_km*oil_volume*oil_big)-(5*oil_km)
# if 200-Km==0:
#     print '你需要加油了'
# elif 200-Km>0:
#     if 200-Km


# ##现有面包、热狗、番茄酱、芥末酱以及洋葱,数字显示有多少种订购组合,其中面包必订,0不订,1订,比如10000, 表示只订购面包
#
#
# # #输入一个正整数,输出其阶乘结果
# num = int(input("请输入一个数字: "))
# factorial = 1
#
# # 查看数字是负数，0 或 正数
# if num < 0:
#     print("抱歉，负数没有阶乘")
# elif num == 0:
#     print("0 的阶乘为 1")
# else:
#     for i in range(1, num + 1):
#         factorial = factorial * i
#     print("%d 的阶乘为 %d" % (num, factorial))

# #输入3个数字,以逗号隔开,输出其中最大的数
# A1 = raw_input("请输入一个数字:")
# A2 = raw_input("请输入一个数字:")
# A3 = raw_input("请输入一个数字:")
# print max(A1,A2,A3)

##求两个正整数m和n的最大公约数

# ##22输入一个年份,输出是否为闰年是闰年的条件:
# #能被4整数但不能被100整除,或者能被400整除的年份都是闰年
# year= input("请输入一个年份:")
# if  year%4==0 and year%100!=0 or year%400==00:
#     print '今年是闰年'
# else:
#     print '今年不是闰年'


###20 计算存款利息 4种方法可选:
#活期,年利率为r1;
#一年期定息,年利率为r2;
#存两次半年期定期,年利率为r3
#两年期定息,年利率为r4
##现有本金1000元,请分别计算出一年后按4种方法所得到的本息和。
#提示 :本息= 本金+ 本金* 年利率* 存款期
# r1=1
# r2=2
# r3=3
# r4=4
# current=fixed=half_fixed= xx = yy=0
# def current():
#     current=1000+1000*r1*1
#     fixed=1000 + 1000 * r2 *1
#     half_fixed=1000 + 100 * r3 *1
#     xx = 1000 + 1000 * r4 * 0.5
#     yy=current+fixed+half_fixed+xx
#
# print yy


