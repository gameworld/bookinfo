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
        self.setWindowTitle("search book")
        self.srch_label=QLabel("搜索方式".decode('utf-8'))
        self.srch_cmbbox=QComboBox()
        self.srch_cmbbox.addItem("书名".decode('utf-8'),"name")
        self.srch_cmbbox.addItem("标签".decode('utf-8'),"tag")
        self.edit=QLineEdit("enter book name here")
        self.srch_button=QPushButton("search")
        self.textarea=QTextEdit();

        layout=QVBoxLayout()
        hlayout=QHBoxLayout()
        hlayout.addWidget(self.srch_label)
        hlayout.addWidget(self.srch_cmbbox)
        hlayout.addWidget(self.edit)
        hlayout.addWidget(self.srch_button)
        layout.addLayout(hlayout)
        layout.addWidget(self.textarea)
        self.setLayout(layout)
        self.srch_button.clicked.connect(self.do_search)
        self.edit.setFocus()
        self.resize(700,400)

    def do_search(self):
        key_word=self.edit.text()
        if(key_word==""):
            QMessageBox.information(self,"infomation",\
                    ("请输入关键字".decode('utf-8')),
                    QMessageBox.Ok)
            return 
        ss=book_search();
        print "search key :%s " % self.edit.text()
        print "search type %s" % self.srch_cmbbox.currentIndex()

        books=ss.search(self.edit.text(),self.srch_cmbbox.currentIndex(),0,5)
        book_length=books['total']
        text="find %d books\n" % book_length
        for item in books['book_arr']:
            s_author=""
            for author in item.author[0:-2]:
                s_author+=author+","
            if(len(item.author)>0):
                s_author+=item.author[-1]
            text+="%s\t %s \t %s \t%s\n" % (item.title,s_author,item.publisher,item.price)
            
        self.textarea.setText(text)

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Form()
    form.show();
    sys.exit(app.exec_())


