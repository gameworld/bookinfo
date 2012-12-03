#!/usr/bin/env python2
#-*-coding:utf-8-*-

from PySide.QtGui import *
from PySide.QtCore import *

class Form(QDialog):
    def __init__(self,parent=None,bookitem):
        super(Form,self).__init__(parent)

