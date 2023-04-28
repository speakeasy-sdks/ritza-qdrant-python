"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import operationdurationstatistics as shared_operationdurationstatistics
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Any


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OptimizerTelemetryStatus2:
    r"""Something wrong happened with optimizers"""
    
    error: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})

    
class OptimizerTelemetryStatus1Enum(str, Enum):
    r"""Optimizers are reporting as expected"""
    OK = 'ok'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OptimizerTelemetry:
    
    optimizations: shared_operationdurationstatistics.OperationDurationStatistics = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('optimizations') }})

    status: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})

    r"""Current state of the collection"""
    