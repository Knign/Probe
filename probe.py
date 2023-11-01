from socket import *
import sys
import time
import argparse
import threading
from queue import Queue

queue = Queue()

parser = argparse.ArgumentParser(description="Simple port scanner")

# Obtaining the host
parser.add_argument("host", help="Host to scan.")

# Obtaining the port range
# If no arguments are parsed, the default port range (1-1023) is selected
parser.add_argument("-p", "--ports", dest="port_range", default="1-1023", help="Port range to scan, default is 1-65535 (all ports)")

# Obtain the number of threads
parser.add_argument("-t", "--threads", dest="threads", default=50, help="Specify Threads(Default 600 (MAX - 849))")

args = parser.parse_args()
host, port_range, threads = args.host, args.port_range, args.threads

print("Scanning remote host", host)

# Obtaining starting port and ending port from range
start_port, end_port = port_range.split("-")
start_port, end_port = int(start_port), int(end_port)

# Obtaining time since epoch
startTime = time.time()

#Scanning ports
def portScan(port):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        setdefaulttimeout(1)

        # Checking if port is open
        # s.connect_ex() returns an error instead of raising exception
        if s.connect_ex((host, port)) == 0:
            print("Port " + str(port) + " is open")
        s.close()

    except KeyboardInterrupt:
        print("\nExiting Program")
        sys.exit()
    except gaierror:
        print("\nHostname Could Not Be Resolved")
        sys.exit()
    except error:
        print("\nServer not responding")
        sys.exit()

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portScan(port):
            print("Port " + str(port) + " is open")

port_list = range(start_port, end_port)
fill_queue(port_list)

thread_list = []

for t in range(int(threads)):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

# Print time required for process to complete
print('Scanning Completed in ' + str(time.time() - startTime) + ' seconds')
