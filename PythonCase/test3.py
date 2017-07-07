# #!/user/bin/python
# #-*- coding:UTF-8 -*-
#
# # #计算一周有多少分钟、多少秒钟
# #
# # #计算出多少秒钟,入参为周
# # def week_to_sec(wek):
# #     sec=wek*7*24*60*60
# #     print str(wek)+'周有'+str(sec)+'s'
# #
# # #计算出多少分钟
# # def week_to_mi(min):
# #     xx=min*7*24*60
# #     print str(min)+'周有'+str(xx)+'m'
# #
# # week_to_mi(1)   #一周有多少分钟
# # week_to_sec(1)  #一周有多少秒
#
#
# #
# # #3个人在餐厅吃饭，想分摊饭费。总共花费35.27美元，他们还想给15%的小费。每个人该怎么付钱，
# #
# # def halve(number):
# #     xx=float((35.27/number)*0.15)
# #     yy='%.2f' % xx  #'%.2f' % a 方式最好,保留小数的两位
# #     print yy
# #
# # halve(3)
#
# # #计算一个12.5m X 16.7m的矩形房间的面积和周长
# def area(x,y):
#     print '求出来周长'+str((x+y)*2)
#
# def gir(z,w):
#  print '求出来面积'+ str(z*w)
#
# area(12.5,16.7)
# gir(12.5,16.7)
#
# #怎么得到9 / 2的小数结果
# def div(x,y):
#     print x/y
#
# div(9,2)

#python计算中7 * 7 *7 * 7，可以有多少种写法

#
#
#
# #写程序将温度从华氏温度转换为摄氏温度。转换公式为C = 5 / 9*(F - 32)
# def Operating(F):
#     C=5 / 9*(F - 32)
#     print C
# Operating(12)





#一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，如果
# 购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣(10%或20%)和
#最终价格。
price=raw_input("please input a number:")
if (price>50 and price<100):
    print price*0.01
elif (price<100):
    j=price * 0.02
    print j


# #求1 + 2 + 3 +....+100之和
# num=0
# for i  in  range(1,100):
#     num+=i
# print num
#


