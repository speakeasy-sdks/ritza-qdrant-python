"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import collectionsresponse as shared_collectionsresponse
from ..shared import errorresponse as shared_errorresponse
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional

class GetCollections200ApplicationJSONStatusEnum(str, Enum):
    OK = 'ok'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCollections200ApplicationJSON:
    r"""successful operation"""
    
    result: Optional[shared_collectionsresponse.CollectionsResponse] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('result'), 'exclude': lambda f: f is None }})

    status: Optional[GetCollections200ApplicationJSONStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})

    time: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('time'), 'exclude': lambda f: f is None }})

    r"""Time spent to process this request"""
    

@dataclasses.dataclass
class GetCollectionsResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)

    r"""error"""
    get_collections_200_application_json_object: Optional[GetCollections200ApplicationJSON] = dataclasses.field(default=None)

    r"""successful operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    