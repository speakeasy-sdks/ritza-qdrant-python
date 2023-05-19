"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import payloadschematype as shared_payloadschematype
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PayloadIndexInfo:
    r"""Display payload field type & index information"""
    
    data_type: shared_payloadschematype.PayloadSchemaType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data_type') }})
    r"""All possible names of payload types"""
    points: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('points') }})
    r"""Number of points indexed with this index"""
    params: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('params'), 'exclude': lambda f: f is None }})
    