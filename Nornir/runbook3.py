from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result
import json
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

def get_config_interfaces(task):
    configuration = task.run(task=netmiko_send_command,
             command_string="show configuration interfaces | display json")
    dict_configuration = json.loads(configuration.result)

    interfaces = dict_configuration["configuration"]["interfaces"]["interface"]
    for interface in interfaces:
        target_interface = interface["name"]
        unit = interface["unit"]
        for element in unit:
            names = element['family']['inet']['address']
            for name in names:
                ip_address = name["name"]
        rprint(f"{target_interface} {ip_address}")


result = nr.run(task=get_config_interfaces)
# print_result(result)
