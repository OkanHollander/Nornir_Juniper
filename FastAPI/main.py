from fastapi import FastAPI
from nornir import InitNornir
import yaml

nr = InitNornir(config_file="config.yaml")

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/inventory")
async def inventory():
    return nr.inventory.hosts

@app.get("/all_vars")
async def get_all_vars():
    with open("group_vars/snmp/juniper.yaml", "r", encoding='utf-8') as file:
        all_vars = yaml.safe_load(file)
    return {"all_vars": all_vars}

@app.get("/devinfo")
async def get_dev_info():
    with open("hosts.yaml", "r", encoding='utf-8') as file:
        dev_info = yaml.safe_load(file)
    return {"dev_info": dev_info}
