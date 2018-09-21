#coding:utf8

import os
from flask import request, render_template, redirect, url_for, session, make_response
from . import app, fileSelf_path 
import xlwt
import imp
import re

@app.route('/filter')
def Search():
    return render_template('search.html')

# 搜索结果页
@app.route('/scan')
def Main():
    q = request.args.get('q', '')
    
    _vulnScan = imp.load_source("123",os.path.join(fileSelf_path  +'/',"vulnScan.py"))
    modName = _vulnScan.getModName()
    
    if q:  # 基于搜索条件显示结果
        ip = q.split(" ")[0].split(":")[1]
        port = q.split(" ")[1].split(":")[1]
        _vulnSSH = ""
        _sshPath = ""
        for i in modName:
            if re.search(r"ssh",i) != None:
                print(i)
                _sshPath = i
                _vulnSSH = imp.load_source("123",i)
        
        res = _vulnSSH.check(ip,int(port),2020)
        
        title = ['IP', '端口',  '漏洞描述', '插件名称', '扫描结果']
        wbk = xlwt.Workbook(encoding='utf-8')
        sheet = wbk.add_sheet('sheet 1')
        for i in range(1,len(title)):    
            sheet.write(0,i,title[i])
        
        sheet.write(1,1,ip)
        sheet.write(1,2,port)
        sheet.write(1,3,_vulnSSH.get_plugin_info()["info"])
        sheet.write(1,4,_sshPath)
        sheet.write(1,5,res)

        wbk.save('./views/static/test.xls')

        return render_template('test.html')
    else:  # 自定义，无任何结果，用户手工添加
        return render_template('search.html')



@app.route('/selfplugin')
def Plugin():

    _vulnScan = imp.load_source("123",os.path.join(fileSelf_path  +'/',"vulnScan.py"))
    modSchema = _vulnScan.getModule()
        
    return render_template('plugin.html', count=66, modSchema=modSchema)

@app.route('/404')
def NotFound():
    return render_template('404.html')


@app.route('/500')
def Error():
    return render_template('500.html')
