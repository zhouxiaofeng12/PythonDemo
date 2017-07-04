# >>> code=97
# >>> s=""
# >>> for i in range(26):
# ...     s+=chr(code+i)
# ...
# >>> print s
# abcdefghijklmnopqrstuvwxyz
#
# >>> code=48
# >>> type(chr(48))
# <type 'str'>
# >>> for i in range(10):
# ...     s+=chr(code+i)
# ...
# >>> print s
# abcdefghijklmnopqrstuvwxyz0123456789
#
#
# >>> code=95
# >>> s=""
# >>> for i in range(13):
# ...     code=code+2
# ...     s+=chr(code)
# ...
# >>> print s
# acegikmoqsuwy
# >>>
#
#
#
# code=ord("z")
# >>> s=""
# >>> for i in range(26):
# ...     s+=chr(code-i)
# ...
# >>> print s
# zyxwvutsrqponmlkjihgfedcba
#
#
# code=ord("z")
# >>> s=""
# >>> for i in range(26):
# ...     s+=chr(code-i)
# ...
# >>> print s
# zyxwvutsrqponmlkjihgfedcba
#
#
#
# >>> s=""
# >>> for i in range(26):
# ...     s+=chr(ord("A")+i)+chr(ord("a")+i)
# ...
# >>> print s
# AaBbCcDdE
#
#
# >>> s=""
# >>> for i in range(13):
# ...     s+=chr(ord("a")+i)+chr(ord("z")-i)
# ...
# >>> print s
# azbycxdwevfugthsirjqkplomn
#
#
#
# >>> print type("s")
# <type 'str'>
# >>> print type(u"s")
# <type 'unicode'>
# >>> "s" is u"s"
# False
#
#
#
# >>> print type('s')
# <type 'str'>
# >>>
# >>> #-*- coding: UTF-8 -*-
# ... s='abccdd'
# >>> print type(s)
# <type 'str'>
# >>>
# >>> u=s.decode()
# >>> print type(u)
# <type 'unicode'>
# >>>
# >>> xx=u.encode()
# >>> print type(xx)
# <type 'str'>