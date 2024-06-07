import yaml
from jinja2 import Environment, FileSystemLoader
from scrapli import Scrapli
from scrapli.response import MultiResponse
from typing import List

from inventory import DEVICES


def create_config(hostname: str) -> list[str]:
    """
    Generates a configuration for a network device based on a Jinja2 template and YAML data.

    This function reads YAML data from a file corresponding to the given hostname,
    uses a Jinja2 template to render the configuration, and splits the rendered
    configuration into a list of commands.

    Parameters:
    hostname (str): The hostname of the network device. This is used to locate the corresponding YAML file.

    Returns:
    list[str]: A list of configuration commands generated from the template and YAML data.
    """
    yaml_data = yaml.safe_load(
        open(f"host_vars/{hostname}.yaml", "r", encoding="UTF-8")
    )
    env = Environment(
        loader=FileSystemLoader("templates"), trim_blocks=True, lstrip_blocks=True
    )
    template = env.get_template("config.j2")
    my_config = template.render(yaml_data)
    configuration = my_config.split("\n")

    return configuration


def send_configuration(host: str, configuration: List[str]) -> MultiResponse:
    """
    This function establishes a connection to a network device using Scrapli,
    sends a configuration to the device, and returns the response.

    Parameters:
    host (str): The hostname or IP address of the network device.
    configuration (List[str]): A list of configuration commands to be sent to the device.

    Returns:
    MultiResponse: The response from the network device after sending the configuration.

    Raises:
    ScrapliException: If there is an error establishing a connection or sending the configuration.
    """
    with Scrapli(
        host=host,
        auth_username="okan",
        auth_password="Welkom@1234",
        auth_strict_key=False,
        platform="juniper_junos"
    ) as conn:
        response = conn.send_configs(configs=configuration)
        return response


def main() -> None:
    """
    Main function to generate and send configuration to network devices.

    This function iterates over a list of devices defined in the DEVICES variable,
    generates the configuration for each device using the create_config function,
    sends the configuration to the device using the send_configuration function,
    and prints the result of the configuration deployment.

    Parameters:
    None

    Returns:
    None
    """
    for device in DEVICES:
        hostname = device["hostname"]
        host = device["host"]
        configuration = create_config(hostname)
        result = send_configuration(host, configuration)
        print(result.result)

if __name__ == "__main__":
    main()
