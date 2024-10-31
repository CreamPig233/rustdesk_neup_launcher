import sys, requests, time, threading

import window1, window2, window3, window4

from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QUrl, QObject, pyqtSignal
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import QThread, pyqtSignal

def SwitchTo_TermsWindow():
    TermsWindow_wd = window2.Ui_TermsWindow()
    TermsWindow_wd.setupUi(mainWindow)
    TermsWindow_wd.TermsWindow_NextBtn.clicked.connect(SwitchTo_NetworkWindow)

def SwitchTo_NetworkWindow():
    NetworkWindow_wd = window3.Ui_NetworkWindow()
    NetworkWindow_wd.setupUi(mainWindow)
    NetworkWindow_wd.NetworkWindow_CustomBtn.clicked.connect(SwitchTo_ServerWindow)
    #另开线程，先加载窗口，再检测网络连接
    t = threading.Thread(target=NetworkWindow_wd.NetworkCheck_NetworkWindow)
    t.start()

def SwitchTo_ServerWindow():
    ServerWindow_wd = window4.Ui_ServerWindow()
    ServerWindow_wd.setupUi(mainWindow)
    ServerWindow_wd.ServerWindow_NextBtn.clicked.connect(SwitchTo_NetworkWindow)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWindow = QMainWindow()


    WelcomeWindow_wd = window1.Ui_WelcomeWindow()
    WelcomeWindow_wd.setupUi(mainWindow)
    WelcomeWindow_wd.WelcomeWindow_NextBtn.clicked.connect(SwitchTo_TermsWindow)



    mainWindow.show()

    sys.exit(app.exec_())
