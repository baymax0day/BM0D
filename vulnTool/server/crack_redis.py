# coding:utf-8
import socket

import Config


def get_plugin_info():
    plugin_info = {
        "name": "Redis弱口令",
        "info": "导致数据库敏感信息泄露，严重可导致服务器被入侵。",
        "exp_url": "",
        "docker": "",
        "other": ""
    }
    return plugin_info


def check(ip, port, timeout):
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, int(port)))
        s.send("INFO\r\n")
        result = s.recv(1024)
        if "redis_version" in result:
            return u"未授权访问"
        elif "Authentication" in result:
            PASSWORD_DIC = Config.PASSWORD_DIC_DIR
            for pass_ in PASSWORD_DIC:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, int(port)))
                s.send("AUTH %s\r\n" % (pass_))
                result = s.recv(1024)
                if '+OK' in result:
                    return u"存在弱口令，密码：%s" % (pass_)
    except Exception, e:
        pass
