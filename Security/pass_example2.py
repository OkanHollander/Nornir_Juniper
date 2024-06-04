import getpass
from netmiko import ConnectHandler
from rich import print as rprint
import os

my_pass = os.environ.get("MYPASSWORD")
my_user = os.environ.get("MYUSERNAME")

with ConnectHandler(device_type="juniper",
                    host="10.123.10.195",
                    username=my_user,
                    password=my_pass,
                    port=22) as ssh:
    result = ssh.send_command("show version")
    rprint(result)
