"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import operationdurationstatistics as shared_operationdurationstatistics
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RemoteShardTelemetry:
    
    searches: shared_operationdurationstatistics.OperationDurationStatistics = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('searches') }})

    shard_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shard_id') }})

    updates: shared_operationdurationstatistics.OperationDurationStatistics = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updates') }})

    peer_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('peer_id'), 'exclude': lambda f: f is None }})

    