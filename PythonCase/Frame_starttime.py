#!/user/bin/python
#-*- coding:UTF-8 -*-


import os
import xlwt
import xlrd
import re

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

#此方法是用来执行uiautomator的脚本
def Frame(Local,case_list):
     for CaseName in case_list:
        #清除log日志
        os.system('adb logcat -c')

        #先执行uiauto的脚本//需要该脚本执行后,app不被杀掉
        os.system('adb shell am instrument -w -r   -e debug false -e class performance.performancetest.PerformanceTest.Frame#%s performance.performancetest.test/android.support.test.runner.AndroidJUnitRunner'%CaseName)

        #在命令行输入获取的命令
        frame_file = Local+'%s.txt' % CaseName
        os.system('adb shell dumpsys gfxinfo >'+frame_file)

     work_save_excle(Local)




##此方法是来循环Frame文件夹下的所有文件后，打印出来excle表格
def work_save_excle(Local):
    workbook = xlwt.Workbook(encoding='utf8')
    worksheet = workbook.add_sheet('Frame')
    i = 0
    j = 1
    for File_list in dir_list(Local):
        with open(File_list, 'r+') as fp:
            list_line = len(fp.readlines())
            fp.seek(0, 0)
            for lint_count in range(list_line):
                Line = fp.readline()
                #先找到具体数据的标志符号
                if Line.__contains__(".ui.activity"):
                    #正则，生成匹配结果的list
                    pattern = re.findall(".*activity|list.(.*)/android.*", Line.strip())
                    #判断是否该元素是否为需要的元素
                    if pattern[0] == 'MainActivity':
                        print '数据不做处理'
                    else:
                        #在获取目标行后面的一行内容
                        Line = fp.readline()
                        ##判断是否下一行的数据是否为：
                        if Line.strip().find("Execute")!=-1:
                            print("不做处理")
                            # 用acitivity名称填充第一行
                            worksheet.write(0, i, pattern[0])
                            i += 1
                            line = fp.readline()
                            print line

                            #死循环去便利每一行，直到返回空白
                            while 1:
                                line = fp.readline()
                                if line.strip()!='':
                                    list=re.split(r'\s',line.strip())
                                    total = float(list[0]) + float(list[1]) + float(list[2])
                                    print i,j
                                    worksheet.write(j,i-1,total)
                                    j += 1
                                else:
                                    j = 1
                                    break
    workbook.save(os.path.join(Local, 'Frame数据.xls'))



ro_list = ['T01_WeidianNotesListActivity','T02_GoodsListActivity','T03_CRMListActivity','T04_OrderListActivity','T05_OAListActivity']
local_dir='/Users/zhoufeng/Desktop/Frame/'
Frame(local_dir,ro_list)
