from netmiko import ConnectHandler

my_device = {
    'device_type': 'juniper',
    'ip': '10.123.10.195',
    'username': 'okan',
    'password': 'Welkom@1234',
    'port': 22
}

conn = ConnectHandler(**my_device)

result = conn.send_config_from_file(config_file="R1.cfg")

print(result)

conn.disconnect()
