#!/usr/bin/env python2
#-*-coding:utf-8-*-

import sys
from PySide.QtGui import *
from PySide.QtCore import *
from request import *
from book import *

class Form(QDialog):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)
        #初始化主窗口
        self.initui()



        #保存当前每页显示的条数
        self.per_page_show=5
        #保存搜索结果的图书
        self.books=""
        #当前页数开始的索引
        self.cur_start=0
        #当前的页数
        self.cur_page=0
        #搜索到的总的图书数
        self.total_books=0

    #执行搜索操作，关键字,开始索引,期望的条数
    def do_search(self,key_word,start=0,count=5):
        if(key_word==""):
            QMessageBox.information(self,"infomation",\
                    ("请输入关键字".decode('utf-8')),
                    QMessageBox.Ok)
            return 
        ss=book_search();
        print "search key :%s " % self.edit.text()
        print "search type %s" % self.srch_cmbbox.currentIndex()

        books=ss.search(self.edit.text(),self.srch_cmbbox.currentIndex(),start,count)
        self.total_books=books['total']
        text="find %d books\n" % self.total_books 
        text+="current page :%d \n"  % self.cur_page
        for item in books['book_arr']:
            s_author=""
            for author in item.author[0:-2]:
                s_author+=author+","
            if(len(item.author)>0):
                s_author+=item.author[-1]
            text+="%s\t %s \t %s \t%s\n" % (item.title,s_author,item.publisher,item.price)
            
        self.textarea.setText(text)
    def on_search_btn_click(self):
            self.cur_page=1
            self.cur_start=0
            self.do_search(self.edit.text(),self.cur_start,self.per_page_show)
    def on_next_btn_click(self):
            self.cur_page+=1
            self.cur_start=(self.cur_page-1)*self.per_page_show
            if(self.cur_start<self.total_books):
                self.do_search(self.edit.text(),self.cur_start,self.per_page_show)
            if(self.cur_start+self.per_page_show>self.total_books-1):
                self.next_btn.setEnabled(False)
            if(self.cur_page>1):
                self.pre_btn.setEnabled(True)
    
    def on_pre_btn_click(self):
            if(self.cur_page>1):
                self.cur_page-=1
                self.cur_start=(self.cur_page-1)*self.per_page_show
                self.do_search(self.edit.text(),self.cur_start,self.per_page_show)
                if(self.cur_page==1):
                    self.pre_btn.setEnabled(False)
                if(self.cur_start+self.per_page_show<=self.total_books-1):
                    self.next_btn.setEnabled(True)

            

    def initui(self):
            self.setWindowTitle("search book")
            self.srch_label=QLabel("搜索方式".decode('utf-8'))
            self.srch_cmbbox=QComboBox()
            self.srch_cmbbox.addItem("书名".decode('utf-8'),"name")
            self.srch_cmbbox.addItem("标签".decode('utf-8'),"tag")
            self.edit=QLineEdit("enter book name here")
            self.srch_button=QPushButton("search")
            self.textarea=QTextEdit();
            self.next_btn=QPushButton("next")
            self.pre_btn=QPushButton("previous")

            layout=QVBoxLayout()
            hlayout=QHBoxLayout()
            btnlayout=QHBoxLayout()
            btnlayout.addWidget(self.next_btn)
            btnlayout.addWidget(self.pre_btn)

            hlayout.addWidget(self.srch_label)
            hlayout.addWidget(self.srch_cmbbox)
            hlayout.addWidget(self.edit)
            hlayout.addWidget(self.srch_button)
            layout.addLayout(hlayout)
            layout.addWidget(self.textarea)
            layout.addLayout(btnlayout)
            self.setLayout(layout)
            self.srch_button.clicked.connect(self.on_search_btn_click)
            self.next_btn.clicked.connect(self.on_next_btn_click)
            self.pre_btn.clicked.connect(self.on_pre_btn_click)
            self.edit.setFocus()
            self.resize(700,400)



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Form()
    form.show();
    sys.exit(app.exec_())


