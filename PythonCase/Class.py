#/user/bin/python
#-*- coding:UTF-8 -*-

#self 代表类的实例,self相当于这个类实例化的出来的对象
class Person:
    '所有员工的基类'
    empCount = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Person.empCount += 1

    def displayCount(self):
        print 'Total Person %d' % Person.empCount

    def displayEmployee(self):
        print "Name:", self.name,  ", Salary:", self.salary

p=Person('zho',223)
p.displayCount()
p.displayEmployee()



