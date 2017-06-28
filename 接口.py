#encoding=utf-8
#encoding=utf-8
import requests
import json
import os
import hashlib

m5 = hashlib.md5()

m5.update('lily')
pwd = m5.hexdigest()
print pwd

print "update post------"
data = json.dumps({'userid': 1, "token": "a1c0738a6cf054606b055a419c3390f3", 'articleId': 2, 'title': 'about port', 'content': 'code code'}) #
r = requests.put('http://localhost:8080/update/', data = data)
print r.status_code
print r.text
print type(r.json())
print str(r.json())
