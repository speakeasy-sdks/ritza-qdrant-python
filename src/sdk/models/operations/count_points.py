"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import countrequest as shared_countrequest
from ..shared import countresult as shared_countresult
from ..shared import errorresponse as shared_errorresponse
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional



@dataclasses.dataclass
class CountPointsRequest:
    collection_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'collection_name', 'style': 'simple', 'explode': False }})
    r"""Name of the collection to count in"""
    count_request: Optional[shared_countrequest.CountRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""Request counts of points which matches given filtering condition"""
    


class CountPoints200ApplicationJSONStatus(str, Enum):
    OK = 'ok'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CountPoints200ApplicationJSON:
    r"""successful operation"""
    result: Optional[shared_countresult.CountResult] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('result'), 'exclude': lambda f: f is None }})
    status: Optional[CountPoints200ApplicationJSONStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    time: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('time'), 'exclude': lambda f: f is None }})
    r"""Time spent to process this request"""
    




@dataclasses.dataclass
class CountPointsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    count_points_200_application_json_object: Optional[CountPoints200ApplicationJSON] = dataclasses.field(default=None)
    r"""successful operation"""
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    r"""error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

