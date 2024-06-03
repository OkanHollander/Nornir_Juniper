from netmiko import ConnectHandler
from rich import print as rprint
from inventory import DEVICES


def configure_devices(hostname):
    my_list_configs = [
        "set snmp community BLAHBLAHBLAH",
        "set snmp community BLAH2",
    ]
    with ConnectHandler(
        device_type="juniper",
        host=hostname,
        username="okan",
        password="Welkom@1234",
        port=22,
    ) as conn:
        conn.send_command(command_string="request system configuration rescue save")


def main():
    for device in DEVICES:
        hostname = device["hostname"]
        configure_devices(hostname)


main()
