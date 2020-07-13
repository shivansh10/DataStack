#!/usr/bin/python3
import cgi
import subprocess 
import os
import cgitb
import time
# To show common errors in webbrowser
cgitb.enable()   # CGI Traceback... display errors in browser..
print("Content-type:text/html")
print("")


webdata=cgi.FieldStorage()    # This will collect all the HTML code with data.
# Now extracting value of X
name=webdata.getvalue('name')
email=webdata.getvalue('email')
username=webdata.getvalue('username')
password=webdata.getvalue('password')

n=open('/etc/ansible/project_playbooks/name.txt','w')
e=open('/etc/ansible/project_playbooks/email.txt','w')
u=open('/etc/ansible/project_playbooks/username.txt','w')
p=open('/etc/ansible/project_playbooks/password.txt','w')


n.write(name)
e.write(email)
u.write(username)
p.write(password)

n.close()
e.close()
u.close()
p.close()


os.system("sudo ansible-playbook /etc/ansible/project_playbooks/launch_user_instance.yml &>/dev/null &")
time.sleep(10)
print('''
 <html>
      <head>
          <meta http-equiv="refresh" content="0;url=../wait.html" />
      </head>
    </html>

''')

