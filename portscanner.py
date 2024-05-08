# A TCP client program to scan the ports that is running on a server. 
import argparse
from socket import *

def printBanner(connsock,targetport):
    try:
        if(targetport==80):
            connsock.send("GET HTTP/1.1 \r\n")
        else:
            connsock.send(("\r\n"))
        results = connsock.recv(4096)
        print " Banner: " + str(results)
    except:
        print "Banner not available"

def connscan(targethost,targetport):
    # Create the socket
    try:
        print"Went inside the program"
        connsock = socket(AF_INET,SOCK_STREAM)
        connsock.connect((targethost,targetport))
        print " %d tcp open"%targetport
        printBanner(connsock,targetport)
    except:
        print " %d tcp closed"%targetport
    finally:
        connsock.close()
        


def portscan(targethost,targetport):
    try:
        local_ip = gethostbyname(targethost)
    except:
        print " Host does not exist exiting the program"
        exit(0)
    try:
        name = gethostbyaddr(local_ip)
        print " scan result for  " + name[0] + "===="
    except:
        print "Scan result for " + local_ip + "====="
    setdefaulttimeout(10)

    for i in targetport:
        connscan(targethost,int(i))





def main():
    #parsing the arguments
    parser = argparse.ArgumentParser('Port scanner')
    parser.add_argument("-a","--address", type=str,help="target ip address")
    parser.add_argument("-p","--portnumber", type=str,help="target port number")
    args = parser.parse_args()
    ip=args.address
    port=args.portnumber.split(',')
    portscan(ip,port)
    



if __name__ == "__main__":
    main()
