from nornir import InitNornir
from nornir_utils.plugins.tasks.data import load_yaml
import ipdb

nr = InitNornir(config_file="config.yaml")


def load_my_ospf_vars(task):
    ospf_host_data = task.run(task=load_yaml, file=f"./host_vars/ospf/{task.host}.yaml")
    task.host["host_vars"] = ospf_host_data.result

nr.run(task=load_my_ospf_vars)
ipdb.set_trace()
