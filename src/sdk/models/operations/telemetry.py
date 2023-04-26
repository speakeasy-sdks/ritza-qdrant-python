"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresponse as shared_errorresponse
from ..shared import telemetrydata as shared_telemetrydata
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class TelemetryRequest:
    
    anonymize: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'anonymize', 'style': 'form', 'explode': True }})
    r"""If true, anonymize result"""  
    
class Telemetry200ApplicationJSONStatusEnum(str, Enum):
    OK = 'ok'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Telemetry200ApplicationJSON:
    r"""successful operation"""
    
    result: Optional[shared_telemetrydata.TelemetryData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('result'), 'exclude': lambda f: f is None }})  
    status: Optional[Telemetry200ApplicationJSONStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})  
    time: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('time'), 'exclude': lambda f: f is None }})
    r"""Time spent to process this request"""  
    

@dataclasses.dataclass
class TelemetryResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    r"""error"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    telemetry_200_application_json_object: Optional[Telemetry200ApplicationJSON] = dataclasses.field(default=None)
    r"""successful operation"""  
    