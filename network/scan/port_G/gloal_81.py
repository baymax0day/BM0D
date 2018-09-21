# !/usr/bin/env python
# coding:utf-8

import json
import sys


sys.path.append("../../../lib")
import nmap

def scan_81(hosts, port):
    res_List = []
    nm = nmap.PortScanner()
    nm.scan(hosts=hosts, arguments=" -P0 -sV", ports=str(port))
    for host in nm.all_hosts():
        #print(host)
        #print(nm[host])
        #print(nm[host].state())
        #print(nm[host].tcp(port))
        if nm[host].state() == "up" and nm[host].tcp(port)["state"] == "open":
            res_List.append(nm[host])

    res = json.dumps(res_List)
    resF = open(hosts.split("/")[0], "w+")
    resF.write(res)
    resF.close()
    print(hosts + "结束")
    return res_List

def main():
    with open("testIP","r") as f:
        lines = f.readlines()
        for i in lines:
            print(i.split("\t")[2] + "开始")
            scan_81(i.split("\t")[2], 81)
        #print("文件长度 %d" % len(lines))


if __name__ == "__main__":
    main()

