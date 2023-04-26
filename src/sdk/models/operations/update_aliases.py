"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import changealiasesoperation as shared_changealiasesoperation
from ..shared import errorresponse as shared_errorresponse
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class UpdateAliasesRequest:
    
    change_aliases_operation: Optional[shared_changealiasesoperation.ChangeAliasesOperation] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""Alias update operations"""  
    timeout: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeout', 'style': 'form', 'explode': True }})
    r"""Wait for operation commit timeout in seconds.
    If timeout is reached - request will return with service error.
    """  
    
class UpdateAliases200ApplicationJSONStatusEnum(str, Enum):
    OK = 'ok'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateAliases200ApplicationJSON:
    r"""successful operation"""
    
    result: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('result'), 'exclude': lambda f: f is None }})  
    status: Optional[UpdateAliases200ApplicationJSONStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})  
    time: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('time'), 'exclude': lambda f: f is None }})
    r"""Time spent to process this request"""  
    

@dataclasses.dataclass
class UpdateAliasesResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    r"""error"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    update_aliases_200_application_json_object: Optional[UpdateAliases200ApplicationJSON] = dataclasses.field(default=None)
    r"""successful operation"""  
    