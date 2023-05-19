"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresponse as shared_errorresponse
from ..shared import setpayload as shared_setpayload
from ..shared import updateresult as shared_updateresult
from ..shared import writeordering as shared_writeordering
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class SetPayloadRequest:
    
    collection_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'collection_name', 'style': 'simple', 'explode': False }})
    r"""Name of the collection to set from"""
    ordering: Optional[shared_writeordering.WriteOrdering] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'ordering', 'style': 'form', 'explode': True }})
    r"""define ordering guarantees for the operation"""
    set_payload: Optional[shared_setpayload.SetPayload] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""Set payload on points"""
    wait: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'wait', 'style': 'form', 'explode': True }})
    r"""If true, wait for changes to actually happen"""
    
class SetPayload200ApplicationJSONStatus(str, Enum):
    OK = 'ok'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SetPayload200ApplicationJSON:
    r"""successful operation"""
    
    result: Optional[shared_updateresult.UpdateResult] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('result'), 'exclude': lambda f: f is None }})
    status: Optional[SetPayload200ApplicationJSONStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    time: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('time'), 'exclude': lambda f: f is None }})
    r"""Time spent to process this request"""
    

@dataclasses.dataclass
class SetPayloadResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    r"""error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    set_payload_200_application_json_object: Optional[SetPayload200ApplicationJSON] = dataclasses.field(default=None)
    r"""successful operation"""
    