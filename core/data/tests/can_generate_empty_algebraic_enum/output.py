"""
 Generated by typeshare 1.0.0
"""
from __future__ import annotations

from typing import Literal
from pydantic import BaseModel


class AddressFixedAddress(BaseModel):
    type: Literal["FixedAddress"]
    content: AddressDetails


class AddressNoFixedAddress:
    type: Literal["NoFixedAddress"]
Address = AddressFixedAddress | AddressNoFixedAddress

class AddressDetails(BaseModel):
    pass

