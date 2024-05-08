#A program to make a tcp server running and listening to a port number
import argparse
import socket
import threading

#client request
def serverclient(clienttoserve,clientipaddress,portnumber):
    clientrequest = clienttoserve.recv(4096)
    print "Received data from client %s:%d"%(clientipaddress,portnumber,clientrequest)

    clienttoserve.send("I am server response")
    clienttoserve.close()


#starting the server
def startserver(portnumber):
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("0.0.0.0",portnumber))         #server is in the listening mode
    server.listen(10)  #listen for 10 connections
    print "Listening on port number %d"%portnumber
    while True:
        client,address=server.accept()
        print "Connected with client %s:%d" %(address[0],address[1])
        serverclientthread=threading.Thread(target=serverclient,args=(client,address[0],address[1]))
        serverclientthread.start()
        exit(0)

#main program with argument parsing
def main():
    parser = argparse.ArgumentParser('TCP Server program')
    parser.add_argument("-p","--port", type=int, help="The port number to connec with",default=4444)
    args = parser.parse_args()
    por = args.port
    startserver(por)


if __name__ == "__main__":
    main()
