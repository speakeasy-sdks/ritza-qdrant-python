"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GeoPoint:
    r"""Geo point payload schema"""
    
    lat: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lat') }})  
    lon: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lon') }})  
    