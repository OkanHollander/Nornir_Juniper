import json
from rich import print as rprint

my_json_data = '{"name": "John","age": 30}'

my_dict = json.loads(my_json_data)

rprint(my_dict['name'])