import pymssql

class SqlConf(object):

    def __init__(self,host='**',user='sa',password='*',database='proxyPool'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def conn(self):
        conn = pymssql.connect(host=self.host,user=self.user,password=self.password,database=self.database)
        return conn

