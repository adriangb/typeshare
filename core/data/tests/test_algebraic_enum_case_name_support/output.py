"""
 Generated by typeshare 1.0.0
"""
from __future__ import annotations

from pydantic import BaseModel
from typing import List, Literal


class ItemDetailsFieldValue(BaseModel):
    pass

class AdvancedColorsString(BaseModel):
    type: Literal["string"]
    content: str


class AdvancedColorsNumber(BaseModel):
    type: Literal["number"]
    content: int


class AdvancedColorsNumberArray(BaseModel):
    type: Literal["number-array"]
    content: List[int]


class AdvancedColorsReallyCoolType(BaseModel):
    type: Literal["reallyCoolType"]
    content: ItemDetailsFieldValue


AdvancedColors = AdvancedColorsString | AdvancedColorsNumber | AdvancedColorsNumberArray | AdvancedColorsReallyCoolType

