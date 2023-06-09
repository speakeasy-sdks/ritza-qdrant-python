"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PointRequest:
    r"""List of points to retrieve"""
    ids: list[Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ids') }})
    r"""Look for points with ids"""
    with_payload: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('with_payload'), 'exclude': lambda f: f is None }})
    r"""Select which payload to return with the response. Default: All"""
    with_vector: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('with_vector'), 'exclude': lambda f: f is None }})
    r"""Options for specifying which vector to include"""
    

