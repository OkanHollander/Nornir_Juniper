from nornir import InitNornir
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

rprint(nr.inventory.hosts['R1'].password)
