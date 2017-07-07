#!/user/bin/python
#-*- coding:UTF-8 -*-

# try:
#     fh=open('/Users/zhoufeng/Desktop/java.txt','r')
#     fh.write('test')
# except IOError:   #输入/输出操作失败
#     print 'Error：没有找到文件或读取文件失败'
# else:
#     print '内容写入文件成功'
#     fh.close()

# try:
#     1 / 0
# except Exception as e:
#     '''异常的父类，可以捕获所有的异常'''
#     print "0不能被除"
# else:
#     '''保护不抛出异常的代码'''
#     print "没有异常"
# finally:
#     print "最后总是要执行我"


# try:
#     fh=open('/Users/zhoufeng/Desktop/javatest.txt','r')  #执行的
# except IOError,e:
#     print 'is error message',e


# def safe_float(obj):
#     try:
#         retval=float(obj)
#         return retval
#     except ValueError:
#         retval= 'could not convert non-number to float'
#         return  retval
#     except TypeError:
#         retval='could not convert non-number to typeerror'
#         return retval
#
# safe_float(['dadfafadsfdaf'])
# safe_float(223.23)


def safe_float(obj):
    try:
        retval = float(obj)
        print retval
    except ValueError:
        retval = 'could not convert non-number to float'
        print retval
    except TypeError:
        retval = 'object type cannot be converted to float'
        print retval

safe_float(['dadfafadsfdaf'])
safe_float(223.23)
safe_float(23232323323223)
safe_float(200L)


def safe_float(obj):
    try:
        retval = float(obj)
        print retval
    except (ValueError,TypeError):
        retval = 'could not convert non-number to float'
        print retval
safe_float(121231313131313131)