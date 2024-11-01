import datetime, colorama
colorama.init(autoreset=True)


def outlog(level, msg):
    '''

    :param level: 1=info, 2=warn, 3=error
    :param msg:
    :return:
    '''

    nowtime = datetime.datetime.now().strftime('%H:%M:%S.%f')
    if level ==1:
        level='INFO'
        print(nowtime + '\t' + 'INFO' + '\t' + msg)
    elif level ==2:
        print(colorama.Fore.YELLOW + nowtime + '\t' + "WARN" + '\t' + msg)
    else:
        print(nowtime + '\t' + "000"+str(level) + '\t' + msg)



    #print(nowtime+'\t'+level+'\t'+msg)