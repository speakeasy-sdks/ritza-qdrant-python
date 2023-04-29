"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import scalarquantizationconfig as shared_scalarquantizationconfig
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ScalarQuantization:
    r"""Custom params for quantization. If none - values from collection configuration are used."""
    
    scalar: shared_scalarquantizationconfig.ScalarQuantizationConfig = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scalar') }})
    