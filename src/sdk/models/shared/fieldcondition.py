"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FieldCondition:
    r"""All possible payload filtering conditions"""
    
    key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key') }})

    r"""Payload key"""
    geo_bounding_box: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('geo_bounding_box'), 'exclude': lambda f: f is None }})

    r"""Check if points geo location lies in a given area"""
    geo_radius: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('geo_radius'), 'exclude': lambda f: f is None }})

    r"""Check if geo point is within a given radius"""
    match: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('match'), 'exclude': lambda f: f is None }})

    r"""Check if point has field with a given value"""
    range: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('range'), 'exclude': lambda f: f is None }})

    r"""Check if points value lies in a given range"""
    values_count: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('values_count'), 'exclude': lambda f: f is None }})

    r"""Check number of values of the field"""
    