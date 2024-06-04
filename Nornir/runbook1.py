from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

def get_some_stuff(task):
    result = task.run(task=netmiko_send_command, command_string="show version")
    print(result.result)

result = nr.run(task=get_some_stuff)
rprint(result)
