#!/usr/bin/env python2
#-*-coding:utf-8-*-

# the book info class

import json

class book:
    def __init__(self):
        self.bid="id"
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
        self.author_intro=""
        self.summary=""
    def load(self,jsondata):
        self.bid=jsondata['id']
        self.isbn10=jsondata['isbn10']
        self.isbn13=jsondata['isbn13']
        self.title=jsondata['title']
        self.origin_title=jsondata['origin_title']
        self.subtitle=jsondata['subtitle']
        self.url=jsondata['url']
        self.alt=jsondata['alt']
        self.image=jsondata['image']
        self.images=jsondata['images']
        self.author=jsondata['author']
        self.translator=jsondata['translator']
        self.publisher=jsondata['publisher']
        self.pubdate=jsondata['pubdate']
#        self.rating=jsondata['rating']
        self.tags=jsondata['tags']
        self.binding=jsondata['binding']
        self.price=jsondata['price']
        self.pages=jsondata['pages']
        self.author_intro=jsondata['author_intro']
        self.summary=jsondata['summary']

    def showinfo(self):
        print "id:",self.bid
        print "isbn10:",self.isbn10
        print "isbn13:",self.isbn13
        print "title:",self.title
        print "origin_title:",self.origin_title
        print "alt_title:",self.alt_title
        print "subtitle:",self.subtitle
        print "url:",self.url
        print "alt:",self.alt
        print "image:",self.image

        #print "images:",self.images
        print "images:"
        print "\tsmall",self.images['small']
        print "\tmedium",self.images['medium']
        print "\tlarge",self.images['large']


        print "author:",
        for item in self.author:
            print "\t",item

        #print "translator:",self.translator
        print "translator;"
        for item in self.translator:
            print "\t",item

        print "publisher:",self.publisher
        print "pubdate",self.pubdate
        print "rating:",self.rating

        #print "tags:",self.tags
        for item in self.tags:
            print item['count'],item['name']



        print "binding:",self.binding
        print "price:",self.price
        print "pages",self.pages
        print "author_intro:",self.author_intro
        print "summary\t",self.summary

        

        

if __name__=='__main__':
    mbook=book()
    f=open("data.txt","r")
    data=f.read()
    booksjson=json.loads(data)
    mbook.load(booksjson['books'][0])

    mbook.showinfo()







