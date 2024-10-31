import base64, networkcheck
import os, os.path, shutil

#测试用代码

workdir=os.getcwd()     #发布版应该用这个
#workdir=r'D:\rdtest'   #测试用代码

ip=networkcheck.serverip
key="hE8ri5Xrk5p5m3lhm2931fg3I7Uh4jOByGfnjuaQK5c="  #发布时应修改默认key
new_file_name=''

use_official_server = False

def get_rustdesk_path():
    if use_official_server:
        return os.path.join(workdir, 'rustdesk.exe')
    else:
        return os.path.join(workdir, new_file_name)
    pass

def generate_exe_file():

    #删除可能存在的rustdesk--*--.exe文件
    files = os.listdir(os.path.join(workdir))
    for file in files:
        if 'rustdesk--' in file:
            os.remove(os.path.join(workdir, file))


    if not use_official_server:
        #使用自定义服务器，则生成新的exe文件
        config_string=generate_config_string()
        global new_file_name
        new_file_name='rustdesk--'+config_string+'--.exe'
        #待补充生成exe文件的代码
        shutil.copy(os.path.join(workdir, 'rustdesk.exe'), os.path.join(workdir, new_file_name))
        return os.path.join(workdir, new_file_name)
    else:
        #使用原exe的代码
        return os.path.join(workdir, 'rustdesk.exe')


def generate_config_string():
    original_config = {"host":ip,"relay":"","api":"","key":key}
    original_config = str(original_config).replace(" ", "").replace("'", "\"")
    print('gener:'+ip)
    print(original_config)
    base64_config = base64.b64encode(original_config.encode()).decode()
    base64_config = base64_config.replace("=", "")
    base64_config = base64_config[::-1]
    print(base64_config)
    return base64_config


if __name__ == '__main__':
    generate_config_string()