import ipaddress

net = ipaddress.ip_network("172.18.0.0/24")
for a in net:
    print(a)
net6 = ipaddress.ip_network('12:3456:78:90ab:cd:ef01:23:30/125')
for a in net6:
    print(a)
assert ipaddress.ip_address("172.18.0.120") in net
