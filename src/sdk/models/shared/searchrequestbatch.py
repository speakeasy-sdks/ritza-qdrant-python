"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import searchrequest as shared_searchrequest
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchRequestBatch:
    r"""Search batch request"""
    
    searches: list[shared_searchrequest.SearchRequest] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('searches') }})  
    