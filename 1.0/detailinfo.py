#!/usr/bin/env python2
#-*-coding:utf-8-*-

import sys
from PySide.QtGui import *
from PySide.QtCore import *
from book import *

class detailDialog(QDialog):
    def __init__(self,parent=None):
        super(detailDialog,self).__init__(parent)
        self.book=book()

    def initui(self):
        self.title=QLabel(self.book.title)
        auth="作者:".decode('utf-8');
        for item in self.book.author:
            auth+=" "+item
        self.lauthor=QLabel(auth)
        self.publisher=QLabel("出版社:".decode('utf-8')+self.book.publisher)
        self.publishdate=QLabel("出版日期".decode('utf-8')+self.book.pubdate)
        self.price=QLabel("定价:".decode('utf-8')+self.book.price)
        self.lalt=QLabel("<a href=\""+self.book.alt+"\""+"\\>豆瓣链接".decode('utf-8'))
        self.lalt.setOpenExternalLinks(True)
        self.lsummary=QTextEdit(self.book.summary)
        self.lsummary.setReadOnly(True)

        layout=QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.lauthor)
        layout.addWidget(self.publisher)
        layout.addWidget(self.price)
        layout.addWidget(self.lalt)
        layout.addWidget(self.lsummary)
        self.setLayout(layout)
    def setBook(self,bookitem):
        self.book=bookitem
        self.initui()
if __name__=='__main__':
    App=QApplication(sys.argv)
    dlg=detailDialog()
    dlg.show()
    sys.exit(App.exec_())




        
        

