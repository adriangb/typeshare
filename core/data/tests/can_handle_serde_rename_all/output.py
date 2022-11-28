"""
 Generated by typeshare 1.0.0
"""
from __future__ import annotations

from typing import Annotated, List, Optional
from pydantic import Field, BaseModel


class Person2(BaseModel):
    """
    This is a Person2 struct with UPPERCASE rename
    """
    first_name: Annotated[str, Field(alias="FIRST_NAME")]
    last_name: Annotated[str, Field(alias="LAST_NAME")]
    age: Annotated[int, Field(alias="AGE")]


class Person(BaseModel):
    """
    This is a Person struct with camelCase rename
    """
    first_name: Annotated[str, Field(alias="firstName")]
    last_name: Annotated[str, Field(alias="lastName")]
    age: int
    extra_special_field_1: Annotated[int, Field(alias="extraSpecialField1")]
    extra_special_field_2: Annotated[Optional[List[str]], Field(alias="extraSpecialField2")]


