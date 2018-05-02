# coding: utf-8
import sys, os
print(sys.path)
import bottle

dirpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dirpath)
os.chdir(dirpath)

import upload
application = bottle.default_app()
