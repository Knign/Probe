from socket import *
import sys
import time
import argparse

parser = argparse.ArgumentParser(description="Simple port scanner")

# Obtaining the host
parser.add_argument("host", help="Host to scan.")

# Obtaining the port range
# If no arguments are parsed, the default port range (1-65535) is selected
parser.add_argument("--ports", "-p", dest="port_range", default="1-65535", help="Port range to scan, default is 1-65535 (all ports)")

args = parser.parse_args()
host, port_range = args.host, args.port_range

print("Please wait, scanning remote host", host)

# Obtaining starting port and ending port from range
start_port, end_port = port_range.split("-")
start_port, end_port = int(start_port), int(end_port)

# Obtaining time since epoch
startTime = time.time()

# Finding the services
def printServiceOnPort(protocol):
    # Obtaining time since epoch
    startTime = time.time()

    try:
        # Working through the port range
        for port in range(start_port, end_port):
            s = socket(AF_INET, SOCK_STREAM)
            setdefaulttimeout(1)

            # Checking if port is open
            # s.connect_ex() returns an error instead of raising exception
            if s.connect_ex((host, port)) == 0:

                # Obtaining the service running on the port
                serviceName = getservbyport(port, protocol);
                print("Port " + str(port) + " : " + serviceName);

    except KeyboardInterrupt:
        print("\nExiting Program")
        sys.exit()
    except gaierror:
        print("\nHostname Could Not Be Resolved")
        sys.exit()
    except error:
        print("\nServer not responding")
        sys.exit()

printServiceOnPort(21, "tcp");
printServiceOnPort(105, "tcp");
printServiceOnPort(80, "tcp");
printServiceOnPort(443, "tcp");
printServiceOnPort(20, "udp");
printServiceOnPort(21, "udp");

# Printing time required for process to complete
print('Scanning Completed in ' + str(time.time() - startTime) + " seconds")
