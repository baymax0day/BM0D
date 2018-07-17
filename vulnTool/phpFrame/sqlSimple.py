# coding:utf8
# !/usr/bin/python3
import requests
import re
import sys

sys.path.append('../..')
from Config import Colored
from Config import Config

class sql_Simple(Colored):
    '''
        简单的数据库注入测试
        对页面回显数据进行判断确定是否产生sql注入
        url:测试的url地址
        debug:是否输出debug信息
        reg:对于非id结尾的url,直接传入可触发错误的url,然后传入正则表达式匹配
    '''

    def __init__(self,url,debug,reg=''):
        self.url = url + "'" if re.match(r'^.*\.php\?.*\d+$',url) else url
        self.dbg = debug
        self.reg = reg

    def contain_error(self,msg):
        '''
            页面中是否含有'you have sql error'
        '''
        error_find = re.search(r'error',str(msg),re.I)
        reg_find = re.search(self.reg,str(msg,re.I) if reg != '' else False  #自定义的正则表达式:如果不为空,则对其进行匹配
        if error_find or reg_find:  #两个中的一个存在就可以进行数据库注入
            print(Colored.green('[INFO]:页面存在错误信息,可进一步测试数据库注入'))
            return True
        else:
            return False

    def build_error(self):
        '''
            对url进行判断,拼接 使得页面返回错误信息
        '''
        html = requests.get(self.url)
        if self.dbg:
            print('[Target-Plugin]:%s' % self.url)
        self.contain_error(html.content)


    def run(self):
        if self.dbg:
            print('[Target-url]:%s' % self.url)
        self.build_error()


if __name__ == '__main__':
    test = sql_Simple('http://www.hzsrkj.com/allist.php?id=51',Config.IS_DEBUG)
    test.run()
    #a = Config.Colored()
    #print(a.red('s'))
    #print(Config.Corlored.red('test'))
