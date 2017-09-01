# -*- coding: utf-8 -*-

import os
import shutil
from time import sleep
import xlrd
import xlwt
import re
from subprocess import Popen, PIPE
#
# def file_get_Detail(address):
#     file = os.listdir(address)  #获取地址下的所有文件夹
#     return file
#
# def Activity_Frame(Local):
#     j=1
#     workbook = xlwt.Workbook(encoding = 'utf8')
#     worksheet = workbook.add_sheet('Frame')
#
#     fp = open(Local+"/Frame/"+'帧率.txt','r+')
#     for line in fp:
#             # print line
#         name = re.split("\\s+", line.strip())
#         total = float(name[0])+float(name[1])+float(name[2])
#         fps = round(1000/total)
#         print fps
#         worksheet.write(j, 0, label = fps)
#         j+=1
#
#     workbook.save(Local + '/Frame/xx.xls')
#
#
#
# if __name__ == "__main__":
#
#     Local = "/Users/zhoufeng/Desktop/"
#     Activity_Frame(Local)
#

# #删除某个目录下的全部文件
#
# def remove_file(path):
#     os.chdir(path)
#     for Filename in os.listdir('.'):
#         if os.path.isfile(Filename):
#             os.remove(Filename)
#
# pathA='/Users/zhoufeng/Desktop/pythontest'
# remove_file(pathA)


#统计某个目录下文件数和目录个数

# 处理帧率
def Frame_file(Local):
    # # globals(path)
    workbook = xlwt.Workbook(encoding='utf8')
    worksheet = workbook.add_sheet('Frame')
    i = 0
    j = 1
    for Filename in os.listdir(Local):
        #依次循环，文件判断
        if Filename=='.DS_Store':
            print '空行不作处理'
        else:
            if os.path.splitext(Filename)[1]=='.txt':
                #获取txt的文件
                path_file=os.path.join(Local,Filename)
                fp = open(path_file,'r')
                for line in fp:
                    #获取行
                    if line.__contains__('.ui.activity'):
                        print '处理后续数据'
                    pattern=re.findall(".*activity.(.*)/android.*",line.strip())
                    if pattern[0]=='MainActivity':
                        print '不处理main'
                    else:
                        worksheet.write(0,i,pattern[0])
                        i=i+1
                        if line.__contains__('Execute'):
                            print '不做处理'
                        elif line.__contains__('display lists'):
                            print '不做处理'
                        else:
                            name=re.split(r'\s',line.strip())
                            total = float(name[0]) + float(name[1]) + float(name[2])
                            print(name[0], name[1], name[2])
                            print(total)
                            fps = round(1000 / total)
                            worksheet.write(j, i - 1, label=fps)
                            j += 1
                workbook.save(Local + '数据.xls')


Frame_file('/Users/zhoufeng/Desktop/Frame')
