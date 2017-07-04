#!/user/bin/python
#-*- coding:UTF-8 -*-

f=open('/Users/wangshijie/Desktop/weidianTEST.txt','w+')
f.write('我是周凤')
f.seek(0.0)
xx=f.read()
xx.encode
print type(xx)

#encoding=utf-8

s=u"自己跑没搞过IP!!!!!!!!!!1"
with open("e:\\a.txt","w") as fp:
    fp.write(s.encode("gbk"))
    fp.write(s.encode("utf-8"))

    # -*- coding: UTF-8 -*-
    fp1 = open('e:\\testfile.txt', 'r')  # 手工创建文件为ANSI编码保存（gbk）
    info1 = fp1.read()
    # 已知是 GBK 编码，解码成 Unicode、
    tmp = info1.decode('GBK')
    fp1.close()

    fp2 = open('e:\\testfile.txt', 'w')
    # 编码成 UTF-8 编码的 str
    info2 = tmp.encode('UTF-8')
    fp2.write(info2)  # 写入utf8字符，并进行保存
    fp2.close()  # 文件会变为utf-8编码保存
