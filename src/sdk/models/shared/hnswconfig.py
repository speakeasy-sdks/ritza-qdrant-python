"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class HnswConfig:
    r"""Config of HNSW index"""
    
    ef_construct: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ef_construct') }})

    r"""Number of neighbours to consider during the index building. Larger the value - more accurate the search, more time required to build index."""
    full_scan_threshold: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('full_scan_threshold') }})

    r"""Minimal size (in KiloBytes) of vectors for additional payload-based indexing. If payload chunk is smaller than `full_scan_threshold_kb` additional indexing won't be used - in this case full-scan search should be preferred by query planner and additional indexing is not required. Note: 1Kb = 1 vector of size 256"""
    m: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('m') }})

    r"""Number of edges per node in the index graph. Larger the value - more accurate the search, more space required."""
    max_indexing_threads: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_indexing_threads'), 'exclude': lambda f: f is None }})

    r"""Number of parallel threads used for background index building. If 0 - auto selection."""
    on_disk: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('on_disk'), 'exclude': lambda f: f is None }})

    r"""Store HNSW index on disk. If set to false, index will be stored in RAM. Default: false"""
    payload_m: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payload_m'), 'exclude': lambda f: f is None }})

    r"""Custom M param for hnsw graph built for payload index. If not set, default M will be used."""
    