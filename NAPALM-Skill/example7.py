from napalm import get_network_driver
from rich import print as rprint
import yaml

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
    results = device.compliance_report("R1-validate.yaml")

    rprint(results)
