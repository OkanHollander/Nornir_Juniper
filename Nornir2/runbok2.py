from nornir import InitNornir
from nornir_utils.plugins.tasks.data import load_yaml
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.tasks import print_result


nr = InitNornir(config_file="config.yaml")

def load_juniper_snmp_data(task):
    juniper_group_snmp_data = task.run(task=load_yaml, file=f"./group_vars/snmp/juniper.yaml")
    task.host["vars"] = juniper_group_snmp_data.result
    juniper_host_snmp_data = task.run(task=load_yaml, file=f"./host_vars/snmp/{task.host}.yaml")
    task.host["vars"].update(juniper_host_snmp_data.result)

def generate_config(task):
    snmp_template = task.run(task=template_file,
                             template="snmp.j2",
                             path=f"./templates/{task.host['vendor']}/")
    snmp_result = snmp_template.result
    snmp_config = snmp_result.splitlines()
    

load_results = nr.run(task=load_juniper_snmp_data)
config_results = nr.run(task=generate_config)

print_result(load_results)
print_result(config_results)
