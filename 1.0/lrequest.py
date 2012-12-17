#!/usr/bin/env python
#-*-coding:utf-8-*-

import sys
import json
from book import *

class lbook_search:
    def __init__(self):
        pass
    def search(self,key_word,atype,start,count):
        print "search key:%s" % key_word
        print "atype :%d " % atype
        if(atype==0):
            stype='q'
        elif(atype==1):
            stype='tag'
        else:
            print "atype  error"
            return []
        fp=open("search.json","r")
        data=fp.read()
        js=json.loads(data)
        jsbooks=js['books']
        books={}
        books['start']=start
        books['total']=js['total']
        books['book_arr']=[]
        books['count']=js['count']-start
        if(books['count']<=0):
            return books
        i=start
        j=start+5
        while i<books['total'] and i<j :
            print jsbooks[i]
            mbook=book()
            mbook.load(jsbooks[i])
            books['book_arr'].append(mbook)
            i+=1
        return books
if __name__=="__main__":
    ss=lbook_search();
    books=ss.search("linux",0,20,5)
    for item in books['book_arr']:
        print item.title
