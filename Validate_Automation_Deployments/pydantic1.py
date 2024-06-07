from pydantic import BaseModel
from typing import List


class Ospfinfo(BaseModel):
    interface: str
    area: str


class Ospf(BaseModel):
    router_id: str
    interfaces: List[Ospfinfo]


class Data(BaseModel):
    ospf: Ospf


class NetworkData(BaseModel):
    data: Data
