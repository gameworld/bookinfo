#!/usr/bin/env python2
#-*-coding:utf-8-*-

# the book info class

import json

class book:
    def __init__(self):
        self.id="id"
        self.isbn10="isbn10"
        self.isbn13="isbn13"
        self.title="title"
        self.origin_title="origin_title"
        self.alt_title="alt_title"
        self.subtitle="subtitle"
        self.url="http://api.douban.com"
        self.alt="http://api.douban.com"
        self.image=""
        self.images=[]
        self.author=[];
        self.translator=[];
        self.publisher="publisher"
        self.pubdate="pubdate"
        self.rating=""
        self.tags=""
        self.binding=""
        self.price="1.00"
        self.pages="100"
        self.author_intor=""
        self.summary=""
    def loadjson(self,jsondata):
        encodejson=json.dumps(jsondata)
        self.id=encodejson['id']
        self.isbn10=encodejson['isbn10']
        self.isbn13=encodejson['isbn13']
        self.title=encodejson['title']
        self.origin_title=encodejson['origin_title']
        self.subtitle=encodejson['subtitle']
    def showinfo(self):
        print self.id
        print self.isbn10
        print self.isbn13
        print self.title
        print self.origin_title
        print self.alt_title
        print self.subtitle
        print self.url
        print self.alt
        print self.image
        print self.images
        print self.author
        print self.translator
        print self.publisher
        print self.pubdate
        print self.rating
        print self.tags
        print self.binding
        print self.price
        print self.pages
        print self.author_intor
        print self.summary

        

        

if __name__=='__main__':
    mbook=book()
    f=open("data.txt","r")
    data=f.read()
    mbook.loadjson(data)

    mbook.showinfo()







