"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import record as shared_record
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ScrollResult:
    r"""Result of the points read request"""
    
    points: list[shared_record.Record] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('points') }})
    r"""List of retrieved points"""
    next_page_offset: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next_page_offset'), 'exclude': lambda f: f is None }})
    r"""Offset which should be used to retrieve a next page result"""
    