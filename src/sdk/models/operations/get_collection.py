"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import collectioninfo as shared_collectioninfo
from ..shared import errorresponse as shared_errorresponse
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetCollectionRequest:
    
    collection_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'collection_name', 'style': 'simple', 'explode': False }})

    r"""Name of the collection to retrieve"""
    
class GetCollection200ApplicationJSONStatusEnum(str, Enum):
    OK = 'ok'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCollection200ApplicationJSON:
    r"""successful operation"""
    
    result: Optional[shared_collectioninfo.CollectionInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('result'), 'exclude': lambda f: f is None }})

    r"""Current statistics and configuration of the collection"""
    status: Optional[GetCollection200ApplicationJSONStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})

    time: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('time'), 'exclude': lambda f: f is None }})

    r"""Time spent to process this request"""
    

@dataclasses.dataclass
class GetCollectionResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)

    r"""error"""
    get_collection_200_application_json_object: Optional[GetCollection200ApplicationJSON] = dataclasses.field(default=None)

    r"""successful operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    