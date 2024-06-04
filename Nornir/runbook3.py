from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result
import json
from nornir.core.task import Result
import logging

nr = InitNornir(config_file="config.yaml")

def get_config_interfaces(task):
    configuration = task.run(task=netmiko_send_command,
                             severity_level=logging.DEBUG,
             command_string="show configuration interfaces | display json")
    dict_configuration = json.loads(configuration.result)

    interfaces = dict_configuration["configuration"]["interfaces"]["interface"]
    result_list = []

    for interface in interfaces:
        target_interface = interface["name"]
        unit = interface["unit"]
        for element in unit:
            names = element['family']['inet']['address']
            for name in names:
                ip_address = name["name"]
        result_list.append(f"{target_interface} {ip_address}")
    return Result(host=task.host, result=result_list)


result = nr.run(task=get_config_interfaces)
print_result(result)
