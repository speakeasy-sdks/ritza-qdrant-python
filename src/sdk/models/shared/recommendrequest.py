"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class RecommendRequest:
    r"""Recommendation request. Provides positive and negative examples of the vectors, which are already stored in the collection.
    
    Service should look for the points which are closer to positive examples and at the same time further to negative examples. The concrete way of how to compare negative and positive distances is up to implementation in `segment` crate.
    """
    limit: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('limit') }})
    r"""Max number of result to return"""
    positive: list[Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('positive') }})
    r"""Look for vectors closest to those"""
    filter: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filter'), 'exclude': lambda f: f is None }})
    r"""Look only for points which satisfies this conditions"""
    lookup_from: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lookup_from'), 'exclude': lambda f: f is None }})
    r"""The location used to lookup vectors. If not specified - use current collection. Note: the other collection should have the same vector size as the current collection"""
    negative: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('negative'), 'exclude': lambda f: f is None }})
    r"""Try to avoid vectors like this"""
    offset: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('offset'), 'exclude': lambda f: f is None }})
    r"""Offset of the first result to return. May be used to paginate results. Note: large offset values may cause performance issues."""
    params: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('params'), 'exclude': lambda f: f is None }})
    r"""Additional search params"""
    score_threshold: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('score_threshold'), 'exclude': lambda f: f is None }})
    r"""Define a minimal score threshold for the result. If defined, less similar results will not be returned. Score of the returned result might be higher or smaller than the threshold depending on the Distance function used. E.g. for cosine similarity only higher scores will be returned."""
    using: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('using'), 'exclude': lambda f: f is None }})
    r"""Define which vector to use for recommendation, if not specified - try to use default vector"""
    with_payload: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('with_payload'), 'exclude': lambda f: f is None }})
    r"""Select which payload to return with the response. Default: None"""
    with_vector: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('with_vector'), 'exclude': lambda f: f is None }})
    r"""Whether to return the point vector with the result?"""
    

