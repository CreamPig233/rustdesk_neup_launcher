import base64, networkcheck

ip=networkcheck.serverip
key="hE8ri5Xrk5p5m3lhm2931fg3I7Uh4jOByGfnjuaQK5c="

use_official_server = False

def generate_exe_file():
    if not use_official_server:
        config_string=generate_config_string()
        new_file_name='rustdesk--'+config_string+'--.exe'
        #待补充生成exe文件的代码
    else:
        #使用原exe的代码
        pass


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
    generate_config_string("172.20.65.19", "hE8ri5Xrk5p5m3lhm2931fg3I7Uh4jOByGfnjuaQK5c=")