# python test.py any_mode_description any_location_description
# e.g. python test.py wired|phone|exdata site-01-sw01|floor1|outdoor

import sys, time, wmi, ping3, requests, speedtest
from colorist import Color

start_time = time.time()
date = time.strftime("%Y%m%d")
with open(f'results_{date}.log', 'a') as f:
    # Redirect stdout to both the console and the file
    class MultiFile(object):
        def __init__(self, *files):
            self.files = files
        def write(self, text):
            for file in self.files:
                file.write(text)
    sys.stdout = MultiFile(sys.stdout, f)

    print('-'*25, time.strftime("%Y-%m-%d %H:%M"), '-'*25)
    mode = str(sys.argv[1])
    print(f'Test Mode: {mode}')
    location = str(sys.argv[2])
    print(f'Switch/Location: {location}')

    host_dict = {
        'Primary Data Center IP (1): ': 'x.x.x.x',
        'Primary Data Center IP (2): ': 'x.x.x.x',
        'Secondary Data Center IP (1): ': 'x.x.x.x',
        'Secondary Data Center IP (2): ': 'x.x.x.x',
        }

    # Get IP Address, Subnet Mask and Default Gateway
    wmi_interface = wmi.WMI()
    network_interface = wmi_interface.Win32_NetworkAdapterConfiguration(IPEnabled=True)[0]
    ip_address = network_interface.IPAddress[0]
    print(f'IP Address: {ip_address}')
    subnet_mask = network_interface.IPSubnet[0]
    print(f'Subnet Mask: {subnet_mask}')
    nidg = network_interface.DefaultIPGateway
    for gw in nidg:
        host_dict[f'Default Gateway ({nidg.index(gw)}): '] = str(gw)
        print(f'Default Gateway ({nidg.index(gw)}): {gw}')
    for dns in network_interface.DNSServerSearchOrder:
        print(f'DNS Server: {dns}')

    # Ping Tests
    print('Pinging....')
    host_items = host_dict.items()
    for key,value in host_items:
        ping_result = ping3.ping(value)
        print(f'Ping {key} {value} :', 'PASSED' if type(ping_result) is float else f'{Color.RED}FAILED{Color.OFF}')

    # HTTP Tests
    print('Checking Websites...')
    for url in [
        "Enter internal website here",
        "https://www.google.com",
        "https://www.bing.com",
        "https://www.cisco.com",
        "https://www.gambling.com"
        ]:
        try:
            response = requests.get(url)
            result = 'PASSED' if response.status_code == 200 else 'FAILED'
        except:
            result = 'FAILED'
        print(f'{url}: ', f'{Color.RED}FAILED{Color.OFF}' if result == 'FAILED' else result)

    # Speedtest
    print('Running Speedtest...')
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # convert to Mbps
    upload_speed = st.upload() / 1_000_000  # convert to Mbps
    latency = st.results.ping
    source_ip = st.results.client['ip']
    isp = st.results.client['isp']
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Latency: {latency:.2f} ms")
    print(f"Source IP Address: {source_ip}")
    print(f"ISP: {isp}")

    print(f'Completed in {round(time.time() - start_time)} seconds.')

# Restore stdout to its original value
sys.stdout = sys.__stdout__