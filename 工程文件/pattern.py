# -*- coding: utf-8 -*-


# Form implementation generated from reading ui file 'imgreconition.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import json
import sys

import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import urllib, urllib.request
import ssl

import base64


# 另外获取token值 图像识别
P_KEY = 'i3nnnhZ5Phh08CLFGIechvHD'
P_SECRET = '5NiQ4hEAlddhfVtQnEOCYG887d1ORn3F'


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(597, 471)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 50, 171, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 100, 271, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 271, 261))
        # self.label_3.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_3.setStyleSheet("border-width: 1px;border-style: solid;boder-color: rgb(0,0,0);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(330, 50, 241, 321))
        # self.label_4.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.label_4.setStyleSheet("border-width: 1px;border-style: solid;boder-color: rgb(0,0,0);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 380, 241, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "菜品识别"))
        self.label.setText(_translate("Form", "选择识别类型:"))
        self.comboBox.setItemText(1, _translate("Form", "菜品"))
        self.label_2.setText(_translate("Form", "选择要识别的图片:"))
        self.pushButton.setText(_translate("Form", "选择"))
        self.pushButton_2.setText(_translate("Form", "复制导粘贴板"))
        # 为选择按钮添加点击事件
        self.pushButton.clicked.connect(self.openfile)
        # 为复制按钮添加点击事件
        self.pushButton_2.clicked.connect(self.copyText)

class MyWidget_11(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(MyWidget_11, self).__init__()
        self.setupUi(self)

    def copyText(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.label_4.text())
        print(1)
    # 打开文件函数
    def openfile(self):
        self.download_path = QFileDialog.getOpenFileName(self.horizontalLayoutWidget_2, "选择要识别的图片", "/",
                                                         "Image File(*.jpg *.png)")
        if not self.download_path[0].strip():
            pass
        else:
            #print(self.download_path[0])
            # 把图片路径显示
            self.lineEdit.setText(self.download_path[0])
            # 显示选择的图片 自动解析图片
            pixmap = QPixmap(self.download_path[0])

            # 处理图片  规定大小
            scarePixmap = pixmap.scaled(QSize(271, 261), aspectRatioMode=Qt.KeepAspectRatio)

            # 把图片设置到控件里
            self.label_3.setPixmap(scarePixmap)

            # 通过百度ai接口来识别特定类别的图片
            self.typeTp()



    # 类别 识别
    def typeTp(self):
        self.get_plant(self.img_get_token())



    # 获取token  图像识别
    def img_get_token(self):
        # client_id 为官网获取的AK， client_secret 为官网获取的SK
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+P_KEY+'&client_secret='+P_SECRET
        #print(host)
        response = requests.get(host)
        if response:
            print(response.json())
            self.access_token = response.json()['access_token']
            return self.access_token


    # 植物识别函数
    def get_plant(self, access_token):
        '''
        植物识别
        '''
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/dish"
        # 二进制方式打开图片文件
        f = open(self.download_path[0], 'rb')

        img = base64.b64encode(f.read())


        params = {"image": img}

        request_url = request_url + "?access_token=" + access_token


        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)

        if response:
            # 解析返回的数据
            rs = response.json()
            print(rs)
            # 读取数据
            strover = '识别结果：\n'
            try:
                #i = 1
                for dish in rs['result']:
                    strover += '食物卡路里：{}. \n是否含卡路里：{}. \n食物名称：{}.  \n置信度：  {:.6}\n'.format(dish['calorie'],dish['has_calorie'], dish['name'], dish['probability'])
                    break
                    #i += 1
            except Exception:
                strover += '无法识别'
            # 把结果显示到控件
            self.label_4.setText(strover)



