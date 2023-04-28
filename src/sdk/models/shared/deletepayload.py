"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeletePayload:
    r"""delete payload on points"""
    
    keys: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('keys') }})

    r"""List of payload keys to remove from payload"""
    filter: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filter'), 'exclude': lambda f: f is None }})

    r"""Deletes values from points that satisfy this filter condition"""
    points: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('points'), 'exclude': lambda f: f is None }})

    r"""Deletes values from each point in this list"""
    