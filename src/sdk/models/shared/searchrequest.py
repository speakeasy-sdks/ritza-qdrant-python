"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SearchRequest:
    r"""Search request. Holds all conditions and parameters for the search of most similar points by vector similarity given the filtering restrictions."""
    limit: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('limit') }})
    r"""Max number of result to return"""
    vector: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vector') }})
    r"""Vector data separator for named and unnamed modes Unanmed mode:
    
    { \"vector\": [1.0, 2.0, 3.0] }
    
    or named mode:
    
    { \"vector\": { \"vector\": [1.0, 2.0, 3.0], \"name\": \"image-embeddings\" } }
    """
    filter: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filter'), 'exclude': lambda f: f is None }})
    r"""Look only for points which satisfies this conditions"""
    offset: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('offset'), 'exclude': lambda f: f is None }})
    r"""Offset of the first result to return. May be used to paginate results. Note: large offset values may cause performance issues."""
    params: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('params'), 'exclude': lambda f: f is None }})
    r"""Additional search params"""
    score_threshold: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('score_threshold'), 'exclude': lambda f: f is None }})
    r"""Define a minimal score threshold for the result. If defined, less similar results will not be returned. Score of the returned result might be higher or smaller than the threshold depending on the Distance function used. E.g. for cosine similarity only higher scores will be returned."""
    with_payload: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('with_payload'), 'exclude': lambda f: f is None }})
    r"""Select which payload to return with the response. Default: None"""
    with_vector: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('with_vector'), 'exclude': lambda f: f is None }})
    r"""Whether to return the point vector with the result?"""
    

