"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from sdk.models import operations, shared
from typing import Optional

class Service:
    r"""Service management"""
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
        
    
    def get_locks(self) -> operations.GetLocksResponse:
        r"""Get lock options
        Get lock options. If write is locked, all write operations and collection creation are forbidden
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/locks'
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetLocksResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetLocks200ApplicationJSON])
                res.get_locks_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    
    def metrics(self, request: operations.MetricsRequest) -> operations.MetricsResponse:
        r"""Collect Prometheus metrics data
        Collect metrics data including app info, collections info, cluster info and statistics
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/metrics'
        headers = {}
        query_params = utils.get_query_params(operations.MetricsRequest, request)
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.MetricsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'text/plain'):
                res.metrics_200_text_plain_string = http_res.content
        elif http_res.status_code >= 400 and http_res.status_code < 500:
            pass

        return res

    
    def post_locks(self, request: shared.LocksOption) -> operations.PostLocksResponse:
        r"""Set lock options
        Set lock options. If write is locked, all write operations and collection creation are forbidden. Returns previous lock options
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/locks'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostLocksResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostLocks200ApplicationJSON])
                res.post_locks_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    
    def telemetry(self, request: operations.TelemetryRequest) -> operations.TelemetryResponse:
        r"""Collect telemetry data
        Collect telemetry data including app info, system info, collections info, cluster info, configs and statistics
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/telemetry'
        headers = {}
        query_params = utils.get_query_params(operations.TelemetryRequest, request)
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TelemetryResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.Telemetry200ApplicationJSON])
                res.telemetry_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    