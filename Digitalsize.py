#!/user/bin/python
#-*- coding:UTF-8 -*-



namelist=[1,23,23425,23245,['stirng','helo','xx',[1,2,3]]]
for each_values in namelist:
    if isinstance(each_values,list):
    	for west in each_values:
    		print west
    else:
    	print each_values