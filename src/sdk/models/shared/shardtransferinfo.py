"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ShardTransferInfo:
    from_: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from') }})
    shard_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shard_id') }})
    sync: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sync') }})
    r"""If `true` transfer is a synchronization of a replicas If `false` transfer is a moving of a shard from one peer to another"""
    to: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('to') }})
    

