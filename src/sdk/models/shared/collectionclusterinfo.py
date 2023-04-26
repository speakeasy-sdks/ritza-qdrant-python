"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import localshardinfo as shared_localshardinfo
from ..shared import remoteshardinfo as shared_remoteshardinfo
from ..shared import shardtransferinfo as shared_shardtransferinfo
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CollectionClusterInfo:
    r"""Current clustering distribution for the collection"""
    
    local_shards: list[shared_localshardinfo.LocalShardInfo] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('local_shards') }})
    r"""Local shards"""  
    peer_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('peer_id') }})
    r"""ID of this peer"""  
    remote_shards: list[shared_remoteshardinfo.RemoteShardInfo] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_shards') }})
    r"""Remote shards"""  
    shard_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shard_count') }})
    r"""Total number of shards"""  
    shard_transfers: list[shared_shardtransferinfo.ShardTransferInfo] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shard_transfers') }})
    r"""Shard transfers"""  
    