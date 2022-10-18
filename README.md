
<p align="center">
 <img src="https://github.com/Xeonrx/Puwr/blob/main/img/icon.png" width=300 >
 </p>
<p align="center">
 <img src="https://img.shields.io/github/stars/Xeonrx/Puwr?style=social">
 <img src="https://img.shields.io/github/forks/Xeonrx/Puwr?style=social">
 <img src="https://img.shields.io/github/watchers/Xeonrx/Puwr?style=social">
 </p>
 <p align="center">
 <img src="https://img.shields.io/github/license/xeonrx/puwr">
 <img src="https://img.shields.io/badge/version-0.2.1-green">
 </p>
 <p align="center">
 <img src="https://github.com/Xeonrx/Puwr/blob/main/img/puwr.gif">
 </p>

## Contents
- [About Puwr](#puwr)
- [Puwr Usage](#usage)
- [Port scanning](#port-scanning)
- [Showcases](#showcases)
- [Disclaimer](#disclaimer)
- [Future](#future)

## Puwr
Easily expand your attack surface on a local network by discovering more hosts, via [SSH](https://en.wikipedia.org/wiki/Secure_Shell).
Using a machine running a SSH service, Puwr uses a given subnet range to scope out IP's, sending back any successful ping requests it has.
This can be used to create a [pivoting attack](https://www.geeksforgeeks.org/pivoting-moving-inside-a-network/) from a compromised machine, by returning you hosts you couldn't normally discover from your own device.
Open [ports](https://en.wikipedia.org/wiki/Port_(computer_networking)) can then be probed on these discovered devices, to find a gateway into attacking more devices.

Of course feel free to fill out an issue request if there are any apparent issues, or if functionality should be added.
  (https://github.com/Xeonrx/Puwr/issues)

# Usage
Puwr is simple to run, only requiring 4 flags: <br />
`python3 puwr.py (MACHINE IP) (SSH USER) (SSH PASSWORD) (SUBNET VALUE)`


example: <br />
`python3 puwr.py 10.0.0.53 xeonrx password123 10.0.0.1/24`


>If you need to connect through a port other than 22, use the `-p` flag. (example: -p 2222)<br />
>If you want to keep quiet, use the `-s` flag to wait specified seconds between requests. (example: -s 5)<br />
>You can use `--scan` to probe for open ports on discovered devices. (example: --scan 80 443)<br />
>Use the `-h` flag for usage reference in the script.

**The paramiko and netaddr modules are required for this script to work!** <br />
You can install them with the pip tool:
`pip install netaddr paramiko`

# Port Scanning
As mentioned earlier a few times, you can now not only discover hosts, but also scan them for open ports.<br />
This can be used to find an attack vector on devices running an accessable service. By default, ports will not
be scanned, but you can use the `--scan` flag, and add the port numbers you'd like to scan.<br />
Keep in mind however, that port scanning does take a good bit of additional time to complete.
**PORT SCANNING ONLY WORKS ON MACHINES WITH PYTHON 3 INSTALLED FOR NOW**

# Showcases
Here are a few of the many sources that have helped share Puwr with others, and I wanted to give a thanks to them!</br>
- https://www.kitploit.com/2022/06/puwr-ssh-pivoting-script-for-expanding.html
- https://www.handla.it/ssh-pivoting-script-for-increasing-assault-surfaces-on-native-networks/
- https://haxf4rall.com/2022/06/06/puwr-ssh-pivoting-script-for-expanding-attack-surfaces-on-local-networks/
>Extra thanks to the people who left a star on the repo. Every one is very appreciated :)

# Disclaimer
Note this script is purley just a small enumeration script, and does not directly attack any found devices on the network.
Wether you decide to remain persistence on the machine and use it to attack other devices from it, is your choice. Puwr
is designed to help aid you in pivoting, by purley discovering more targets for you to map out.

I encourage you carry out these techniques with **permission**, and stay in the legal bounds of things.
Unathorized cyber attacks are highly illegal, and no one but you is responsible for any crime!

# Future
This project is still in development, and is being worked on. My main objective as of right now, is to add minor features, and make the current
code more efficent/faster. Contributions are welcome to the project.
