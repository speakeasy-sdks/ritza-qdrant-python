"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import moveshard as shared_moveshard
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ReplicateShardOperation:
    
    replicate_shard: shared_moveshard.MoveShard = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('replicate_shard') }})

    