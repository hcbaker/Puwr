import paramiko
from etc import *

def connect(host,user,password,port): # sets up SSH connection
    ssh = paramiko.SSHClient();ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=host,username=user,password=password,port=port,timeout=3)
        return ssh
    except:
        exit(f"Failed to reach {user}@{host} via ssh. Maybe the credintals are incorrect?")
        
def command(ssh,cmd): # processes command to machine via ssh
    stdin, stdout, stderr = ssh.exec_command(cmd)
    result = str(stdout.read())
    return result

def ping(ssh,ip): # pings host and returns output
    stdin, stdout, stderr = ssh.exec_command(f"ping {ip} -c 1 -w 1")
    cmd = str(stdout.read())
    return cmd

def prtscan(ssh,ip,port): # probes for open ports on discovered hosts.
    cmd = f'''python3 -c "import socket;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('{ip}',{port}));print(True)"'''
    if "True" in command(ssh,cmd):
        return True
    else:
        return False

def summary(online,count): # prints summary of scan
    print(f"\n[Finished at {current()}]\n────────────────────────────────────────")
    exit(f"Scanned) {count}\nOnline)  {len(online)} ")

# Author: Xeonrx
# Source: https://github.com/Xeonrx/Puwr
# License: MIT License
