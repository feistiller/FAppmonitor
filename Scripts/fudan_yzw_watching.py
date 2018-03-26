# coding:utf-8
# 复旦研招网爬虫
from bs4 import BeautifulSoup
import urllib.request
import time
import random
import m_Log
from mail_send import mail_send


def diff(new_text):
    new_text = str(new_text)
    f1 = open("../temp/1.temp", "r")
    old_str = f1.read()
    print("老版本为：")
    print(old_str)
    print('\n')
    time.sleep(1)
    print("新版本是：")
    print(new_text)
    print('\n')
    time.sleep(1)
    m_Log.logWrite("reptile", "fdyzw", "new----", new_text)
    m_Log.logWrite("reptile", "fdyzw", "old----", old_str)
    if old_str == new_text:
        print("两次一致，不更新")
        m_Log.logWrite("reptile", "fdyzw", "start", "两次一致，不更新")
        f1.close()
        time.sleep(1)
        return "未发布内容"
    else:
        # 发送邮件并且重写temp
        print("两次不一致")
        m_Log.logWrite("reptile", "fdyzw", "start", "两次不一致")
        sm = mail_send(new_text)
        sm.send()
        f1.close()
        f = open("../temp/1.temp", "w")
        f.write(new_text)
        f.close()
        return "发布新内容"


# 入口
def main(n):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 62.0.3202.94 Safari / 537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    }
    baseUrl = 'http://www.gsao.fudan.edu.cn/1659/list.htm'
    print("开始爬取")
    # 设置请求头信息
    rep = urllib.request.Request(baseUrl, headers=header)
    m_Log.logWrite("reptile", "fdyzw", "start", "start")
    response = urllib.request.urlopen(rep)
    data = response.read()
    if (data == ''):
        print("read DownloadUrl failed")
        exit()
    else:
        print("读取成功")
        # print(data)
    soup = BeautifulSoup(data, "lxml")
    print("解析中")
    time.sleep(1)
    texts = soup.find_all('font', style="font-weight:bold;")
    for text in texts:
        print(text)
        print('\n')
    print("第一条信息是：")
    print(texts[0])
    print(diff(texts[0]))
    print("执行完成，这是第" + str(n) + '遍')
    print("______________________________________________________")
    time.sleep(20)
    m_Log.logWrite("reptile", "fdyzw", "end", "__________________________________")


# 入口
if __name__ == '__main__':
    n = 0
    while 1:
        main(n)
        n = n + 1
