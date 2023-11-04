# Threaded Port Scanner
Portscanner that implements multithreading for swift scans.

## Usage
```
probe.py [HOST]

    Arguments:
        [HOST]                      Address of host to be scanned
    
    Options:
        -p, --ports <int>-<int>     Range of ports to be scanned (default: 1-1036)
        -t, --threads <int>         Number of threads to be created (default: 50)
```
