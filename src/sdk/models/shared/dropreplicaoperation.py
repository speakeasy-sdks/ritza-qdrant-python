"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import replica as shared_replica
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DropReplicaOperation:
    
    drop_replica: shared_replica.Replica = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('drop_replica') }})

    