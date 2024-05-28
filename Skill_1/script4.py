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

result = conn.send_command("show interfaces terse")

print(result.result)

conn.close()
