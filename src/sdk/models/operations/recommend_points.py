"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresponse as shared_errorresponse
from ..shared import recommendrequest as shared_recommendrequest
from ..shared import scoredpoint as shared_scoredpoint
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Any, Optional


@dataclasses.dataclass
class RecommendPointsRequest:
    
    collection_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'collection_name', 'style': 'simple', 'explode': False }})
    r"""Name of the collection to search in"""  
    consistency: Optional[Any] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'consistency', 'style': 'form', 'explode': True }})
    r"""Define read consistency guarantees for the operation"""  
    recommend_request: Optional[shared_recommendrequest.RecommendRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""Request points based on positive and negative examples."""  
    
class RecommendPoints200ApplicationJSONStatusEnum(str, Enum):
    OK = 'ok'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RecommendPoints200ApplicationJSON:
    r"""successful operation"""
    
    result: Optional[list[shared_scoredpoint.ScoredPoint]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('result'), 'exclude': lambda f: f is None }})  
    status: Optional[RecommendPoints200ApplicationJSONStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})  
    time: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('time'), 'exclude': lambda f: f is None }})
    r"""Time spent to process this request"""  
    

@dataclasses.dataclass
class RecommendPointsResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    r"""error"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    recommend_points_200_application_json_object: Optional[RecommendPoints200ApplicationJSON] = dataclasses.field(default=None)
    r"""successful operation"""  
    