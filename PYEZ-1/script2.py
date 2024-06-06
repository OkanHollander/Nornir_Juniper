from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
import sys
import getpass
from rich import print as rprint
from lxml import etree

my_pass = getpass.getpass()

device = Device(host="10.123.10.195", user="okan", passwd=my_pass)
try:
    device.open()
except ConnectError as e:
    print(e)
    sys.exit(1)
except Exception as e:
    print(e)
    sys.exit(1)

response = device.rpc.get_interface_information()
print(etree.tostring(response, pretty_print=True).decode())
