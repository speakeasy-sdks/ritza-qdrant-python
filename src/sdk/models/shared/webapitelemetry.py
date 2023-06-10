"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import operationdurationstatistics as shared_operationdurationstatistics
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class WebAPITelemetry:
    responses: dict[str, dict[str, shared_operationdurationstatistics.OperationDurationStatistics]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('responses') }})
    

