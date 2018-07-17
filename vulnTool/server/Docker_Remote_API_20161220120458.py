# coding:utf-8
import socket
import requests
import Config


def get_plugin_info():
    plugin_info = {
        "name": "Docker Remote API未授权访问",
        "info": "数据库敏感信息泄露",
        "exp_url": "http://www.tuicool.com/articles/3Yv2iiY",
        "docker": "",
        "other": ""
    }
    return plugin_info


def check(ip, port, timeout):
    try:
        url = "http://"+ip+":" + port
        res = requests.get(url+"/containers/json",timeout)
        if res.status_code == 200:
            return u"%s 存在Docker 未授权访问漏洞" % url
    except Exception, e:
        pass
