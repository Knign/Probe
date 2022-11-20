#!/usr/bin/python3

from socket import *
import sys
import time
startTime = time.time()

host = input("Enter a remote host to scan: ")
hostIP = gethostbyname(host)
print ("Please wait, scanning remote host", hostIP)

def printServiceOnPort(port, protocol):
    for port in range(1, 5000):
        s = socket(AF_INET, SOCK_STREAM)
        setdefaulttimeout(1)

        if s.connect_ex((hostIP, port)) == 0:
            serviceName = getservbyport(port, protocol);
            print("Port number %d : %s" % (port, serviceName));

printServiceOnPort(21, "tcp");
printServiceOnPort(105, "tcp");
printServiceOnPort(80, "tcp");
printServiceOnPort(443, "tcp");
printServiceOnPort(20, "udp");
printServiceOnPort(21, "udp");

print('Scanning Completed in ', time.time() - startTime)
