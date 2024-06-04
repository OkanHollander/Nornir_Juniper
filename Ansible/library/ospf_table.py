from ansible.module_utils.basic import AnsibleModule
import json
from scrapli import Scrapli
from rich import print as rprint
from tabulate import tabulate
import itertools


def connect_junos(device_ip):
    device = {
        "host": device_ip,
        "auth_username": "okan",
        "auth_password": "Welkom@1234",
        "auth_strict_key": False,
        "platform": "juniper_junos",
    }
    conn = Scrapli(**device)
    conn.open()
    result = conn.send_command("show configuration | display json")
    pretty_results = json.loads(result.result)

    return pretty_results


def parse_ospf(device_ip, result):
    print_list = []
    for area in result["configuration"]["protocols"]["ospf"]["area"]:
        area_name = area["name"]
        for interface in area["interface"]:
            interface_name = interface["name"]
            print_list.append(f"Interface: {interface_name}, Area: {area_name}")
    table = itertools.zip_longest(print_list)
    return tabulate(table, headers=[f"{device_ip}"], tablefmt="psql")


def main():
    data_fields = {"ip": {}}
    module = AnsibleModule(argument_spec=data_fields)
    device_ip = module.params["ip"]
    pretty_result = connect_junos(device_ip)
    table_result = parse_ospf(device_ip, pretty_result)

    module.params.update({"result": table_result})
    module.params.pop("ip")

    module.exit_json(data=module.params)


if __name__ == "__main__":
    main()
