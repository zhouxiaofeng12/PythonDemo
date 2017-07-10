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



#
#
# #一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，如果
# # 购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣(10%或20%)和
# #最终价格。
# price=raw_input("please input a number:")
# if (price>50 and price<100):
#     print price*0.01
# elif (price<100):
#     j=price * 0.02
#     print j
#
#
# # #求1 + 2 + 3 +....+100之和
# # num=0
# # for i  in  range(1,100):
# #     num+=i
# # print num
# #

#
# #判断一个数n能否同时被3和5整除
# n=input('请输入一个数值:')
# if n%3 ==0 and n %5==0:
#     print '能够被整除'
# else:
#     print '不能够被整除'
#
#
# #交换两个变量的值
# def change(a,b):


# ##一个足球队在寻找年龄在10到12岁的小女孩(包括10岁和12岁)加入。
# # 编写一个程序，询问用户的性别(m表示男性，f表示女性)和年龄，
# # 然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数
#
# count=0
# while True:
#     age = input('你的年纪是:')
#     sex = raw_input('你的性别是:')
#     if sex=='f' and 10<=age<=12:
#         count=count+1
#     else:
#         print '不满足条件'



###交换两个变量的值
# temp=''
# x1=raw_input('请输入x1的值:')
# y2=raw_input('请输入y2的值:')
# temp = x1
# x1 = y2;
# y2 = temp;
#
# print x1
# print y2


#现有面包、热狗、番茄酱、芥末酱以及洋葱，数字显示有多少种订购组合，
        # 其中面包必订，0不订，1订，比如10000， 表示只订购面包


# #输入5个名字，排序后输出
# a=[]
# i=0
# while(i<5):
#     x=raw_input('请输入你的名字:')
#     a.append(x)
#     i+=1
# print '输入的名字依次是:'+str(a)


#实现一个简单的单词本 功能:
# 可以添加单词和词义，当所添加的单词已存在，让用户知道;
# 可以查找单词，当查找的单词不存在时，让用户知道;
# 可以删除单词，当删除的单词不存在时，让用户知道;
#  以上功能可以无限制操作，直到用户输入bye退出程序。
#
# WordsBook=[]
# while True:
#     word=raw_input('请输入你想输入的单词:')
#     if  word == 'bye':
#          break
#     elif word in WordsBook:
#         print '该字符已经存在于单词本里面了'
#     elif word not in WordsBook:
#         print '该字符不存在于单词本里面了'
#         WordsBook.append(word)
#
#     else:
#         try:
#             del WordsBook[word]
#         except:
#             print '该单词无法删除'
#         WordsBook.append(word)


###输入一个正整数，输出其阶乘结果
# 亦即n!=1×2×3×...×n。阶乘亦可以递归方式定义：0!=1，n!=(n-1)!×n。
# 3!=1*2*3
# 4!=1*2*3*4
# n=1
#
# num=raw_input('请输入一个正整数:')
# if num==0:
#     print '阶乘为1'
# else:
#     *(num-1)*num