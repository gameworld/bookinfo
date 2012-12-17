#!/usr/bin/env python2
#-*-coding:utf-8-*-

from PySide.QtGui import *
from PySide.QtCore import *

class detialDialog(QDialog):
    def __init__(self,parent=None):
        super(detialDialog,self).__init__(parent)
        self.book=bookitem
        self.initui()

    def initui(self):
        self.title=QLabel(self.book.title)
        self.lid=QLabel(self.book.bid)
        self.lalt=QLabel(self.book.alt)
        self.lauthor=QLabel(self.book.author)
        self.price=QLabel(self.book.price)
        self.lsummary=QLabel(self.book.summary)

        layout=QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.lid)
        layout.addWidget(self.lalt)
        layout.addWidget(self.lauthor)
        layout.addWidget(self.lsummary)
        self.setLayout(layout)




        
        

