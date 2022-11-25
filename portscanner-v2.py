from socket import *
import sys
import time

# Getting input from user
host = input("Enter a remote host to scan: ")
hostIP = gethostbyname(host)
print ("Please wait, scanning remote host", hostIP)

# Finding the services
def printServiceOnPort(port, protocol):

    # Obtaining time since epoch
    startTime = time.time()

    try:
        for port in range(1, 200):
            s = socket(AF_INET, SOCK_STREAM)
            setdefaulttimeout(1)

            if s.connect_ex((hostIP, port)) == 0:
                serviceName = getservbyport(port, protocol);
                print("Port " + str(port) + " : " + serviceName);

    except KeyboardInterrupt:
        print("\nExiting Program")
        sys.exit()
    except socket.gaierror:
        print("\nHostname Could Not Be Resolved")
        sys.exit()
    except socket.error:
        print("\nServer not responding")
        sys.exit()

    # Printing time required for process to complete
    print('Scanning Completed in ' + time.time() - startTime + " seconds")

printServiceOnPort(21, "tcp");
printServiceOnPort(105, "tcp");
printServiceOnPort(80, "tcp");
printServiceOnPort(443, "tcp");
printServiceOnPort(20, "udp");
printServiceOnPort(21, "udp");