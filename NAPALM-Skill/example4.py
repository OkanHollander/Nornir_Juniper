from napalm import get_network_driver

juniper_device = get_network_driver('junos')

my_device = {
    "host": "10.123.10.195",
    "auth_username": "okan",
    "auth_password": "Welkom@1234",
}

with juniper_device(
    hostname=my_device["host"],
    username=my_device["auth_username"],
    password=my_device["auth_password"],
) as device:
    device.load_merge_candidate(config="set snmp community public")
    device.load_merge_candidate(filename="snmp-update.cfg")
    # device.commit_config()

    compare_result = device.compare_config()
    if compare_result:
        print(compare_result)

        answer = input("Do you want to commit the changes? [y/n]: ")
        while answer not in ["y", "n"]:
            print("Please enter y or n")
            answer = input("Do you want to commit the changes? [y/n]: ")

        if answer == "y":
            device.commit_config()
            print("Changes are committed")
        elif answer == "n":
            print("Changes are not committed")
    else:
        print("There are no differences between the running config and the candidate config")
