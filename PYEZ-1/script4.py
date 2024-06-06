from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
import sys
from getpass import getpass
from rich import print as rprint
from lxml import etree
import xmltodict

my_pass = getpass()

device = Device(host="10.123.10.195", user="okan", passwd=my_pass)
try:
    device.open()
except ConnectError as e:
    print(e)
    sys.exit(1)
except Exception as e:
    print(e)
    sys.exit(1)

response = device.rpc.get_ospf_overview_information()
rprint(etree.tostring(response, pretty_print=True).decode())
ospf_router_id = response.find(".//ospf-router-id").text
ospf_area =response.find(".//ospf-area").text
rprint(f"The ospf area is {ospf_area} and the router id is {ospf_router_id}")
