import netaddr, time, os
from client import *
from etc import *

def puwr(ssh,sec,iprange,portrange,scanports):

    if scanports:
        if command(ssh,"which python3") == "b''":
            exit("EXIT) Python3 isn't avaible on this machine to support port scanning, or isn't in a path...")
    print(f"[PUWR started at {current()}]")
    count = 0 # acdresses scanned
    online = [] # online hosts found
    print("________________________________________\nNUMB|DISCOVERED HOSTS|TIME TO LIVE|PORTS")
    try:
        for i in netaddr.IPNetwork(iprange): # for each ip in subnet value
            openports = []
            count += 1
            cmd = ping(ssh,i) # request function
            if "100% packet loss" in cmd:
                continue
            else:
                for a in portrange:
                    if prtscan(ssh,i,a) == True:
                        openports.append(a)
                for a in cmd.split(" "):
                    if "ttl=" in a: # finds TTL
                        online.append(i)
                        output = f"#{len(online)}".ljust(4," ") + f"|{i}".ljust(17," ") + f"|{a}".ljust(13," ") + "|" + str(openports)[1:-1] # output to terminal
                        print(output)

                        time.sleep(sec)
        summary(online,count)
    except KeyboardInterrupt:
        summary(online,count)


# Author: Xeonrx
# Source: https://github.com/Xeonrx/Puwr
# License: MIT License
