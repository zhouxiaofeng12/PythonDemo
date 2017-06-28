#!/user/bin/python
#-*- coding:UTF-8 -*-

lista=[1,2,4,89,45,57,56,93]
even=[]  #偶数
odd=[]   #奇数
while len(lista)>0:
    number = lista.pop()
    if(number%2==0):
        even.append(number)
    else:
        odd.append(number)

print even
print odd