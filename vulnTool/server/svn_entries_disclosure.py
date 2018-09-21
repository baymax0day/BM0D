# coding:utf-8
import requests
import binascii
import collections
import mmap
import struct
import sys
import urllib2
import os
import urlparse
import zlib
import threading
import Queue
import re
import time


def get_plugin_info():
    plugin_info = {
        "name": ".svn代码泄露",
        "info": ".svn代码泄露,可使用githack工具",
        "exp_url": "https://www.waitalone.cn/seay-svn-poc-donw-20140505.html",
        "docker": "",
        "other": ""
    }
    return plugin_info


def check(ip, port, timeout):
    try:
        url = "http://"+ip+":" + port
        res = requests.get(url+"/.svn",timeout)
        if res.status_code == 200:
            return u"%s 存在git目录" % url
        res = requests.get(url + "/.svn/all-wcprops", timeout)
        if res.status_code == 200:
            return u"%s 存在git目录 " % url

    except Exception, e:
        pass

