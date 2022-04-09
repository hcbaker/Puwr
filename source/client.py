import paramiko
from etc import *

def connect(host,user,password,port):
    ssh = paramiko.SSHClient();ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=host,username=user,password=password,port=port,timeout=3)
        return ssh
    except:
        exit(f"Failed to reach {user}@{host} via ssh. Maybe the credintals are incorrect?")
        

def command(ssh,cmd):
    stdin, stdout, stderr = ssh.exec_command(cmd)
    result = str(stdout.read())
    if "default via" in cmd:
        result = result.split(" ");return result[2]
    else:
        return result

def ping(ssh,ip):
    stdin, stdout, stderr = ssh.exec_command(f"ping {ip} -c 1 -w 1")
    cmd = str(stdout.read())
    return cmd

def summary(online,count):
    print(f"\n[Finished at {current()}]\n────────────────────────────────────────")
    exit(f"Scanned) {count}\nOnline)  {len(online)} ")


def portscn(ssh,ip,prt):

    scn = f"python3 -c 'import socket;s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);r = s.connect_ex(('{ip}',{prt}));result = True if r == 0 else False;print(result)'"
    stdin, stdout, stderr = ssh.exec_command(scn)
    cmd = str(stdout.read())
    print(cmd)


# Author: Xeonrx
# Source: https://github.com/Xeonrx/Puwr
# License: MIT License