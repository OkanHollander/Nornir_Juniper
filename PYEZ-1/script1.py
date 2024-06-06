from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from rich import print as rprint
import getpass
import sys


device = Device(host="10.123.10.195", user="okan", passwd="Welkom@1234")
try:
    device.open()
except ConnectError as e:
    print(e)
    sys.exit(1)
except Exception as e:
    print(e)
    sys.exit(1)

response = device.facts
# rprint(response.keys())
rprint(f"The device hostname is {response['hostname']}")
rprint(f"The serial number is {response['serialnumber']}")
rprint(f"The version of the device is {response['version']}")
