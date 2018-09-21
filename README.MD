# 内网漏洞扫描工具

## 目录介绍

    ├── Config.py       配置文件
    ├── lib             c语言链接库文件
    ├── network         网络发现模块[文件夹]
    ├── README.MD       本文档
    ├── run.py          自动化网络扫描
    	spider			爬虫,爬取网页信息[文件夹]
	├── start.py        特定模块,具体网段扫描
    ├── temp            文件缓存目录[文件夹]
    └── vulnTool        漏洞模块
        ├── aspFrame    Web->asp[文件夹]
        ├── hardware    硬件,路由器等[文件夹]
        ├── jspFrame    Web->jsp[文件夹]
        ├── phpFrame    Web->php[文件夹]
        ├── server      服务器漏洞[文件夹]
        └── vulnScan.py 此目录的模块调用

### Nerwork
> zoomEye
```
	调用ZoomEye网站的接口广收服务器信息，
		指定端口、服务、地域、等信息。保存结果，进行下一步扫描。

例: 保存 81端口的信息, 摄像头信息；
	1. 广收webcam信息，保存到本地
	2. 分析webcam【海康威视、思科、JAWS等】
	3. 分析可否爆破,执行专属脚本进行爆破
	
```


## 使用教程


## 交流
