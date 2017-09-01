#!/user/bin/python
#-*- coding:UTF-8 -*-
# import os
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
#
#




#17、文件访问,􏰀示输入数字 N 和文件 F, 然后显示文件 F 的前 N 行.
