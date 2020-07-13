#!/usr/bin/python3
import   cgi,subprocess,os
import  cgitb
import time
cgitb.enable()

print("Content-type:text/html")
print("")

#  get  html page code and data
web=cgi.FieldStorage()


pip=str(web.getvalue('ip'))
ip=str(web.getvalue('ip'))+","


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Project@1234",
  database="project"
)

mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM register where public_ip='{}' ".format(pip))
myresult = mycursor.fetchall()
instanceid=myresult[0][4]
region=myresult[0][5]
region = (region[:len(region)-1])  # skipping the last word from region -- "ap-south-1b -->> ap-south-1"  bcoz only region name is required,not subpart.
#get the value of first name	
os.system("sudo ansible-playbook /etc/ansible/project_playbooks/stop.yml  --extra-vars 'instance_id=%s region=%s'   &>/dev/null &"%(instanceid,region))
time.sleep(5)
print('''

<html>
      <head>
        <form method="post">
       <meta http-equiv="refresh" content="0;url=../dashboard/stop.php" />
        </form>
      </head>
    </html>

''')
