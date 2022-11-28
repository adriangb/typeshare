"""
 Generated by typeshare 1.0.0
"""
from __future__ import annotations

from pydantic import Field, BaseModel
from typing import Annotated, Dict, List, Optional


class Types(BaseModel):
    s: str
    static_s: str
    int_8: Annotated[int, Field(alias="int8")]
    float: float
    double: float
    array: List[str]
    dictionary: Dict[str, int]
    optional_dictionary: Optional[Dict[str, int]]
    custom_type: CustomType


class CustomType(BaseModel):
    pass

