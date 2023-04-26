"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CollectionParamsDiff:
    r"""Collection base params.  If none - values from service configuration file are used."""
    
    replication_factor: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('replication_factor'), 'exclude': lambda f: f is None }})
    r"""Number of replicas for each shard"""  
    write_consistency_factor: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('write_consistency_factor'), 'exclude': lambda f: f is None }})
    r"""Minimal number successful responses from replicas to consider operation successful"""  
    