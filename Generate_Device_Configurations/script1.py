import yaml
from jinja2 import Environment, FileSystemLoader
from inventory import DEVICES
from rich import print as rprint
from netmiko import ConnectHandler


def generate_config(device_name):
    yaml_data = yaml.safe_load(
        open(f"host_vars/{device_name}.yaml", "r", encoding="UTF-8")
    )
    env = Environment(
        loader=FileSystemLoader("templates"), trim_blocks=True, lstrip_blocks=True
    )
    template = env.get_template("config.j2")
    configuration = template.render(yaml_data)
    rprint(f"Connecting to device: {device_name}")
    return configuration.splitlines()


def configure_device(hostname, configuration):
    with ConnectHandler(
        device_type="juniper",
        host=hostname,
        username="okan",
        password="Welkom@1234",
        port=22,
    ) as conn:
        results = conn.send_config_set(config_commands=configuration)
        print(results)


def main():
    for device in DEVICES:
        device_name = device["device_name"]
        hostname = device["hostname"]

        configuration = generate_config(device_name)
        configure_device(hostname, configuration)


if __name__ == "__main__":
    main()
