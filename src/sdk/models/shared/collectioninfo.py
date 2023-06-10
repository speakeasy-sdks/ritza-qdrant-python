"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import collectionconfig as shared_collectionconfig
from ..shared import collectionstatus as shared_collectionstatus
from ..shared import payloadindexinfo as shared_payloadindexinfo
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Any


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CollectionInfoOptimizerStatus2:
    r"""Something wrong happened with optimizers"""
    error: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    


class CollectionInfoOptimizerStatus1(str, Enum):
    r"""Optimizers are reporting as expected"""
    OK = 'ok'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CollectionInfo:
    r"""Current statistics and configuration of the collection"""
    config: shared_collectionconfig.CollectionConfig = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('config') }})
    indexed_vectors_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('indexed_vectors_count') }})
    r"""Number of indexed vectors in the collection. Indexed vectors in large segments are faster to query, as it is stored in vector index (HNSW)"""
    optimizer_status: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('optimizer_status') }})
    r"""Current state of the collection"""
    payload_schema: dict[str, shared_payloadindexinfo.PayloadIndexInfo] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payload_schema') }})
    r"""Types of stored payload"""
    points_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('points_count') }})
    r"""Number of points (vectors + payloads) in collection Each point could be accessed by unique id"""
    segments_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('segments_count') }})
    r"""Number of segments in collection. Each segment has independent vector as payload indexes"""
    status: shared_collectionstatus.CollectionStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""Current state of the collection. `Green` - all good. `Yellow` - optimization is running, `Red` - some operations failed and was not recovered"""
    vectors_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vectors_count') }})
    r"""Number of vectors in collection All vectors in collection are available for querying Calculated as `points_count x vectors_per_point` Where `vectors_per_point` is a number of named vectors in schema"""
    

