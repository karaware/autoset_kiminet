from datetime import datetime
from dateutil.relativedelta import relativedelta
import re
import sys
import MySQLdb

def rm_prev_month():
    today = datetime.today()
    prev = today + relativedelta(months=-1)
    prev_month = prev.strftime('%b').lower()

    # 202.78.218.161(キミネット様ホスト)
    sqlstr1 = "DELETE FROM asterisk.timegroups_details WHERE timegroupid = 1 AND time LIKE '%"
    # wm0104.fonex.jp(検証用)
    #sqlstr1 = "DELETE FROM asterisk.timegroups_details WHERE timegroupid = 6 AND time LIKE '%"

    sqlstr2 = "%';"
    sqlstr_comb = sqlstr1 + prev_month + sqlstr2

    # 202.78.218.161(キミネット様ホスト)
    conn = MySQLdb.connect(host="202.78.218.161", port=3306, user="ruby", password="passw0rd", database="asterisk")
    # wm0104.fonex.jp(検証用)
    #conn = MySQLdb.connect(host="wm0104.fonex.jp", port=3306, user="ruby", password="passw0rd", database="asterisk")

    cur = conn.cursor()
    cur.execute(sqlstr_comb)
    cur.close()
    conn.close()
    return sqlstr_comb
