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

    def initui(self,):
        self.title=QLabel(self.book.title)
        self.lid=QLabel(self.book.bid)
        self.lalt=QLabel(self.book.alt)
        self.lauthor=QLabel(self.book.author[0])
        self.price=QLabel(self.book.price)
        self.lsummary=QTextEdit(self.book.summary)
        self.lsummary.setReadOnly(True)

        layout=QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.lid)
        layout.addWidget(self.lalt)
        layout.addWidget(self.lauthor)
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




        
        

