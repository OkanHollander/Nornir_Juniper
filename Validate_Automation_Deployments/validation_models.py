from pydantic import BaseModel, Field
from ipaddress import IPv4Address


class BGP(BaseModel):
    ASN: int = Field(gt=0, le=65535)
    group: str = Field(min_length=1, max_length=64)
    type: str = "internal"
    peer: IPv4Address


class Model(BaseModel):
    BGP: BGP
