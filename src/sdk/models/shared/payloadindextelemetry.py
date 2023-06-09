"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PayloadIndexTelemetry:
    points_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('points_count') }})
    points_values_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('points_values_count') }})
    field_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field_name'), 'exclude': lambda f: f is None }})
    histogram_bucket_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('histogram_bucket_size'), 'exclude': lambda f: f is None }})
    

