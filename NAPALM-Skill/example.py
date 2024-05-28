from napalm import get_network_driver
from rich import print as rprint

juniper_device = get_network_driver('junos')

my_device = juniper_device(
    hostname="10.123.10.195",
    username="okan",
    password="Welkom@1234",
)

my_device.open()

result = my_device.get_facts()

rprint(result)

my_device.close()
