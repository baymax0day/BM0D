import sys
from datetime import timedelta
from flask import Flask
import os


app = Flask(__name__)
sys.path.append(sys.path[0] + '/vulnTool/')
fileSelf_path = os.path.split(os.path.realpath(__file__))[0] + '/../vulnTool/'