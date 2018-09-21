# coding:utf8
import socket
import time
import requests
import random

def get_plugin_info():
    plugin_info = {
        "name": "Axis2信息泄露",
        "info": "HappyAxis.jsp 页面存在系统敏感信息",
        "exp_url":"",
        "docker":"https://github.com/ainehanta/docker-axis2/blob/master/Dockerfile",
        "other":""
    }
    return plugin_info

def check(ip, port, timeout):
    try:
        url = ip+":"+port+"/axis2/axis2-web/HappyAxis.jsp"
        res = requests.get(url,timeout=timeout)
        if res.status_code == 200:
            return u'%s 存在Axis2信息泄露漏洞 访问地址:%s' % (ip,url)
    except:
        pass
