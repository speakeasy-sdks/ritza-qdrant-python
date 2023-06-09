"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import payloadfield as shared_payloadfield
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class IsNullCondition:
    r"""Select points with null payload for a specified field"""
    is_null: shared_payloadfield.PayloadField = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_null') }})
    r"""Payload field"""
    

