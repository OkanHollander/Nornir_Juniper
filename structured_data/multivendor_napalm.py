from netmiko import ConnectHandler
from napalm import get_network_driver
from rich import print as rprint
from devices import DEVICES


def connect_juniper(hostname, username, password):
    juniper_device = get_network_driver("junos")
    with juniper_device(hostname=hostname, username=username, password=password) as device:
        device.open()
        output = device.get_facts()
    getter_parser_printer(output)


def connect_cisco(hostname, username, password):
    cisco_device = get_network_driver("ios")
    with cisco_device(hostname=hostname, username=username, password=password) as device:
        device.open()
        output = device.get_facts()
    getter_parser_printer(output)


def getter_parser_printer(result):
    hostname = result['hostname']
    serial_number = result['serial_number']
    vendor = result['vendor']
    uptime = result['uptime']
    rprint(f"{hostname} ({serial_number}/{vendor}) has an uptime of {uptime}")


def main():
    for device in DEVICES:
        hostname = device['hostname']
        username = device['username']
        password = device['password']
        platform = device['platform']
        if platform == 'juniper':
            connect_juniper(hostname, username, password)
        elif platform == 'cisco':
            connect_cisco(hostname, username, password)
        else:
            rprint(f"Unknown platform: {platform}")


if __name__ == "__main__":
    main()
