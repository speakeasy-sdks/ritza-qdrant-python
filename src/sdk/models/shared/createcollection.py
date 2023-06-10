"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateCollection:
    r"""Operation for creating new collection and (optionally) specify index params"""
    vectors: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vectors') }})
    r"""Vector params separator for single and multiple vector modes Single mode:
    
    { \"size\": 128, \"distance\": \"Cosine\" }
    
    or multiple mode:
    
    { \"default\": { \"size\": 128, \"distance\": \"Cosine\" } }
    """
    hnsw_config: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hnsw_config'), 'exclude': lambda f: f is None }})
    r"""Custom params for HNSW index. If none - values from service configuration file are used."""
    init_from: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('init_from'), 'exclude': lambda f: f is None }})
    r"""Specify other collection to copy data from."""
    on_disk_payload: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('on_disk_payload'), 'exclude': lambda f: f is None }})
    r"""If true - point's payload will not be stored in memory. It will be read from the disk every time it is requested. This setting saves RAM by (slightly) increasing the response time. Note: those payload values that are involved in filtering and are indexed - remain in RAM."""
    optimizers_config: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('optimizers_config'), 'exclude': lambda f: f is None }})
    r"""Custom params for Optimizers.  If none - values from service configuration file are used."""
    quantization_config: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantization_config'), 'exclude': lambda f: f is None }})
    r"""Quantization parameters. If none - quantization is disabled."""
    replication_factor: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('replication_factor'), 'exclude': lambda f: f is None }})
    r"""Number of shards replicas. Default is 1 Minimum is 1"""
    shard_number: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shard_number'), 'exclude': lambda f: f is None }})
    r"""Number of shards in collection. Default is 1 for standalone, otherwise equal to the number of nodes Minimum is 1"""
    wal_config: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('wal_config'), 'exclude': lambda f: f is None }})
    r"""Custom params for WAL. If none - values from service configuration file are used."""
    write_consistency_factor: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('write_consistency_factor'), 'exclude': lambda f: f is None }})
    r"""Defines how many replicas should apply the operation for us to consider it successful. Increasing this number will make the collection more resilient to inconsistencies, but will also make it fail if not enough replicas are available. Does not have any performance impact."""
    

