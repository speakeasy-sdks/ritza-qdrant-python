"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConsensusConfigTelemetry:
    
    bootstrap_timeout_sec: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bootstrap_timeout_sec') }})

    max_message_queue_size: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_message_queue_size') }})

    tick_period_ms: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tick_period_ms') }})

    