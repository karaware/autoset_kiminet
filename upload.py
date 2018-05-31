import os
from bottle import route, run, template, redirect, request, post, get
import mkexecsql
import sys
import rm_prev_month

@route('/upload', method=["GET","POST"])
def upload():
    return template('index')


@route('/sql', method=["GET","POST"])
def sql():
    upload   = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    upload_str = upload.filename

    #file check
    upload.save("./uploadfile/", overwrite=True)
    upload_result = mkexecsql.msql(upload_str)
    return template("./sql",m=upload_result)


@route('/prev_month', method=["GET","POST"])
def prev_month():
    rm_result = rm_prev_month.rm_prev_month()
    return template('./comp_rm',m=rm_result)



#@route('/result', method=["GET","POST"])
#def do_upload():
#    upload   = request.files.get('upload')
#    name, ext = os.path.splitext(upload.filename)
#    upload_str = upload.filename
#
#    return name
#    sys.exit()
#
#    #file check
#    if ext not in ('.xlsx'):
#        return template("notallow")
#    else:
#        upload.save("./tmp",overwrite=True)
##        return template("complete",m=name)
#        return template("./complete",m=upload_str)

#    return ext
#    return name
#    return upload_str
#    sys.exit()
#    if ext not in ('.xlsx'):
#        return template("notallow")
#    else:
#        upload.save("./tmp",overwrite=True)
#        #upload_result = mksql.msql(upload_str)
#        upload_result = mkexecsql.msql(upload_str)
#        return template("./sql",m=upload_result)
#     else:
#        return ext
# bottle.py起動
# run(host='0.0.0.0', port=8080)
