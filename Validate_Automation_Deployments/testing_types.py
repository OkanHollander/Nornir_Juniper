import yaml
from jinja2 import Environment, FileSystemLoader
from scrapli import Scrapli

from inventory import DEVICES


def create_config(hostname):
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


def send_configuration(host, configuration):
    with Scrapli(
        host=host,
        auth_username="okan",
        auth_password="Welkom@1234",
        auth_strict_key=False,
        platform="juniper_junos"
    ) as conn:
        response = conn.send_configs(configs=configuration)
        return response


def main():
    for device in DEVICES:
        hostname = device["hostname"]
        host = device["host"]
        configuration = create_config(hostname)
        result = send_configuration(host, configuration)
        print(result.result)

if __name__ == "__main__":
    main()
