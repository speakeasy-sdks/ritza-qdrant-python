"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresponse as shared_errorresponse
from typing import Optional


@dataclasses.dataclass
class GetSnapshotRequest:
    
    collection_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'collection_name', 'style': 'simple', 'explode': False }})
    r"""Name of the collection"""
    snapshot_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'snapshot_name', 'style': 'simple', 'explode': False }})
    r"""Name of the snapshot to download"""
    

@dataclasses.dataclass
class GetSnapshotResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    r"""error"""
    get_snapshot_200_application_octet_stream_binary_string: Optional[bytes] = dataclasses.field(default=None)
    r"""Snapshot file"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    