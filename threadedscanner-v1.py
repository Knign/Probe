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

#Scanning ports
def portScan(port):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        setdefaulttimeout(1)

        # Checking if port is open
        # s.connect_ex() returns an error instead of raising exception
        if s.connect_ex((host, port)) == 0:
            return True
        s.close()

    except KeyboardInterrupt:
        return False
    except gaierror:
        return False
    except error:
        return False

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

for t in range(500):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

# Printing time required for process to complete
print('Scanning Completed in ' + str(time.time() - startTime) + ' seconds')