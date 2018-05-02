#import mysql.connector
import MySQLdb
import json
import mksql


#upload_result = mksql.msql(upload_str)
conn = MySQLdb.connect(host="localhost", port=3306, user="root", password="prodpassw0rd", database="asterisk")
cur = conn.cursor()
#query = upload_result
query = ["INSERT INTO asterisk.timegroups_details (timegroupid,time) VALUES (6,'12:00-20:59|*|03|apr');","INSERT INTO asterisk.timegroups_details (timegroupid,time) VALUES (6,'12:00-20:59|*|04|apr');"]
resultlist = []

for query_set in query:
  print(query_set)
  cur.execute(query_set)
  resultlist.append(cur.fetchall())
cur.close()
conn.close()
json.dumps(resultlist)
