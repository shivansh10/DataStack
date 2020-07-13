#!/usr/bin/python3
import cgi
import subprocess,os
import cgitb
import webbrowser,time
# To show common errors in webbrowser
cgitb.enable()   # CGI Traceback... display errors in browser..
print("Content-type:text/html")
print("")



webdata=cgi.FieldStorage()  
username=webdata.getvalue("username")
password=webdata.getvalue("password")

import mysql.connector
mydb = mysql.connector.connect(host="localhost",database="project",user="root",password="Project@1234")
'''
mydb = mysql.connector.connect(
  user="root",
  passwd="Project@1234",
  database="project",
host = "localhost"

)'''

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM register where username='{}' and password='{}'".format(username,password))
myresult = mycursor.fetchall()

if len(myresult)>0:
	uname=myresult[0][0]
	email=myresult[0][1]
	pip=myresult[0][6]
	print('''

<html>
      <head>
	<form method="post">   
       <meta http-equiv="refresh" content="0;url=../check.php?name=%s&ip=%s&email=%s" />
	</form>
      </head>
    </html>

'''%(uname,pip,email))
else:
	print('''
<html>
      <head>
          <meta http-equiv="refresh" content="0;url=../index.php" />
      </head>
    </html>
''')
	print("Invalid Credentials")
