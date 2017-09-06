#!/user/bin/python
#-*- coding:UTF-8 -*-


import os
import xlwt
import xlrd
import re


# 处理帧率
# def Activity_Frame(Local):
#     case_list = ['WeidianNotesListActivity', 'OrderListActivity', 'GoodsListActivity']
#
#     # globals(path)
#     workbook = xlwt.Workbook(encoding='utf8')
#     worksheet = workbook.add_sheet('Frame')
#     i = 0
#     fp = open(Local, 'r')
#     Tag = False
#     Break = True
#     for line in fp:
#         if Break:
#             if Tag == True:
#                 if line.__contains__("Execute"):
#                     print("不做处理")
#                 elif line.__contains__("hierarchy"):
#                     Break = False
#                 else:
#                     if line.strip() == "":
#                         print("空行不处理")
#                         Tag = False
#                     else:
#                         name = re.split("\\s+", line.strip())
#                         total = float(name[0]) + float(name[1]) + float(name[2])
#                         print(line)
#                         print(name[0], name[1], name[2])
#                         print(total)
#                         fps = round(1000 / total)
#                         worksheet.write(j, i - 1, label=fps)
#                         j += 1
#             else:
#                 if line.__contains__(".ui.activity"):
#                     print("处理后续数据")
#                     # com.koudai.weishop/com.koudai.weishop.goods.ui.activity.GoodsManagementActivity/android.view.ViewRootImpl@4340e0b0
#                     pattern = re.findall(".*activity.(.*)/android.*", line.strip())
#                     if pattern[0] == "MainActivity":
#                         print("不处理main")
#                     else:
#                         worksheet.write(0, i, pattern[0])
#                         print(pattern[0])
#                         i += 1
#                         j = 1
#                         Tag = True
#
#                 elif line.__contains__("hierarchy"):
#                     Break = False
#
#         else:
#             break
#
#     workbook.save(path + '数据'+i+'.xls')

def file_get_Detail(address):
    file = os.listdir(address)
    return file

def Frame(path,case_list):
     for CaseName in case_list:
        #清除log日志
        os.system('adb logcat -c')

        #先执行uiauto的脚本//需要该脚本执行后,app不被杀掉
        os.system('adb shell am instrument -w -r   -e debug false -e class performance.performancetest.PerformanceTest.Frame#%s performance.performancetest.test/android.support.test.runner.AndroidJUnitRunner'%CaseName)

        #在命令行输入获取的命令
        frame_file = path+'%s.txt' % CaseName
        os.system('adb shell dumpsys gfxinfo >'+frame_file)


ro_list = ['T01_WeidianNotesListActivity','T02_GoodsListActivity','T03_CRMListActivity','T04_OrderListActivity','T05_OAListActivity']
local_dir='/Users/zhoufeng/Desktop/Frame/'
Frame(local_dir,ro_list)

# 处理脚本
workbook = xlwt.Workbook(encoding='utf8')
worksheet = workbook.add_sheet('Frame')
i = 0
fp = open(frame_file, 'r')
Tag = False
Break = True
for line in fp:
    if Break:
        if Tag == True:
            if line.__contains__("Execute"):
                print("不做处理")
            elif line.__contains__("hierarchy"):
                Break = False
            else:
                if line.strip() == "":
                    print("空行不处理")
                    Tag = False
                else:
                    name = re.split("\\s+", line.strip())
                    total = float(name[0]) + float(name[1]) + float(name[2])
                    print(line)
                    print(name[0], name[1], name[2])
                    print(total)
                    fps = round(1000 / total)
                    worksheet.write(j, i - 1, label=fps)
                    j += 1
        else:
            if line.__contains__(".ui.activity"):
                print("处理后续数据")
                # com.koudai.weishop/com.koudai.weishop.goods.ui.activity.GoodsManagementActivity/android.view.ViewRootImpl@4340e0b0
                pattern = re.findall(".*activity.(.*)/android.*", line.strip())
                if pattern[0] == "MainActivity":
                    print("不处理main")
                else:
                    worksheet.write(0, i, pattern[0])
                    print(pattern[0])
                    i += 1
                    j = 1
                    Tag = True

            elif line.__contains__("hierarchy"):
                Break = False

    else:
        break

workbook.save(path + '数据' + CaseName + '.xls')
