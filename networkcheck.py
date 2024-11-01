import socket

import requests
import winreg, log_print

serverip='172.20.65.19'     #发布时应修改默认服务器ip

def NetworkCheck(self):

    isConnectCampus=False
    isSupportIPv4=False
    isSupportIPv6=False
    isConnectServer=False

    isloginIPGW=False
    idProxyEnabled=False


    #self.isConnectNetwork_label.setText("检测中")
    #self.isConnectNetwork_label.setStyleSheet("color:black")
    self.isConnectCampus_label.setText("检测中")
    self.isConnectCampus_label.setStyleSheet("color:black")
    self.isSupportIPv4_label.setText("检测中")
    self.isSupportIPv4_label.setStyleSheet("color:black")
    self.isSupportIPv6_label.setText("检测中")
    self.isSupportIPv6_label.setStyleSheet("color:black")
    self.isConnectServer_label.setText("检测中")
    self.isConnectServer_label.setStyleSheet("color:black")
    self.NetworkWindow_NextBtn.setEnabled(False)
    #self.NetworkWindow_RetryBtn.setEnabled(False)


#    # 检测互联网连接 - 废弃
#    try:
#        response = requests.get("http://119.29.29.29", timeout=2)
#        if response.status_code == 200:
#            self.isConnectNetwork_label.setStyleSheet("color:green")
#            self.isConnectNetwork_label.setText("成功")
#            isConnectNetwork=True
#        else:
#            self.isConnectNetwork_label.setStyleSheet("color:red")
#            self.isConnectNetwork_label.setText(str(response.status_code))
#    except Exception as e:
#        self.isConnectNetwork_label.setStyleSheet("color:red")
#        self.isConnectNetwork_label.setText("失败")
#        print(e)

    # 检测校园网连接
    log_print.outlog(1, "检测校园网连接")
    try:
        response = requests.get("http://mathe.neu.edu.cn", timeout=2)
        if response.status_code == 200:
            self.isConnectCampus_label.setStyleSheet("color:green")
            self.isConnectCampus_label.setText("成功")
            log_print.outlog(1, "检测校园网连接-成功")
            isConnectCampus=True
        else:
            self.isConnectCampus_label.setStyleSheet("color:red")
            self.isConnectCampus_label.setText(str(response.status_code))
            log_print.outlog(2, "检测校园网连接-失败:网站状态码"+str(response.status_code))
    except Exception as e:
        self.isConnectCampus_label.setStyleSheet("color:red")
        self.isConnectCampus_label.setText("失败")
        log_print.outlog(2, "检测校园网连接-失败:异常信息" + e)


    # 检测IPv4支持
    try:
        response = requests.get("https://mirrors4.tuna.tsinghua.edu.cn/", timeout=5)
        if response.status_code == 200:
            self.isSupportIPv4_label.setStyleSheet("color:green")
            self.isSupportIPv4_label.setText("成功")
            isSupportIPv4=True
            log_print.outlog(1, "检测IPv4支持-成功")
        else:
            self.isSupportIPv4_label.setStyleSheet("color:red")
            self.isSupportIPv4_label.setText(str(response.status_code))
            log_print.outlog(2, "检测IPv4支持-失败:网站状态码"+str(response.status_code))
    except Exception as e:
        self.isSupportIPv4_label.setStyleSheet("color:red")
        self.isSupportIPv4_label.setText("失败")
        log_print.outlog(2, "检测IPv4支持-失败:异常信息" + e)

    # 检测IPv6支持
    try:
        response = requests.get("https://mirrors6.tuna.tsinghua.edu.cn/", timeout=2)
        if response.status_code == 200:
            self.isSupportIPv6_label.setStyleSheet("color:green")
            self.isSupportIPv6_label.setText("成功")
            isSupportIPv6=True
            log_print.outlog(1, "检测IPv6支持-成功")
        else:
            self.isSupportIPv6_label.setStyleSheet("color:red")
            self.isSupportIPv6_label.setText(str(response.status_code))
            log_print.outlog(2, "检测IPv6支持-失败:网站状态码"+str(response.status_code))
    except Exception as e:
        self.isSupportIPv6_label.setStyleSheet("color:red")
        self.isSupportIPv6_label.setText("失败")
        log_print.outlog(2, "检测IPv6支持-失败:异常信息" + e)


    # 检测rustdesk服务器

    # Rustdesk server ip 由变量定义，可能在main.py中的ChangeServer_and_SwitchToNetworkWindow函数中修改
    log_print.outlog(1, "检测Rustdesk服务器")
    log_print.outlog(1, "当前服务器ip:"+serverip)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 21116  # Rustdesk Server 端口号
    try:
        sock.connect((serverip, port))
        self.isConnectServer_label.setStyleSheet("color:green")
        self.isConnectServer_label.setText("成功")
        isConnectServer = True
        log_print.outlog(1, "检测Rustdesk服务器-成功")
    except Exception as e:
        log_print.outlog(2, "检测Rustdesk服务器-失败:异常信息" + str(e))
        self.isConnectServer_label.setStyleSheet("color:red")
        self.isConnectServer_label.setText("失败")
        self.NetworkWindow_CustomBtn.setEnabled(True)



    # 测试用代码：
    #isConnectServer = False



    if isConnectCampus==True and isSupportIPv4==False and isConnectServer==False:
        #检查IPGW是否登录
        log_print.outlog(2, "检测IPGW登录状态")
        login_status = requests.get('https://ipgw.neu.edu.cn/cgi-bin/rad_user_info?callback=%20', timeout=1).text
        if '"error":"not_online_error"' in login_status:     #未登录
            self.isConnectCampus_label.setStyleSheet("color:red")
            self.isConnectCampus_label.setText("IPGW")
            log_print.outlog(2, "IPGW未登录")
        if '"error":"ok"' in login_status:     #已登录
            isloginIPGW=True
            log_print.outlog(1, "IPGW已登录")

    if isConnectCampus==False:
        #检测是否开启代理
        log_print.outlog(2, "检测代理状态")
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Internet Settings')
        value = winreg.QueryValueEx(key, "ProxyEnable")
        if value[0] == 1:
            self.isConnectCampus_label.setStyleSheet("color:red")
            self.isConnectCampus_label.setText("Proxy")
            log_print.outlog(2, "代理已开启")


    log_print.outlog(1, "网络检测结束")
    if isConnectCampus and isConnectServer:
        self.NetworkWindow_NextBtn.setEnabled(True)

    #这是原本的重试按钮的代码，已废弃
    #self.NetworkWindow_RetryBtn.clicked.connect(lambda: self.NetworkCheck_NetworkWindow(self))
    #self.NetworkWindow_RetryBtn.setEnabled(True)

