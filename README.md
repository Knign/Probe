````
██████╗ ██████╗  ██████╗ ██████╗ ███████╗
██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔════╝
██████╔╝██████╔╝██║   ██║██████╔╝█████╗  
██╔═══╝ ██╔══██╗██║   ██║██╔══██╗██╔══╝  
██║     ██║  ██║╚██████╔╝██████╔╝███████╗
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝                                         
````

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
## Examples
### Scanning an IP address:
```
python3 probe.py 127.0.0.1
```
### Scanning the first 100 ports for an IP address:
```
python3 probe.py 127.0.0.1 -p 1-100
```
### Creating 100 threads simultaneously:
```
python3 probe.py 127.0.0.1 -t 100
```
