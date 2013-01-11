#!/usr/bin/env python2
#-*-coding:utf-8-*-

import httplib,urllib
import sys
import json
from book import book
from PySide.QtCore import *
from PySide import * 
from PySide.QtCore import  Signal

#继承一个线程内，在这个线程完成查询操作，避免阻塞主线程（图形线程）
class book_search(QThread):
    # create a new signal on the book data back
    data_back=QtCore.Signal(object)
    def __init__(self,parent=None):
        super(book_search,self).__init__(parent)
        self.key_word='linux'
        self.atype=0
        self.lstart=0
        self.count=5



    def setSearch_data(self,key_word,attype,start,count):
        self.key_word=key_word
        self.attype=attype
        self.lstart=start
        self.count=count
    def run(self):
        books=self.search(self.key_word,self.atype,self.lstart,self.count);
        self.data_back.emit(books)
    def search(self,key_word,atype,start,count):
        print "search key :%s " % key_word
        print "atype :%d:" % atype
        if(atype==0):
            stype='q'
        elif(atype==1):
            stype='tag'
        else:
            print "atype error"
            return  []
        params=urllib.urlencode({stype:key_word.encode('utf-8'),'start':start,'count':count})
        conn=httplib.HTTPConnection("api.douban.com")
        print params
        conn.request("GET","/v2/book/search?%s" % params)
        r1=conn.getresponse()
        print r1.status
        data=r1.read()
        #f=open("data.txt","w")
        #f.write(data)
        js=json.loads(data)
        jsbooks=js['books']
        #book array
        books={}
        books['count']=js['count']
        books['start']=js['start']
        books['total']=js['total']
        books['book_arr']=[];
        for item in jsbooks:
            mbook=book()
            mbook.load(item)
            books['book_arr'].append(mbook)
        return books
           # print "###########################################\n\n\n"


if __name__=='__main__':
    argc=len(sys.argv)
    if(argc<2):
        print "usage %s  keyworkd start count " % sys.argv[0]
        exit(0)
    start=0;
    count=5;
    if(argc==3):
        start=sys.argv[2]
    if(argc==4):
        count=sys.argv[3]
    ss=book_search()
    ss.search(sys.argv[1],start,count)





