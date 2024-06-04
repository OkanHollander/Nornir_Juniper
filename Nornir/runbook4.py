from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def pull_some_data(task):
    task.run(task=napalm_get, getters=["environment"])

result = nr.run(task=pull_some_data)
print_result(result)
