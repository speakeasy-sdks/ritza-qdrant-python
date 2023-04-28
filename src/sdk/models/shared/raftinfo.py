"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RaftInfo:
    r"""Summary information about the current raft state"""
    
    commit: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('commit') }})

    r"""The index of the latest committed (finalized) operation that this peer is aware of."""
    is_voter: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_voter') }})

    r"""Is this peer a voter or a learner"""
    pending_operations: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pending_operations') }})

    r"""Number of consensus operations pending to be applied on this peer"""
    term: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('term') }})

    r"""Raft divides time into terms of arbitrary length, each beginning with an election. If a candidate wins the election, it remains the leader for the rest of the term. The term number increases monotonically. Each server stores the current term number which is also exchanged in every communication."""
    leader: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('leader'), 'exclude': lambda f: f is None }})

    r"""Leader of the current term"""
    role: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('role'), 'exclude': lambda f: f is None }})

    r"""Role of this peer in the current term"""
    