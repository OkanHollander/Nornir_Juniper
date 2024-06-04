from scrapli import Scrapli


def connect_junos(device_ip):
    device = {
        "host": device_ip,
        "auth_username": "okan",
        "auth_password": "Welkom@1234",
        "auth_strict_key": False,
        "platform": "juniper_junos",
    }
    conn = Scrapli(**device)
    conn.open()
    result = conn.send_command("show configuration")

    return result.result

result = connect_junos("10.123.10.195")
print(result)
