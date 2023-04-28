"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PayloadSelectorInclude:
    r"""Specifies how to treat payload selector"""
    
    include: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('include') }})

    r"""Only include this payload keys"""
    