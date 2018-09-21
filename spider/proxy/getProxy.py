import requests
import json
import pymssql
import time
import config

def getProxy(conn,cursor):
    res = requests.get("https://proxyapi.mimvp.com/api/fetchopen.php?orderid=867080318812480105&num=20&result_fields=1,2&result_format=json")
    resE = res.text.encode("utf-8")
    resJson = json.loads(resE)
    print resJson
    for i in resJson["result"]:
        cursor.execute("insert into proxy_mimvp values ('%s','%s')" % (i["http_type"],i["ip:port"]))
    conn.commit()

if __name__ == "__main__":
    sqlConf = config.SqlConf()
    sqlConn = sqlConf.conn()
    with sqlConn.cursor() as cursor:
        #print("====")
        while True:
            getProxy(sqlConn,cursor)
            time.sleep(12)
