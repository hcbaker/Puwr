# Puwr
![icon](https://github.com/Xeonrx/Puwr/blob/main/img/icon.PNG)
![stars](https://img.shields.io/github/stars/Xeonrx/Puwr?style=social)
![forks](https://img.shields.io/github/forks/Xeonrx/Puwr?style=social)
![watching](https://img.shields.io/github/watchers/Xeonrx/Puwr?style=social) <br />
Easily expand your attack surface on a local network by discovering more hosts, via SSH.


Using a machine running a SSH service, Puwr uses a given subnet range to scope out IP's, sending back any successful ping requests it has.
This can be used to expand out an attack surface on a local network, by returning you hosts you couldn't normally reach from your own device.


*(example below of how Puwr handles requests)*
![LogoImage](https://github.com/Xeonrx/Puwr/blob/main/img/diagram.PNG)

# Usage
Puwr is simple to run, only requiring 4 flags: <br />
`python3 puwr.py (MACHINE IP) (USER) (PASSWORD) (SUBNET VALUE)`


example: <br />
`python3 puwr.py 10.0.0.53 xeonrx password123 10.0.0.1/24`


>If you need to connect through a port other than 22, use the `-p` flag. (example: -p 2222)<br />
>If you want to keep quiet, use the `-s` flag to wait specified seconds between request.  (example: -s 5)<br />
>Use the `-h` flag for usage reference in the script.

**The paramiko and netaddr modules are required for this script to work!** <br />
You can install them with the pip tool: <br />
`pip install netaddr paramiko`

![example](https://github.com/Xeonrx/Puwr/blob/main/img/example.PNG)

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
