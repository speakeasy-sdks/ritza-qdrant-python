"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresponse as shared_errorresponse
from ..shared import snapshotrecover as shared_snapshotrecover
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class RecoverFromSnapshotRequest:
    
    collection_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'collection_name', 'style': 'simple', 'explode': False }})

    r"""Name of the collection"""
    snapshot_recover: Optional[shared_snapshotrecover.SnapshotRecover] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})

    r"""Snapshot to recover from"""
    wait: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'wait', 'style': 'form', 'explode': True }})

    r"""If true, wait for changes to actually happen. If false - let changes happen in background. Default is true."""
    
class RecoverFromSnapshot202ApplicationJSONStatusEnum(str, Enum):
    ACCEPTED = 'accepted'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RecoverFromSnapshot202ApplicationJSON:
    r"""operation is accepted"""
    
    status: Optional[RecoverFromSnapshot202ApplicationJSONStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})

    time: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('time'), 'exclude': lambda f: f is None }})

    r"""Time spent to process this request"""
    
class RecoverFromSnapshot200ApplicationJSONStatusEnum(str, Enum):
    OK = 'ok'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RecoverFromSnapshot200ApplicationJSON:
    r"""successful operation"""
    
    result: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('result'), 'exclude': lambda f: f is None }})

    status: Optional[RecoverFromSnapshot200ApplicationJSONStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})

    time: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('time'), 'exclude': lambda f: f is None }})

    r"""Time spent to process this request"""
    

@dataclasses.dataclass
class RecoverFromSnapshotResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)

    r"""error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    recover_from_snapshot_200_application_json_object: Optional[RecoverFromSnapshot200ApplicationJSON] = dataclasses.field(default=None)

    r"""successful operation"""
    recover_from_snapshot_202_application_json_object: Optional[RecoverFromSnapshot202ApplicationJSON] = dataclasses.field(default=None)

    r"""operation is accepted"""
    