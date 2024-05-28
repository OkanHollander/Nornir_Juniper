from netmiko import ConnectHandler
from my_devices import INVENTORY

for device in INVENTORY:
    conn = ConnectHandler(
        device_type=device["platform"],
        ip=device["host"],
        username=device["username"],
        password=device["password"],
        port=device["port"],
    )

    result = conn.send_command("show version")
    print(result)

    conn.disconnect()
