"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import updatestatus as shared_updatestatus
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UpdateResult:
    operation_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('operation_id') }})
    r"""Sequential number of the operation"""
    status: shared_updatestatus.UpdateStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""`Acknowledged` - Request is saved to WAL and will be process in a queue. `Completed` - Request is completed, changes are actual."""
    

