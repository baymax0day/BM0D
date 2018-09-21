#coding:utf-8

import requests
import json
import pymssql
import time
import config

def checkIP(conn,cursor):
    '''
        从proxy_mimvp 表中检查IP的可用性
    '''
    cursor.execute("select * from proxy_mimvp order by id desc")
    resList = cursor.fetchall()
    for i in resList:
        proxy = i[2]
        host = "http://www.baymax0day.com/"
        try:
            res = requests.get(host, proxies={"http": proxy},timeout=2)
            if res.status_code == 200:
                cursor.execute("insert into useful values ('%s')" % proxy)
                conn.commit()
        except Exception as msg:
            print(msg)
            continue

def ipToFile(filename,cursor):
    cursor.execute("select top 100 * from useful order by id desc")
    proxies = cursor.fetchall()
    with open(filename,'a') as f:
        for i in proxies:
            f.write(str(i[1]) + "\r\n")

def main():
    sqlConf = config.SqlConf()
    sqlConn = sqlConf.conn()
    with sqlConn.cursor() as cursor:
        ipToFile("ips.txt",cursor)

if __name__ == "__main__":
    main()
