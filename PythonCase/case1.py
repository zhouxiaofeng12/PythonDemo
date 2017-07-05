#!/user/bin/python
#-*- coding:UTF-8 -*-

#输入1-127的ascii码并输出对应字符
code=0
s=''
for i in range(128):
    s+=chr(code+i)
print s

#输入ASII码中的从A到Z
s=''
code=ord('A')
for i in range(26):
    s+=chr(code+i)
print s

#输入ASII码中的从Z到A
s=''
code=ord('Z')
for i in range(26):
    s+=chr(code-i)
print s


#输入ASII码中的从ZzYx到Aa
s=''
code=ord('Z')
code2=ord('z')
for i in range(26):
    s+=chr(code-i)+chr(code2-i)
print s

#输出ASII码中的Za~Az
s=''
code=ord('Z')
code2=ord('a')
for i in range(26):
    s+=chr(code-i)+chr(code2+i)
print s

