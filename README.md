# ping-url-speedtest
Python script to run ping tests after getting own IP address info on Windows machine, check URL status codes if 200 and run internet speed test using speedtest-cli.

## Installation

### Git clone code
```
git clone https://github.com/onismo/ping-url-speedtest.git test
```

### Create virtual environment, activate then install requirements.txt
```
cd test
python -m venv .venv
.venv\Scripts\activate
(.venv) pip install -r requirements.txt
```

### Edit test.py to add IP addresses that you want to ping and URL's that you want to check.
```
    host_dict = {
        'Primary Data Center IP (1): ': 'x.x.x.x',
        'Primary Data Center IP (2): ': 'x.x.x.x',
        'Secondary Data Center IP (1): ': 'x.x.x.x',
        'Secondary Data Center IP (2): ': 'x.x.x.x',
        }
        
    for url in [
        "Enter internal website here",
        "https://www.google.com",
        "https://www.bing.com",
        "https://www.cisco.com",
        "https://www.gambling.com"
        ]:
```

### Run program
#### python test.py any_mode_description any_location_description
#### Example
```
python test.py Wired Switch1
```
#### Sample console output, also outputs to a file named results_20230504.log
```
------------------------- 2023-05-04 14:54 -------------------------
Test Mode: Wired
Switch/Location: Switch1
IP Address: 10.0.0.20
Subnet Mask: 255.255.255.0
Default Gateway (0): 10.0.0.1
Default Gateway (1): 192.168.0.1
DNS Server: 10.0.0.5
DNS Server: 10.0.0.6
Ping Primary Data Center IP (1):  10.0.0.7 : PASSED
Ping Primary Data Center IP (2):  10.0.0.8 : PASSED
Ping Secondary Data Center IP (1):  10.0.0.9 : PASSED
Ping Secondary Data Center IP (2):  10.0.0.10 : PASSED
Ping Default Gateway (0):  10.0.0.1 : PASSED
Ping Default Gateway (1):  192.168.0.1 : FAILED
Checking Websites...
http://app.internalwebsite.com:  PASSED
https://www.google.com:  PASSED
https://www.bing.com:  PASSED
https://www.cisco.com:  PASSED
https://www.gambling.com:  FAILED
Running Speedtest...
Download Speed: 77.53 Mbps
Upload Speed: 10.94 Mbps
Latency: 23.23 ms
Source IP Address: 68.78.98.108
ISP: Comcast Cable
Completed in 46 seconds.
```
