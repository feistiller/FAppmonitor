# -*- coding: UTF-8 -*-
import os
import time

# 写一个简单的日志脚本
PATH_BASE = '../Logs/'


def logWrite(file, name, before, text):
    file_url = PATH_BASE + file
    if not os.path.exists(file_url):
        os.makedirs(file_url)
    # 写文件
    file = open(file_url + '/' + name + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log', 'a')
    file.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + before + ":" + text + '\n')
    file.close()
