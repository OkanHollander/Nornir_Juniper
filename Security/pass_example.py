import getpass
from netmiko import ConnectHandler
from rich import print as rprint

my_pass = getpass.getpass("Enter your password: ")

with ConnectHandler(device_type="juniper",
                    host="10.123.10.195",
                    username="okan",
                    password=my_pass,
                    port=22) as ssh:
    result = ssh.send_command("show version")
    rprint(result)
