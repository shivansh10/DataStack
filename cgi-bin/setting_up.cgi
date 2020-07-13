#!/usr/bin/python3
import time
import cgi
import subprocess
import cgitb
import os

# To show common errors in webbrowser
cgitb.enable()   # CGI Traceback... display errors in browser..
print("Content-type:text/html")
print("")


webdata=cgi.FieldStorage()    
time.sleep(45)
publicip=open('/etc/ansible/project_playbooks/publicip.txt','r')
privateip=open('/etc/ansible/project_playbooks/privateip.txt','r')
instanceid=open('/etc/ansible/project_playbooks/instanceid.txt','r')
publicdns=open('/etc/ansible/project_playbooks/publicdns.txt','r')
region=open('/etc/ansible/project_playbooks/region.txt','r')

n=open('/etc/ansible/project_playbooks/name.txt','r')
e=open('/etc/ansible/project_playbooks/email.txt','r')
u=open('/etc/ansible/project_playbooks/username.txt','r')
p=open('/etc/ansible/project_playbooks/password.txt','r')

pubip=publicip.read()
privip=privateip.read()
pubdns=publicdns.read()
instid=instanceid.read()
reg=region.read()
name=n.read()
email=e.read()
username=u.read()
password=p.read()


os.system("rm -rf /etc/ansible/project_playbooks/*.txt")

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Project@1234",
  database="project"
)

mycursor=mydb.cursor()
sql="Insert into register (name,email,username,password,instance_id,region,public_ip,public_dns,private_ip,hadoop) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(name,email,username,password,instid,reg,pubip,pubdns,privip,0)
mycursor.execute(sql,val)
mydb.commit()

