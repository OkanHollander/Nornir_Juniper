from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

def get_some_stuff(task):
    """
    This function retrieves the output of the 'how version' command from a network device.

    Parameters:
    task (nornir.core.task.Task): The Nornir task object representing the current device.

    Returns:
    None: The function prints the output of the 'how version' command to the console.
    """
    result = task.run(task=netmiko_send_command, command_string="show configuration")
    # print(result.result)

final_result = nr.run(task=get_some_stuff)
print_result(final_result)
