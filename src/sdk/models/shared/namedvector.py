"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NamedVector:
    r"""Vector data with name"""
    
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Name of vector data"""  
    vector: list[float] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vector') }})
    r"""Vector data"""  
    