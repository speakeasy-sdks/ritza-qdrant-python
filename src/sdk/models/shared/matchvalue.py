"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class MatchValue:
    r"""Exact match of the given value"""
    
    value: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})  
    