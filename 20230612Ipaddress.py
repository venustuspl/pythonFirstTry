import ipaddress

a=ipaddress.ip_address('46.41.128.110')
a2=ipaddress.ip_address('192.168.1.1')
print(a.is_global)
print(a2.is_global)

for h in ipaddress.ip_network('192.168.2.0/24').hosts():
    print(h)