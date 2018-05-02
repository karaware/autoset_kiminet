import os
from bottle import route, run, template, redirect, request, post, get
import sqlite3
import mksql
import mkexecsql

@route('/upload', method=["GET","POST"])
def upload():

  return template('index')

@route('/result', method=["GET","POST"])
def do_upload():
    upload   = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    upload_str = upload.filename

    #file check
    if ext not in ('.xlsx'):
        return template("notallow")
    else:
        upload.save("./tmp",overwrite=True)
#        return template("complete",m=name)
        return template("complete",m=upload_str)

@route('/sql', method=["GET","POST"])
def sql():
    upload   = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    upload_str = upload.filename

    #file check
    if ext not in ('.xlsx'):
        return template("notallow")
    else:
        upload.save("./tmp",overwrite=True)
        #upload_result = mksql.msql(upload_str)
        upload_result = mkexecsql.msql(upload_str)
        return template("sql",m=upload_result)



# bottle.py起動
# run(host='0.0.0.0', port=8080)
