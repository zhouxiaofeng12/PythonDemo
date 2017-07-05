#!/user/bin/python
#-*- coding:UTF-8 -*-

# #计算一周有多少分钟、多少秒钟
#
# #计算出多少秒钟,入参为周
# def week_to_sec(wek):
#     sec=wek*7*24*60*60
#     print str(wek)+'周有'+str(sec)+'s'
#
# #计算出多少分钟
# def week_to_mi(min):
#     xx=min*7*24*60
#     print str(min)+'周有'+str(xx)+'m'
#
# week_to_mi(1)   #一周有多少分钟
# week_to_sec(1)  #一周有多少秒



#3个人在餐厅吃饭，想分摊饭费。总共花费35.27美元，他们还想给15%的小费。每个人该怎么付钱，

def halve(number):
    xx=float((35.27/number)*0.15)
    yy='%.2f' % xx  #'%.2f' % a 方式最好,保留小数的两位
    print yy

halve(3)

#计算一个12.5m X 16.7m的矩形房间的面积和周长

