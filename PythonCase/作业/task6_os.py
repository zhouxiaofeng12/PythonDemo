#!/user/bin/python
#-*- coding:UTF-8 -*-
import os
import sys
import shutil

#1.基础题:
#检验给出的路径是否是一个文件:
#检验给出的路径是否是一个目录:
#判断是否是绝对路径:
#检验给出的路径是否真地存:


# def check_right(path):
# 	if os.path.exists(path):
# 		return '当前路径是一个目录'
# 	elif os.path.isabs(path):
# 		return '当前路径是一个绝对路径'
# 	elif os.path.isfile(path):
# 		return '当前路径是一个文件'
# 	elif os.path.isdir(path):
# 		return '当前路径是一个目录'
# 	else:
# 		return '该路径啥都不是'

# print check_right('/Users/wangshijie/Desktop1/Demo')


# #2.返回一个路径的目录名和文件名
# def back_file(path):
# 	list=os.path.split(path)
# 	print  '目录为:%s'%list[0]
# 	print '文件名:%s'%list[1]

# floder='/Users/wangshijie/Documents/task7_task.py'
# back_file(floder)


##3.分离文件名与扩展名
# def back_file(path):
# 	list=os.path.split(path)
# 	name=os.path.splitext(list[1])
# 	print '文件名:%s'%name[0]
# 	print '扩展名:%s'%name[1]

# floder='/Users/wangshijie/Documents/task7_task.py'
# back_file(floder)


#4.找出某个目录下所有的文件，并在每个文件中写入“gloryroad”
# path=os.chdir('/Users/wangshijie/Documents/file测试')
# for line in os.listdir('.'):
#     if line =='.DS_Store':
#         print("系统默认生成文件,不处理")
#     else:
#         if os.path.isfile(line):
#             with open(line,'a+') as fp:
#                 fp.write('gloryroad')
#                 print '添加成功啦'


#5.如果某个目录下文件名包含txt后缀名，则把文件后面追加写一行“被我找到了!”
#
# def find_txt_file(path):
#     new_path=os.chdir(path)
#     for line in os.listdir('.'):
#         if line == '.DS_Store':
#             print("系统默认生成文件,不处理")
#         else:
#             if os.path.splitext(line)[1].split('.')[1]=='txt':
#                 with open(line, 'a+') as fp:
#                     fp.write('被我找到了')
#                     print '找到了txt的文档哈'
#             else:
#                 print '当前文件非txt'
#
# path='/Users/wangshijie/Documents/file测试'
# find_txt_file(path)

# #7.删除某个目录下的全部文件
# def dir_list(path):
#     os.chdir(path)
#     for Filename in os.listdir('.'):
#         if os.path.isfile(Filename):
#             os.remove(Filename)
#
# dir_list('/Users/wangshijie/Desktop/list')
#
#

# #8.统计某个目录下文件数和目录个数
# def count_file(path_list):
#     file_count = 0
#     dir_count = 0
#     os.chdir(path_list)
#     for Filename in os.listdir('.'):
#         if Filename=='.DS_Store':
#            continue
#         if os.path.isfile(Filename):
#             file_count+=1
#         elif os.path.isdir(Filename):
#             dir_count += 1
#     return '当前路径下的文件数为%s和目录数为:%s'% (file_count,dir_count)
#
# print count_file('/Users/wangshijie/Desktop')



# # 9.删除某个目录下的全部文件(仅限一级目录)
# def remove_file(path):
#     os.chdir(path)
#     for Filename in os.listdir('.'):
#         if os.path.isfile(Filename):
#             os.remove(Filename)
#
# pathA = '/Users/wangshijie/Desktop/Demo'
# remove_file(pathA)
#
# # 10.使用程序建立一个多级的目录，在每个目录下，新建一个和目录名字一样的txt文件
# os.chdir('/Users/wangshijie/Desktop/file')
# for i in range(10):
#     strA = 'test%s' % i
#     # path_road=os.path.join(path,strA)
#     # print path_road
#     os.mkdir(strA)
#     '/Users/wangshijie/Desktop/file/test0'
#     file = open(strA + '.txt', 'a+')
#     os.chdir(strA)
#
#
# # 11. 查找某个目录下是否存在某个文件名
# def find_file_name(path, name):
#     count = 0
#     os.chdir(path)
#     for Filename in os.listdir('.'):
#         if Filename == name.split('.'[0]):
#             print '该目录下存在该数据'
#         else:
#             count += 1
#     if count == len(os.listdir('.')):
#         print '该目录下不存在该数据'
#
#
# find_file_name('/Users/wangshijie/Documents/file测试', 'test')
#
# ##12. 用系统命令拷贝文件
# os.system('cp -r /Users/wangshijie/Desktop/如何统计.jpg  /Users/wangshijie/Desktop/Demo')
#
#
# ##13.输入源文件所在路径和目标目录路径，然后实现文件拷贝功能
#
# def copy_file(now_file_path, Goal_file_path, file):
#     for Filename in os.listdir(now_file_path):
#         if Filename == file:
#             print Filename
#             fp = open(now_file_path + os.sep + Filename, 'r+')
#             fp.seek(0, 0)
#             comment = fp.read()
#             print comment
#     os.chdir(Goal_file_path)
#     fp2 = open('new_file.txt', 'a+')
#     fp2.write(comment)
#     fp2.close()
#
#
# copy_file('/Users/wangshijie/Desktop/Demo/while demo', '/Users/wangshijie/Desktop', '帧率.txt')


