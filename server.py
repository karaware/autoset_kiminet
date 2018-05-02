import sys
import os
# bottle.py, waitressのPATH設定
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'libs'))
from bottle import route, run, template

@route('/hello/<name>')
def greet(name):
    return template('<b>Hello {{name}}</b>!', name=name)

# bottle.py起動時にWebサーバとしてwaitressを指定
run(server="waitress", host='0.0.0.0', port=8080)
