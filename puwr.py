import argparse, os, sys

parser = argparse.ArgumentParser(description="Puwr usage")
parser.add_argument("host",type=str,help="Targeted host")
parser.add_argument("username",type=str,help="SSH username")
parser.add_argument("password",type=str,help="SSH password")
parser.add_argument("iprange",type=str,help="subnet range")
parser.add_argument("-p","--port",type=int,help="Port number (22 default)")
parser.add_argument("-s","--seconds",type=int,help="Seconds between requests")
args = parser.parse_args()

if __name__ == "__main__":
    sys.path.append(f'{os.path.abspath(os.getcwd())}/source')
    import client, main
    port = 22 if not args.port else args.port
    seconds = 0 if not args.seconds else args.seconds

    ssh = client.connect(args.host,args.username,args.password,port) # sets connection with machine via SSH
    main.puwr(ssh,seconds,args.iprange) # starts program


# Author: Xeonrx
# Source: https://github.com/Xeonrx/Puwr
# License: MIT License

# Only you are responsible for the use of this script!
