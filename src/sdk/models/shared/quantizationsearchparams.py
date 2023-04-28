"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class QuantizationSearchParams:
    r"""Additional parameters of the search"""
    
    ignore: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ignore'), 'exclude': lambda f: f is None }})

    r"""If true, quantized vectors are ignored. Default is false."""
    rescore: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rescore'), 'exclude': lambda f: f is None }})

    r"""If true, use original vectors to re-score top-k results. Might require more time in case if original vectors are stored on disk. Default is false."""
    