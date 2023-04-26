"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateFieldIndex:
    r"""Field name"""
    
    field_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field_name') }})  
    field_schema: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field_schema'), 'exclude': lambda f: f is None }})  
    