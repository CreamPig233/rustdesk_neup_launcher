import subprocess
import sys
import threading


import log_print


from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

import generate_exe_file
import networkcheck
import window1
import window2
import window3
import window4
import window5


def SwitchTo_TermsWindow():
    log_print.outlog(1, "切换窗口2")
    TermsWindow_wd = window2.Ui_TermsWindow()
    TermsWindow_wd.setupUi(mainWindow)
    TermsWindow_wd.TermsWindow_NextBtn.clicked.connect(SwitchTo_NetworkWindow)


def SwitchTo_NetworkWindow():
    log_print.outlog(1, "切换窗口3")
    NetworkWindow_wd = window3.Ui_NetworkWindow()
    NetworkWindow_wd.setupUi(mainWindow)
    NetworkWindow_wd.NetworkWindow_CustomBtn.clicked.connect(SwitchTo_ServerWindow)
    NetworkWindow_wd.NetworkWindow_NextBtn.clicked.connect(SwitchTo_ReadyWindow)
    # 另开线程，先加载窗口，再检测网络连接
    log_print.outlog(1, "开始网络检测线程，调用函数")
    t = threading.Thread(target=NetworkWindow_wd.NetworkCheck_NetworkWindow)
    t.start()


def ChangeServer_and_SwitchToNetworkWindow(ServerWindow_wd):
    log_print.outlog(1, "切换服务器")
    # 修改服务器ip
    new_ip = ServerWindow_wd.CustomServer.text()
    if new_ip != '':
        networkcheck.serverip = new_ip
        log_print.outlog(1, "新服务器ip:" + new_ip)

    # 修改是否使用官方服务器
    if (ServerWindow_wd.UseOfficialServer.isChecked()):
        networkcheck.serverip = 'rs-ny.rustdesk.com'
        generate_exe_file.use_official_server = True
        log_print.outlog(1, "使用官方服务器")

    # 修改key
    new_key = ServerWindow_wd.CustomKey.text()
    if new_key != '':
        generate_exe_file.key = new_key
        log_print.outlog(1, "新key:" + new_key)

    # 切换窗口
    SwitchTo_NetworkWindow()


def SwitchTo_ServerWindow():
    log_print.outlog(1, "切换窗口4")
    ServerWindow_wd = window4.Ui_ServerWindow()
    ServerWindow_wd.setupUi(mainWindow)
    ServerWindow_wd.ServerWindow_NextBtn.clicked.connect(
        lambda: ChangeServer_and_SwitchToNetworkWindow(ServerWindow_wd))


def SwitchTo_ReadyWindow():
    log_print.outlog(1, "切换窗口5")
    try:
        generate_exe_file.generate_exe_file()
    except Exception as e:
        log_print.outlog(3, "生成exe文件失败，异常信息：" + str(e))


    log_print.outlog(1, "切换窗口5")
    ReadyWindow_wd = window5.Ui_ReadyWindow()
    ReadyWindow_wd.setupUi(mainWindow)
    ReadyWindow_wd.ReadyWindow_NextBtn.clicked.connect(start_rustdesk)


def start_rustdesk():
    log_print.outlog(1, "准备启动rustdesk,路径:"+generate_exe_file.get_rustdesk_path())
    #从generate_exe_file中获取生成的exe文件路径，启动rustdesk，结束本程序
    try:
        log_print.outlog(1, "启动rustdesk")
        subprocess.Popen(generate_exe_file.get_rustdesk_path())
    except Exception as e:
        log_print.outlog(2, "启动rustdesk失败，异常信息：" + str(e))
    log_print.outlog(1, "启动rustdesk结束，退出程序")
    log_print.outlog(2, "主程序运行结束")

    sys.exit()


if __name__ == '__main__':
    log_print.outlog(1, "主程序运行开始")
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    dpi = QApplication.primaryScreen().logicalDotsPerInch()
    log_print.outlog(1, "dpi:" + str(dpi))
    WelcomeWindow_wd = window1.Ui_WelcomeWindow()
    WelcomeWindow_wd.setupUi(mainWindow)
    WelcomeWindow_wd.WelcomeWindow_NextBtn.clicked.connect(SwitchTo_TermsWindow)
    log_print.outlog(1, "创建窗口1")

    mainWindow.show()

    sys.exit(app.exec_())
