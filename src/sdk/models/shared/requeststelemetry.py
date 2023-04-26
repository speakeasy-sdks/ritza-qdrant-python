"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import grpctelemetry as shared_grpctelemetry
from ..shared import webapitelemetry as shared_webapitelemetry
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RequestsTelemetry:
    
    grpc: shared_grpctelemetry.GrpcTelemetry = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grpc') }})  
    rest: shared_webapitelemetry.WebAPITelemetry = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rest') }})  
    