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
uname=myresult[0][0]
email=myresult[0][1]
instanceid=myresult[0][4]
region=myresult[0][5]
region = (region[:len(region)-1])  # skipping the last word from region -- "ap-south-1b -->> ap-south-1"  bcoz only region name is required,not subpart.
print(instanceid)
print(region)
#get the value of first name	

os.system("sudo ansible-playbook /etc/ansible/project_playbooks/start.yml  --extra-vars 'instance_id=%s region=%s'   &>/dev/null "%(instanceid,region))

publicip=open('/etc/ansible/project_playbooks/newpublicip.txt','r')
privateip=open('/etc/ansible/project_playbooks/newprivateip.txt','r')
publicdns=open('/etc/ansible/project_playbooks/newpublicdns.txt','r')


pubip=publicip.read()
privip=privateip.read()
pubdns=publicdns.read()

os.system("rm -rf /etc/ansible/project_playbooks/*.txt")

mycursor=mydb.cursor()
sql="UPDATE register  set public_ip='%s', public_dns='%s', private_ip='%s', hadoop='%s' where public_ip='%s'" % (pubip,pubdns,privip,2,pip)
mycursor.execute(sql)
mydb.commit()


print('''

<html>
      <head>
        <form method="post">
       <meta http-equiv="refresh" content="0;url=../check.php?name=%s&ip=%s&email=%s" />
        </form>
      </head>
    </html>

'''%(uname,pubip,email))








