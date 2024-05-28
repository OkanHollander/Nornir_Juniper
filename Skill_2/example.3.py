import yaml
from rich import print as rprint

my_data = yaml.safe_load(open("hosts.yaml", "r", encoding="UTF-8"))

rprint(my_data["device"])
