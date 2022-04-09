import netaddr, time, os
from client import *
from etc import *

def puwr(ssh,sec,iprange):
    print(f"\n[Started at {current()}]\n────────────────────────────────────────")
    count = 0 # acdresses scanned
    online = [] # online hosts found
    try:
        for i in netaddr.IPNetwork(iprange): # for each ip in subnet value
            count += 1
            cmd = ping(ssh,i) # request function
            if "100% packet loss" in cmd:
                continue
            else:
                for a in cmd.split(" "):
                    if "ttl=" in a: # finds TTL
                        online.append(i)
                        output = f"#{len(online)}".ljust(5," ") + f"{i}".ljust(16," ") + f"| {a}" # output
                        print(output)
                        time.sleep(sec)
        summary(online,count)
    except KeyboardInterrupt:
        summary(online,count)


# Author: Xeonrx
# Source: https://github.com/Xeonrx/Puwr
# License: MIT License
