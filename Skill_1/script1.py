from netmiko import ConnectHandler

my_device = {
    'device_type': 'juniper',
    'ip': '10.123.10.195',
    'username': 'okan',
    'password': 'Welkom@1234',
    'port': 22
}

conn = ConnectHandler(**my_device)

my_list_of_configs = [
    "set system host-name R1-UPDATED",
    "set snmp community OKAN",
    "commit"
]

result = conn.send_config_set(config_commands=my_list_of_configs)

print(result)

conn.disconnect()
