from netmiko import ConnectHandler
from rich import print as rprint
from inventory import DEVICES


def configure_device(hostname):
    my_list_configs = [
        "set snmp community BLAHBLAHBLAH",
        "set snmp community BLAH2",
    ]
    with ConnectHandler(
        device_type="juniper",
        host=hostname,
        username="okan",
        password="Welkom@1234",
        port=22,
    ) as conn:
        conn.send_config_set(config_commands=my_list_configs)
        compare_results = conn.send_config_set(config_commands=["show | compare"])
        rprint(compare_results)


def rollback_device(hostname):
    with ConnectHandler(
        device_type="juniper",
        host=hostname,
        username="okan",
        password="Welkom@1234",
        port=22,
    ) as conn:
        rollback_results = conn.send_config_set(
            config_commands=["rollback 0", "commit confirmed 1", "commit"]
        )
        rprint(rollback_results)


def commit_device(hostname):
    with ConnectHandler(
        device_type="juniper",
        host=hostname,
        username="okan",
        password="Welkom@1234",
        port=22,
    ) as conn:
        commit_results = conn.send_config_set(
            config_commands=["commit confirmed 1", "commit"]
        )
        rprint(commit_results)


def main():
    for device in DEVICES:
        hostname = device["hostname"]
        configure_device(hostname)
    
    answer = input("Do you want to commit these changes? (y/n) ")
    while answer not in ["y", "n"]:
        print("Please enter y or n")
        answer = input("Do you want to commit these changes? (y/n) ")
        if answer == "y":
            for device in DEVICES:
                hostname = device["hostname"]
                commit_device(hostname)
        elif answer == "n":
            for device in DEVICES:
                hostname = device["hostname"]
                rollback_device(hostname)


if __name__ == "__main__":
    main()