# # 14.遍历某个目录下的所有图片，并在图片名称后面增加_xx
# def list_pic(path):
#     pic_gs = ['bmp', 'jpg', 'png', 'jpeg', 'gif', 'pcx', 'tga', 'exif', 'fpx', 'svg', 'psd']
#     os.chdir(path)
#     for Filename in os.listdir('.'):
#         if Filename != '.DS_Store':
#             if os.path.isfile(Filename):
#                 if Filename.split('.')[1] in pic_gs:
#                     os.rename(Filename, Filename + '_xx')
#
#
# list_pic('/Users/wangshijie/Documents/pic')
#
# ##15.遍历指定目录下的所有文件，找出其中占用空间最大的前3个文件
# def memory_dir(path):
#     memory_size={}
#     memory_size_list=[]
#     os.chdir(path)
#     for Filename in os.listdir('.'):
#         memory_size[os.path.getsize(Filename)]=Filename
#         memory_size_list.append(os.path.getsize(Filename))
#
#     for i in memory_size_list[-1:-4:-1]:
#         print memory_size[i]
#
# memory_dir('/Users/wangshijie/Desktop')



# #16、过滤py源码中的#注释,另存为文件result.py,并执行result.py,断言是否执行成功
# with open('/Users/zhoufeng/Desktop/find_max.py','r+')as fp:
#     list=fp.readlines()
#     seqlist='#!/user/bin/python\n'+'#-*- coding:UTF-8 -*-\n'
#     print list
#     fpA=open('/Users/zhoufeng/Desktop/result.py', 'a+')
#     fpA.write(seqlist)
#
#     for line in list:
#         if line.strip()=='':
#             print '当前行为空白行，不做处理'
#         else:
#                 if line.strip()[0]=='#':
#                     print '当前行为注释行'
#                 else:
#                     fpA.write(line)
#     fpA.close()
#
# comment=os.system('python /Users/zhoufeng/Desktop/result.py')
# if comment==0:
#     print '执行成功'
# else:
#     print '执行失败'


#17、文件访问,􏰀表示输入数字 N 和文件 F, 然后显示文件 F 的前 N 行.
# def access_file(num,file):
#     fp=open(file,'r+')
#     list_num=fp.readlines()
#     # print list_num
#     # for i in range(num):
#     #     print i
#     #
#     # # list=len(fp.readline())
#     # # print list
#     print list_num[0:num]
#
# access_file(10,'/Users/wangshijie/Desktop/a.py')




#18、从命令行接受1个路径如:c:\a\b\c\1.py, 实现1个函数创建目录a\b\c,创建文件1.py
# 实现1个函数删除已创建的目录及文件
# def dos_commend(path):
#     dir_path=os.path.split(path)[0]
#     print dir_path
#     file_name=os.path.split(path)[1]
#     print file_name
#     if not os.path.exists(dir_path):
#         os.makedirs(dir_path)
#     with open(path,'w+')as fp:
#         fp.read()
#
# def remove_dir(path):
#     file_name = os.path.split(path)[1]
#     dir_name = os.path.split(path)[0]
#     os.chdir(dir_name)
#     print file_name
#     os.removedirs(dir_name)
#
# # dos_commend('/Users/wangshijie/Desktop/a/b/c/xxxxxxx.py')
# remove_dir('/Users/wangshijie/Desktop/a/b/c/xxxxxxx.py')

#19、有一个ip.txt，里面每行是一个ip，实现一个函数，ping 每个ip的结果，把结果记录存到ping.txt中，格式为ip:0或ip:1 ，0代表ping成功，1代表ping失败
# import re
# fp=open('/Users/wangshijie/Desktop/ip.txt','r')
# fpA=open('/Users/wangshijie/Desktop/result.txt','a')
# for ip in fp:
#     if os.system('ping '+ip) == 0:
#         fpA.write(ip+':'+'1\n')
#         continue
#     else:
#         fpA.write(ip + ':' + '0\n')
#     fp.close()
#     fpA.close()
#

# fp = open(r"/Users/wangshijie/Desktop/ip.txt", "r")
# count = len(fp.readlines())
# fp.seek(0)
# fs = open(r"/Users/wangshijie/Desktop/result.txt", "a")
# for i in range(count):
#     ip = fp.readline().strip()
#     lenip = len(ip)
#     if os.system("ping " + ip) == 0:
#         fs.write(ip + ":0\n")
#     else:
#         fs.write(ip + ":1\n")
# fs.close()



# # 20、实现DOS命令执行功能，接受输入命令并执行，然后把执行结果和返回码打印到屏幕
# def dos_name(command):
#     if command=='exit':
#         exit(0)
#     os.system(command)
#
# now_input=raw_input('请输入命令行的数据:')
# dos_name(now_input)
#


# 21、文件访问 访问一存在多行的文件，
# 实现每隔一秒逐行显示文本内容的程序，每次显示文本文件的 5 行,
# 暂停并向用户表示“输入任意字符继续”，按回车键后继续执行，直到文件末尾。 显示文件的格式为:
#[当前时间] 一行内容，比如:[2016-07-08 22:21:51] 999370this is test
import time
with open('/Users/wangshijie/Desktop/ip.txt','a+') as fp:
    fp.seek(0,0)
    list=fp.readlines()
    print list
    for i in range(0,len(list)):
        if (i+1)%6==0:
            coment=raw_input('输入任意字符继续')
            time.sleep(1)
            print '['+time.strftime("%Y-%m-%d %H:%M:%S")+']' + str(list[i])
            continue
        else:
            time.sleep(1)
            print '['+time.strftime("%Y-%m-%d %H:%M:%S")+']' + str(list[i])
