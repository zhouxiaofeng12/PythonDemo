#encoding=utf-8
i=1
while i<101:
	#r是读,w是写,a是追加写,wb
	f=open('/Users/wangshijie/Desktop/file/file%d'%i,'w')
	i+=1



f=open('/Users/wangshijie/Desktop/file.txt','w')
f.write('中国abc123\n')
f.write('中国abc\n')
f.close()

f=open(u'/Users/wangshijie/Desktop/file.txt','a')
f.write('中国abc123\n')