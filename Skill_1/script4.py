from scrapli import Scrapli

my_device = {
    "host": "10.123.10.195",
    "auth_username": "okan",
    "auth_password": "Welkom@1234",
    "auth_strict_key": False,
    "platform": "juniper_junos",
}


conn = Scrapli(**my_device)

conn.open()
my_configs = [
    "set system host-name R1-PIZZA",
    "commit"
]

# result = conn.send_configs(my_configs)
result = conn.send_configs_from_file("R1.cfg")

print(result.result)

conn.close()
