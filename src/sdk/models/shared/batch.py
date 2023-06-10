"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Batch:
    ids: list[Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ids') }})
    vectors: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vectors') }})
    payloads: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payloads'), 'exclude': lambda f: f is None }})
    

