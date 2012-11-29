#!/usr/bin/python2
#-*-coding:utf-8-*-

import sys
from PySide.QtGui import *
from PySide.QtCore import *

class Form(QDialog):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)
        self.setWindowTitle("search book")
        self.edit=QLineEdit("enter book name here")
        self.button=QPushButton("search")
        self.textarea=QTextEdit();

        layout=QVBoxLayout()
        hlayout=QHBoxLayout()
        hlayout.addWidget(self.edit)
        hlayout.addWidget(self.button)
        layout.addLayout(hlayout)
        layout.addWidget(self.textarea)
        self.setLayout(layout)
        self.button.clicked.connect(self.do_search)

    def do_search(self):
        self.textarea.setText(self.edit.text())

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Form()
    form.show();
    sys.exit(app.exec_())


