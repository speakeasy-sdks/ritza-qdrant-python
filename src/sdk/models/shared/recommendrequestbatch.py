"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import recommendrequest as shared_recommendrequest
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RecommendRequestBatch:
    r"""Request points based on positive and negative examples."""
    
    searches: list[shared_recommendrequest.RecommendRequest] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('searches') }})  
    