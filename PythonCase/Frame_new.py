#!/user/bin/python
#-*- coding:UTF-8 -*-
import xlwt
import xlrd
import re
import os


def dir_list(Local):
    file_list=[]
    os.chdir(Local)

    for Filename in os.listdir('.'):
        if Filename=='.DS_Store':
            print '系统文件不做处理'
        else:
            if os.path.splitext(Filename)[1]=='.txt':
                file_list.append(Filename)
    return file_list



def work_save_excle(Local):
    workbook = xlwt.Workbook(encoding='utf8')
    worksheet = workbook.add_sheet('Frame')
    i = 0
    j = 1
    for File_list in dir_list(Local):
        print File_list
        with open(File_list, 'r+') as fp:
            list_line = len(fp.readlines())
            fp.seek(0, 0)
            for lint_count in range(list_line):
                Line = fp.readline()
                #先找到具体数据的标志符号
                if Line.__contains__(".ui.activity"):
                    #正则，生成匹配结果的list
                    pattern = re.findall("Activity/android", Line.strip())
                    print pattern
                    #判断是否该元素是否为需要的元素
    #                 if pattern[0] == 'MainActivity':
    #                     print '数据不做处理'
    #                 else:
    #                     #在获取目标行后面的一行内容
    #                     Line = fp.readline()
    #                     ##判断是否下一行的数据是否为：
    #                     if Line.strip().find("Execute")!=-1:
    #                         print("不做处理")
    #                         # 用acitivity名称填充第一行
    #                         worksheet.write(0, i, pattern[0])
    #                         i += 1
    #                         line = fp.readline()
    #                         print line
    #                         while 1:
    #                             line = fp.readline()
    #                             if line.strip()!='':
    #                                 list=re.split(r'\s',line.strip())
    #                                 total = float(list[0]) + float(list[1]) + float(list[2])
    #                                 worksheet.write(j,i-1,total)
    #                                 j += 1
    #                             else:
    #                                 j = 1
    #                                 break
    #
    # workbook.save(os.path.join(Local, '数据.xls'))


LocalA='/Users/zhoufeng/Desktop/Frame'
work_save_excle(LocalA)




