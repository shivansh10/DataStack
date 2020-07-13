#!/usr/bin/python3

import cgi,subprocess
import cgi
import cgitb
import os
import time
import webbrowser

cgitb.enable()
print("Content-type:text/html")
print("")


web=cgi.FieldStorage()

ip=str(web.getvalue('ip'))+","

pip=str(web.getvalue('ip'))

os.system(" sudo ansible-playbook  /etc/ansible/project_playbooks/check_jn.yml  -i '%s'  &>/dev/null "%ip)
time.sleep(5)
f=open('/etc/ansible/project_playbooks/checkjn.txt','r')
result=f.read()

if(len(result)>0):
	tk = open('/etc/ansible/project_playbooks/checkjn.txt','r')
	token=tk.read()
	url="http://"+pip+":8888/?"+token
	os.system("sudo rm -rf /etc/ansible/project_playbooks/*.txt")
	print('''

<html>
      <head>
      <meta http-equiv="refresh" content="0; URL='%s'">
	</head>
    </html>

'''%url)
else:
	os.system(" sudo ansible-playbook  /etc/ansible/project_playbooks/jupyter-notebook.yml  -i '%s'  &>/dev/null "%ip)
	time.sleep(2)
	tk=open('/etc/ansible/project_playbooks/jupyterip.txt','r')
	token=tk.read()
	url="http://"+pip+":8888/?"+token
	os.system("sudo rm -rf /etc/ansible/project_playbooks/*.txt")
	print('''
<html>
      <head>
      <meta http-equiv="refresh" content="0; URL='%s'">
        </head>
    </html>

'''%url)
