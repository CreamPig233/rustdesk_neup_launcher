import sys, requests, time, threading, os, subprocess

import networkcheck
import window1, window2, window3, window4, window5
import generate_exe_file

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
    NetworkWindow_wd.NetworkWindow_NextBtn.clicked.connect(SwitchTo_ReadyWindow)
    #另开线程，先加载窗口，再检测网络连接
    t = threading.Thread(target=NetworkWindow_wd.NetworkCheck_NetworkWindow)
    t.start()

def ChangeServer_and_SwitchToNetworkWindow(ServerWindow_wd):

    #修改服务器ip
    new_ip = ServerWindow_wd.CustomServer.text()
    if new_ip != '':
        networkcheck.serverip = new_ip

    #修改是否使用官方服务器
    if(ServerWindow_wd.UseOfficialServer.isChecked()):
        networkcheck.serverip = 'rs-ny.rustdesk.com'
        generate_exe_file.use_official_server = True

    #修改key
    new_key = ServerWindow_wd.CustomKey.text()
    if new_key != '':
        generate_exe_file.key = new_key

    #切换窗口
    SwitchTo_NetworkWindow()

def SwitchTo_ServerWindow():
    ServerWindow_wd = window4.Ui_ServerWindow()
    ServerWindow_wd.setupUi(mainWindow)
    ServerWindow_wd.ServerWindow_NextBtn.clicked.connect(lambda: ChangeServer_and_SwitchToNetworkWindow(ServerWindow_wd))

def SwitchTo_ReadyWindow():
    try:
        generate_exe_file.generate_exe_file()
    except Exception as e:
        print(e)
    ReadyWindow_wd = window5.Ui_ReadyWindow()
    ReadyWindow_wd.setupUi(mainWindow)
    ReadyWindow_wd.ReadyWindow_NextBtn.clicked.connect(start_rustdesk)

def start_rustdesk():
    print(generate_exe_file.get_rustdesk_path())
    subprocess.Popen(generate_exe_file.get_rustdesk_path())
    #subprocess.Popen('notepad.exe')
    sys.exit()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWindow = QMainWindow()


    WelcomeWindow_wd = window1.Ui_WelcomeWindow()
    WelcomeWindow_wd.setupUi(mainWindow)
    WelcomeWindow_wd.WelcomeWindow_NextBtn.clicked.connect(SwitchTo_TermsWindow)



    mainWindow.show()

    sys.exit(app.exec_())
