from napalm import get_network_driver
from rich import print as rprint

juniper_device = get_network_driver('junos')

my_device = {
    "host": "10.123.10.195",
    "auth_username": "okan",
    "auth_password": "Welkom@1234",}

with juniper_device(
    hostname=my_device["host"],
    username=my_device["auth_username"],
    password=my_device["auth_password"],
) as device:
    results = device.get_config()

rprint(results['running'])
