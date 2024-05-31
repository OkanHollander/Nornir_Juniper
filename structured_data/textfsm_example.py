from netmiko import ConnectHandler
from rich import print as rprint
import xmltodict

my_device = {
    "host": "10.123.10.195",
    "username": "okan",
    "password": "Welkom@1234",
    "device_type": "juniper_junos",
    "port": 22,}

with ConnectHandler(**my_device) as ssh:
    ssh.enable()
    output = ssh.send_command(command_string="show interfaces", use_textfsm=True)
    
rprint(output)
