# coding: utf-8
from bottle import route, run, template
from bottle import TEMPLATE_PATH

@route('/')
def index():
    return "Hello World! Bottle and Apache!"
#run(host='example.com', port=80)
