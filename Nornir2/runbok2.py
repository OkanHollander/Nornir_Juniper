from nornir import InitNornir
from nornir_utils.plugins.tasks.data import load_yaml
import ipdb

nr = InitNornir(config_file="config.yaml")

def load_juniper_snmp_data(task):
    juniper_snmp_data = task.run(task=load_yaml, file=f"./group_vars/snmp/juniper.yaml")
    task.group["snmp_vars"] = juniper_snmp_data.result

nr.run(task=load_juniper_snmp_data)
ipdb.set_trace()
