"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from sdk.models import operations, shared
from typing import Optional

class Points:
    r"""Float-point vectors with payload."""
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    def clear_payload(self, request: operations.ClearPayloadRequest) -> operations.ClearPayloadResponse:
        r"""Clear payload
        Remove all payload for specified points
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.ClearPayloadRequest, base_url, '/collections/{collection_name}/points/payload/clear', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.ClearPayloadRequest, request)
        
        client = self._client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ClearPayloadResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ClearPayload200ApplicationJSON])
                res.clear_payload_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    def count_points(self, request: operations.CountPointsRequest) -> operations.CountPointsResponse:
        r"""Count points
        Count points which matches given filtering condition
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.CountPointsRequest, base_url, '/collections/{collection_name}/points/count', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "count_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CountPointsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CountPoints200ApplicationJSON])
                res.count_points_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    def delete_payload(self, request: operations.DeletePayloadRequest) -> operations.DeletePayloadResponse:
        r"""Delete payload
        Delete specified key payload for points
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeletePayloadRequest, base_url, '/collections/{collection_name}/points/payload/delete', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "delete_payload", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.DeletePayloadRequest, request)
        
        client = self._client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeletePayloadResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeletePayload200ApplicationJSON])
                res.delete_payload_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    def delete_points(self, request: operations.DeletePointsRequest) -> operations.DeletePointsResponse:
        r"""Delete points
        Delete points
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeletePointsRequest, base_url, '/collections/{collection_name}/points/delete', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.DeletePointsRequest, request)
        
        client = self._client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeletePointsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeletePoints200ApplicationJSON])
                res.delete_points_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    def get_point(self, request: operations.GetPointRequest) -> operations.GetPointResponse:
        r"""Get point
        Retrieve full information of single point by id
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetPointRequest, base_url, '/collections/{collection_name}/points/{id}', request)
        
        query_params = utils.get_query_params(operations.GetPointRequest, request)
        
        client = self._client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetPointResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetPoint200ApplicationJSON])
                res.get_point_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    def get_points(self, request: operations.GetPointsRequest) -> operations.GetPointsResponse:
        r"""Get points
        Retrieve multiple points by specified IDs
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetPointsRequest, base_url, '/collections/{collection_name}/points', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "point_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.GetPointsRequest, request)
        
        client = self._client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetPointsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetPoints200ApplicationJSON])
                res.get_points_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    def overwrite_payload(self, request: operations.OverwritePayloadRequest) -> operations.OverwritePayloadResponse:
        r"""Overwrite payload
        Replace full payload of points with new one
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.OverwritePayloadRequest, base_url, '/collections/{collection_name}/points/payload', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "set_payload", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.OverwritePayloadRequest, request)
        
        client = self._client
        
        http_res = client.request('PUT', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.OverwritePayloadResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.OverwritePayload200ApplicationJSON])
                res.overwrite_payload_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    def recommend_batch_points(self, request: operations.RecommendBatchPointsRequest) -> operations.RecommendBatchPointsResponse:
        r"""Recommend batch points
        Look for the points which are closer to stored positive examples and at the same time further to negative examples.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.RecommendBatchPointsRequest, base_url, '/collections/{collection_name}/points/recommend/batch', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "recommend_request_batch", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.RecommendBatchPointsRequest, request)
        
        client = self._client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RecommendBatchPointsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.RecommendBatchPoints200ApplicationJSON])
                res.recommend_batch_points_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    def recommend_points(self, request: operations.RecommendPointsRequest) -> operations.RecommendPointsResponse:
        r"""Recommend points
        Look for the points which are closer to stored positive examples and at the same time further to negative examples.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.RecommendPointsRequest, base_url, '/collections/{collection_name}/points/recommend', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "recommend_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.RecommendPointsRequest, request)
        
        client = self._client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RecommendPointsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.RecommendPoints200ApplicationJSON])
                res.recommend_points_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    def scroll_points(self, request: operations.ScrollPointsRequest) -> operations.ScrollPointsResponse:
        r"""Scroll points
        Scroll request - paginate over all points which matches given filtering condition
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.ScrollPointsRequest, base_url, '/collections/{collection_name}/points/scroll', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "scroll_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.ScrollPointsRequest, request)
        
        client = self._client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ScrollPointsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ScrollPoints200ApplicationJSON])
                res.scroll_points_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    def search_batch_points(self, request: operations.SearchBatchPointsRequest) -> operations.SearchBatchPointsResponse:
        r"""Search batch points
        Retrieve by batch the closest points based on vector similarity and given filtering conditions
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.SearchBatchPointsRequest, base_url, '/collections/{collection_name}/points/search/batch', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "search_request_batch", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.SearchBatchPointsRequest, request)
        
        client = self._client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SearchBatchPointsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.SearchBatchPoints200ApplicationJSON])
                res.search_batch_points_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    def search_points(self, request: operations.SearchPointsRequest) -> operations.SearchPointsResponse:
        r"""Search points
        Retrieve closest points based on vector similarity and given filtering conditions
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.SearchPointsRequest, base_url, '/collections/{collection_name}/points/search', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "search_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.SearchPointsRequest, request)
        
        client = self._client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SearchPointsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.SearchPoints200ApplicationJSON])
                res.search_points_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    def set_payload(self, request: operations.SetPayloadRequest) -> operations.SetPayloadResponse:
        r"""Set payload
        Set payload values for points
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.SetPayloadRequest, base_url, '/collections/{collection_name}/points/payload', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "set_payload", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.SetPayloadRequest, request)
        
        client = self._client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SetPayloadResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.SetPayload200ApplicationJSON])
                res.set_payload_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    def upsert_points(self, request: operations.UpsertPointsRequest) -> operations.UpsertPointsResponse:
        r"""Upsert points
        Perform insert + updates on points. If point with given ID already exists - it will be overwritten.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.UpsertPointsRequest, base_url, '/collections/{collection_name}/points', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.UpsertPointsRequest, request)
        
        client = self._client
        
        http_res = client.request('PUT', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpsertPointsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UpsertPoints200ApplicationJSON])
                res.upsert_points_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    