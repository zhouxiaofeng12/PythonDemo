#!/user/bin/python
#-*- coding:UTF-8 -*-
import xlwt
import xlrd
import re
import os

def work_sheet():
        workbook = xlwt.Workbook(encoding='utf8')
        worksheet = workbook.add_sheet('Frame')
        j = 0
        for File_list in dir_list(Local):
            print File_list

        # with open('/Users/zhoufeng/Desktop/帧率.txt','r+') as fp:
        #     i = 0
        #     list_line=len(fp.readlines())
        #     fp.seek(0, 0)
        #     for lint_count in range(list_line):
        #         Line=fp.readline()
        #         strA='GoodsManagementActivity'
        #         if Line.find('ui.activity.GoodsManagementActivity')!=-1:
        #             #用acitivity名称填充第一行
        #             worksheet.write(0,j,strA)
        #             #在获取一行内容
        #             Line = fp.readline()
        #             if Line.find('Execute')!=-1:
        #                 line = fp.readline()
        #                 while 1:
        #                     line = fp.readline()
        #                     if line.strip()!='':
        #                         list=re.split(r'\s',line.strip())
        #                         total = float(list[0]) + float(list[1]) + float(list[2])
        #                         print total
        #                         i = i + 1
        #                         print i
        #                         worksheet.write(i,0,total)
        #
        #                     else:
        #                         break
        #     workbook.save('/Users/zhoufeng/Desktop/数据.xls')


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

Local='/Users/zhoufeng/Desktop/Frame'
work_sheet()




