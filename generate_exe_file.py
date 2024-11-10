import base64, networkcheck
import os, os.path, shutil, log_print

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


    log_print.outlog(1, "开始生成exe文件")
    log_print.outlog(1, "当前工作目录："+workdir)
    log_print.outlog(1, "删除可能存在的rustdesk--*--.exe文件")
    #删除可能存在的rustdesk--*--.exe文件
    try:
        files = os.listdir(os.path.join(workdir))
        log_print.outlog(1, "文件列表："+str(files))
        for file in files:
            if 'rustdesk--' in file:
                try:
                    log_print.outlog(1, "删除文件："+file)
                    os.remove(os.path.join(workdir, file))
                except Exception as e:
                    log_print.outlog(2, "删除失败，异常信息：" + str(e))
    except Exception as e:
        log_print.outlog(2, "删除失败，异常信息：" + str(e))


    if not use_official_server:
        log_print.outlog(1, "使用自定义服务器，生成新的exe文件")
        #使用自定义服务器，则生成新的exe文件
        config_string=generate_config_string()
        global new_file_name
        new_file_name='rustdesk--'+config_string+'--.exe'
        log_print.outlog(1, "新的exe文件名："+new_file_name)

        try:
            log_print.outlog(1, "复制rustdesk")
            shutil.copy(os.path.join(workdir, 'rustdesk.exe'), os.path.join(workdir, new_file_name))
            return os.path.join(workdir, new_file_name)
        except Exception as e:
            log_print.outlog(2, "复制文件失败，异常信息：" + str(e))
            return -1

    else:
        #使用原exe的代码
        return os.path.join(workdir, 'rustdesk.exe')


def generate_config_string():
    log_print.outlog(1, "生成配置字符串")
    original_config = {"host":ip,"relay":"","api":"","key":key}
    original_config = str(original_config).replace(" ", "").replace("'", "\"")

    log_print.outlog(1, "配置字符串："+original_config)

    base64_config = base64.b64encode(original_config.encode()).decode()
    base64_config = base64_config.replace("=", "")
    base64_config = base64_config[::-1]

    log_print.outlog(1, "生成配置："+base64_config)
    return base64_config


if __name__ == '__main__':
    generate_config_string()