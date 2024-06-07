from fastapi import FastAPI
from nornir import InitNornir
import yaml
from nornir_netmiko.tasks import netmiko_send_command

nr = InitNornir(config_file="config.yaml")

app = FastAPI()

@app.get("/")
async def root() -> dict:
    """
    Root endpoint that returns a simple greeting message.

    This function handles GET requests to the root URL ("/") of the FastAPI application.
    It returns a JSON response with a greeting message.

    Returns:
        dict: A dictionary containing a greeting message.
    """
    return {"message": "Hello World"}

@app.get("/inventory")
async def inventory():
    """
    Inventory endpoint that returns the hosts in the Nornir inventory.

    This function handles GET requests to the "/inventory" URL of the FastAPI application.
    It returns a JSON response containing the hosts from the Nornir inventory.

    Returns:
        dict: A dictionary containing the hosts in the Nornir inventory.
    """
    return nr.inventory.hosts

@app.get("/all_vars", tags=['variables'])
async def get_all_vars() -> dict:
    """
    Endpoint to retrieve all variables from a specific YAML file.

    This function handles GET requests to the "/all_vars" URL of the FastAPI application.
    It reads the contents of the "group_vars/snmp/juniper.yaml" file and returns them as a JSON response.

    Returns:
        dict: A dictionary containing all variables from the specified YAML file.
    """
    with open("group_vars/snmp/juniper.yaml", "r", encoding='utf-8') as file:
        all_vars = yaml.safe_load(file)
    return {"all_vars": all_vars}

@app.get("/devinfo", tags=['variables'])
async def get_dev_info() -> dict:
    """
    Endpoint to retrieve device information from a YAML file.

    This function handles GET requests to the "/devinfo" URL of the FastAPI application.
    It reads the contents of the "hosts.yaml" file and returns them as a JSON response.

    Returns:
        dict: A dictionary containing device information from the specified YAML file.
    """
    with open("hosts.yaml", "r", encoding='utf-8') as file:
        dev_info = yaml.safe_load(file)
    return {"dev_info": dev_info}


@app.get("/configurations", tags=['configurations'])
async def get_configurations():
    results = nr.run(task=netmiko_send_command, command_string="show configuration")
    return results
