# coding:utf8
# -----------------colorama模块的一些常量---------------------------
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL
from colorama import init,Fore,Back,Style
import os
init(autoreset=True)

file_pwd = os.getcwd()
PASSWORD_DIC_DIR = []

with open( file_pwd + "/temp/password") as f:
    for i in f.readlines():
        PASSWORD_DIC_DIR.append(i.strip('\n'))   # 弱口令密码字典

class Config(object):
    PASSWORD_DIC_DIR = []
    with open("./temp/password") as f:
        for i in f.readlines():
            PASSWORD_DIC_DIR.append(i.strip('\n'))   # 弱口令密码字典

    IS_DEBUG = True

class Colored(object):

    @staticmethod
    #  前景色:红色  背景色:默认
    def red( s):
        return Fore.RED + s + Fore.RESET

    @staticmethod
    #  前景色:绿色  背景色:默认
    def green( s):
        return Fore.GREEN + s + Fore.RESET

    @staticmethod
    #  前景色:黄色  背景色:默认
    def yellow( s):
        return Fore.YELLOW + s + Fore.RESET

    @staticmethod
    #  前景色:蓝色  背景色:默认
    def blue( s):
        return Fore.BLUE + s + Fore.RESET

    @staticmethod
    #  前景色:洋红色  背景色:默认
    def magenta( s):
        return Fore.MAGENTA + s + Fore.RESET

    @staticmethod
    #  前景色:青色  背景色:默认
    def cyan( s):
        return Fore.CYAN + s + Fore.RESET

    @staticmethod
    #  前景色:白色  背景色:默认
    def white( s):
        return Fore.WHITE + s + Fore.RESET

    @staticmethod
    #  前景色:黑色  背景色:默认
    def black( s):
        return Fore.BLACK

    @staticmethod
    #  前景色:白色  背景色:绿色
    def white_green( s):
        return Fore.WHITE + Back.GREEN + s + Fore.RESET + Back.RESET
