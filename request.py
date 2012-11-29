#!/usr/bin/python2
#-*-coding:utf-8-*-

import httplib,urllib
import json


class book_search:
    def __init__(self):
        pass
    def search(self,key_word):
        params=urllib.urlencode({'q':key_word,'start':0,'count':1})
        conn=httplib.HTTPConnection("api.douban.com")
        conn.request("GET","/v2/book/search?%s" % params)
        r1=conn.getresponse()
        print r1.status
        data=r1.read()
        js=json.loads(data)
        print js['books'][0]['summary']

if __name__=='__main__':
    ss=book_search()
    ss.search("linux编程")





