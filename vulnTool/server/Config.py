# coding:utf8
# -----------------colorama模块的一些常量---------------------------
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL
from colorama import init,Fore,Back,Style
import os
import sys

init(autoreset=True)
file_pwd = os.getcwd()
PASSWORD_DIC_DIR = []

with open( file_pwd + "/temp/password") as f:
    for i in f.readlines():
        PASSWORD_DIC_DIR.append(i.strip('\n'))   # 弱口令密码字典

# with open( file_path + "../../temp/password") as f:
#     for i in f.readlines():
#         PASSWORD_DIC_DIR.append(i.strip('\n'))   # 弱口令密码字典

