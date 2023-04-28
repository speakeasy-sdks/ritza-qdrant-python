"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchParams:
    r"""Additional parameters of the search"""
    
    exact: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('exact'), 'exclude': lambda f: f is None }})

    r"""Search without approximation. If set to true, search may run long but with exact results."""
    hnsw_ef: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hnsw_ef'), 'exclude': lambda f: f is None }})

    r"""Params relevant to HNSW index /// Size of the beam in a beam-search. Larger the value - more accurate the result, more time required for search."""
    quantization: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantization'), 'exclude': lambda f: f is None }})

    r"""Quantization params"""
    