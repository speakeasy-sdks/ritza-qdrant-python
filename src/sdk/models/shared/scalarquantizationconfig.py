"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import scalartype_enum as shared_scalartype_enum
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ScalarQuantizationConfig:
    
    type: shared_scalartype_enum.ScalarTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})

    always_ram: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('always_ram'), 'exclude': lambda f: f is None }})

    r"""If true - quantized vectors always will be stored in RAM, ignoring the config of main storage"""
    quantile: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantile'), 'exclude': lambda f: f is None }})

    r"""Quantile for quantization. Expected value range in [0.5, 1.0]. If not set - use the whole range of values"""
    