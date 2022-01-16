# -- coding: utf-8 --
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QTabWidget
from PyQt5.QtGui import QPixmap, QImage
from Load_Demo import Ui_Load_lineEdit


from select import Ui_MainWindow_1
from select import *
from untitled import *

# 登录用户和密码信息
USER_PWD = {
    'la_vie': 'password', 'user': '1234'
}

################################################
#######创建主窗口
################################################
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #super(MainWindow,self).__init__(*args, **kwargs)


################################################
#######登录对话框
################################################
class logindialog(QDialog,Ui_Load_lineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #super(logindialog, self).__init__(*args, **kwargs)
        self.setupUi(self) ##初始化界面内容
        self.setWindowFlags(Qt.FramelessWindowHint)

        ## 绑定按钮事件
        self.pushButton_enter.clicked.connect(self.check_login_func)
        self.pushButton_close.clicked.connect(self.check_close_func)

    # 判断用户密码是否正确
    def check_close_func(self):
     self.close()

    # 判断用户密码是否正确
    def check_login_func(self):
        if USER_PWD.get(self.lineEdit_user.text()) != self.lineEdit_password.text():
            QMessageBox.critical(self, 'Wrong', '用户名或密码错误!')
            return
        self.accept()
        self.lineEdit_user.clear()
        self.lineEdit_password.clear()



################################################
#######主程序
################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = logindialog()
    if  dialog.exec_()==QDialog.Accepted:
     the_window_1 = MyMainWindow_1()
     the_window_1.show()
     #the_window = MyMainWindow()
     #the_window.show()

    sys.exit(app.exec_())


