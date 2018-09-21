
# coding:utf-8
# author:wolf
import urllib2
import Config
import requests

def get_plugin_info():
    plugin_info = {
        "name": "Jboss信息泄露",
        "info": "Jboss信息泄露",
         "exp_url":"",
        "docker":"",
        "other":""
    }
    return plugin_info


def check(ip, port, timeout):
    url = "http://%s:%d" % (ip, int(port))
    try:
        res = requests.get(url+"/status?full=true",timeout)
        if res.status_code == 200:
            return u"%s JBOSS信息泄露" % ip
    except:
        pass
