from napalm import get_network_driver
from rich import print as rprint

juniper_device = get_network_driver("junos")
with juniper_device(
    hostname="10.123.10.195", username="okan", password="Welkom@1234"
) as conn:
    conn.load_replace_candidate(filename="R1.cfg")
    conn.commit_config(revert_in=60)
    rprint(conn.has_pending_commit())
    conn.commit_config()
    rprint(conn.has_pending_commit())
