# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'staff.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from food_management import *
from checkorder import *
from staff_management import  *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1217, 762)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(480, 110, 171, 41))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 340, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 340, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(810, 340, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">食堂员工界面</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "菜品管理"))
        self.pushButton_3.setText(_translate("Form", "订单查询"))
        self.pushButton_4.setText(_translate("Form", "职工管理"))


class MyWidget_2(QtWidgets.QMainWindow,Ui_Form):
    def __init__(self):
        super(MyWidget_2, self).__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.pushB_foodmanage_Clicked)
    def pushB_foodmanage_Clicked(self):
        self.the_window_7 = MyMainWindow_7()
        self.the_window_7.show()

        self.pushButton_3.clicked.connect(self.pushB_checkorder_Clicked)
    def pushB_checkorder_Clicked(self):
        self.the_window_8 = MyMainWindow_8()
        self.the_window_8.show()

        self.pushButton_4.clicked.connect(self.pushB_stuffmanage_Clicked)
    def pushB_stuffmanage_Clicked(self):
        self.the_window_9 = MyMainWindow_9()
        self.the_window_9.show()
