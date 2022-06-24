
<p align="center">
 <img src="https://github.com/Xeonrx/Puwr/blob/main/img/icon.png" width="400" height="280">
 </p>
<p align="center">
 <img src="https://img.shields.io/github/stars/Xeonrx/Puwr?style=social">
 <img src="https://img.shields.io/github/forks/Xeonrx/Puwr?style=social">
 <img src="https://img.shields.io/github/watchers/Xeonrx/Puwr?style=social">
 </p>

## Contents
- [About Puwr](#puwr)
- [Upcoming Features](#upcoming)
- [Puwr Usage](#usage)
- [Tested Systems](#tested-operating-systems)
- [Port scanning](#port-scanning)
- [Showcases](#showcases)
- [Disclaimer](#disclaimer)
- [MIT License](#license)

## Puwr
Easily expand your attack surface on a local network by discovering more hosts, via SSH.
Using a machine running a SSH service, Puwr uses a given subnet range to scope out IP's, sending back any successful ping requests it has.
This can be used to create a pivoting attack from a compromised machine, by returning you hosts you couldn't normally discover from your own device.
Open ports can then be probed on these discovered devices, to find a gateway into attacking more devices.

*(example below of how Puwr handles requests)*
![LogoImage](https://github.com/Xeonrx/Puwr/blob/main/img/diagram.PNG)

## Upcoming
Here are some new features I plan to add in along with the upcoming update.<br />
- Scan for open ports of discovered hosts **(DONE)**
- Change CLI output to look more neat and organized **(DONE)**
- Enumerate information on "victim" host for privilege escalation
- Optional colored output

# Usage
Puwr is simple to run, only requiring 4 flags: <br />
`python3 puwr.py (MACHINE IP) (USER) (PASSWORD) (SUBNET VALUE)`


example: <br />
`python3 puwr.py 10.0.0.53 xeonrx password123 10.0.0.1/24`


>If you need to connect through a port other than 22, use the `-p` flag. (example: -p 2222)<br />
>If you want to keep quiet, use the `-s` flag to wait specified seconds between request. (example: -s 5)<br />
>You can now use `--scan` to discover open ports on discovered devices. (example: --scan 80 443)<br />
>Use the `-h` flag for usage reference in the script.

**The paramiko and netaddr modules are required for this script to work!** <br />
You can install them with the pip tool:
`pip install netaddr paramiko`

![example](https://github.com/Xeonrx/Puwr/blob/main/img/example.PNG)
>Here I scanned devices and checked which ones has port 80 and 443 open to target web applications.<br />
>Notice how the TTL number also displays, giving you a hint at what the device may be running on.

# Tested Operating Systems
So far, I have only confirmed Puwr to work on a few operating systems:
- Kali Linux
- Parrot OS
- Windows 10

However, it should work on almost any OS with Python, and the needed modules installed.

# Port Scanning
As mentioned earlier a few times, you can now not only discover hosts, but also scan them for open ports.<br />
This can be used to find an attack vector on devices running an accessable service. By default, ports will not
be scanned, but you can use the `--scan` flag, and add the port numbers you'd like to scan.<br />
Keep in mind however, that port scanning does take a good bit of additional time to complete.
**PORT SCANNING ONLY WORKS ON MACHINES WITH PYTHON 3 INSTALLED FOR NOW**

# Showcases
Here are some sources that have showcased Puwr, and I wanted to give a thanks to them!</br>
- https://www.kitploit.com/2022/06/puwr-ssh-pivoting-script-for-expanding.html
- https://www.handla.it/ssh-pivoting-script-for-increasing-assault-surfaces-on-native-networks/
- https://haxf4rall.com/2022/06/06/puwr-ssh-pivoting-script-for-expanding-attack-surfaces-on-local-networks/

# Disclaimer
Note this script is purley just a small enumeration script, and does not directly attack any found devices on the network.
Wether you decide to remain persistence on the machine and use it to attack other devices from it, is your choice.

I encourage you carry out these techniques with **permission**, and stay in the legal bound of things.
Cyber attacks are highly illegal, and no one but you is responsible for any crime.

# License
Puwr uses the MIT License. You can read about it here:
```
MIT License

Copyright (c) 2022 ciiphys

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
