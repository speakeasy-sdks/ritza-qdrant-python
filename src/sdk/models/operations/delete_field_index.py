"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresponse as shared_errorresponse
from ..shared import updateresult as shared_updateresult
from ..shared import writeordering_enum as shared_writeordering_enum
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class DeleteFieldIndexRequest:
    
    collection_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'collection_name', 'style': 'simple', 'explode': False }})
    r"""Name of the collection"""  
    field_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'field_name', 'style': 'simple', 'explode': False }})
    r"""Name of the field where to delete the index"""  
    ordering: Optional[shared_writeordering_enum.WriteOrderingEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'ordering', 'style': 'form', 'explode': True }})
    r"""define ordering guarantees for the operation"""  
    wait: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'wait', 'style': 'form', 'explode': True }})
    r"""If true, wait for changes to actually happen"""  
    
class DeleteFieldIndex200ApplicationJSONStatusEnum(str, Enum):
    OK = 'ok'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteFieldIndex200ApplicationJSON:
    r"""successful operation"""
    
    result: Optional[shared_updateresult.UpdateResult] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('result'), 'exclude': lambda f: f is None }})  
    status: Optional[DeleteFieldIndex200ApplicationJSONStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})  
    time: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('time'), 'exclude': lambda f: f is None }})
    r"""Time spent to process this request"""  
    

@dataclasses.dataclass
class DeleteFieldIndexResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    delete_field_index_200_application_json_object: Optional[DeleteFieldIndex200ApplicationJSON] = dataclasses.field(default=None)
    r"""successful operation"""  
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    r"""error"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    