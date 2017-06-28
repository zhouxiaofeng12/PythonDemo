#!/user/bin/python
#-*- coding:UTF-8 -*-
s = "abaaaceadgescdwesjgdk"

a_num,b_num,z_num,c_num,d_num,g_num,e_num,s_num=0

for i in s:
    if i=='a':
        a_num+=1
    elif i=='b':
        b_num+=1
    elif i=='z':
        z_num+=1
    elif i=='c':
        c_num=1
    elif i=='d':
        d_num+=1
    elif i =='g':
        g_num += 1
    elif i =='e':
        e_num += 1
    elif i =='s':
        s_num += 1

print "a_num=",a_num
print "b_num=",b_num
print "z_num=",z_num
print "c_num=",c_num
print "d_num=",d_num
print "g_num=",g_num
print "e_num=",e_num
print "s_num=",s_num






