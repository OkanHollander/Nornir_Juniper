import yaml
from jinja2 import Environment, FileSystemLoader
from inventory import DEVICES
from rich import print as rprint


def generate_config(device_name):
    yaml_data = yaml.safe_load(
        open(f"host_vars/{device_name}.yaml", "r", encoding="UTF-8")
    )
    env = Environment(loader=FileSystemLoader("templates"), 
                      trim_blocks=True,
                      lstrip_blocks=True)
    template = env.get_template(f"config.j2")
    configuration = template.render(yaml_data)
    rprint(f"Connecting to device: {device_name}")
    rprint(configuration)


def main():
    for device in DEVICES:
        device_name = device["device_name"]
        generate_config(device_name)


if __name__ == "__main__":
    main()
