from nornir import InitNornir

nr = InitNornir(config_file="config.yaml")

def print_me(task):
    print(f"{task.host} is in ASN {task.host.data['bgp']['asn']}")

nr.run(task=print_me)
