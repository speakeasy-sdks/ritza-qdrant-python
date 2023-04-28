"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import batch as shared_batch
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PointsBatch:
    
    batch: shared_batch.Batch = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('batch') }})

    