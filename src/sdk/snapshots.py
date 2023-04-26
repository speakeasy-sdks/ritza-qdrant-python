"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from sdk.models import operations, shared
from typing import Optional

class Snapshots:
    r"""Storage and collections snapshots"""
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
        
    def create_full_snapshot(self, request: operations.CreateFullSnapshotRequest) -> operations.CreateFullSnapshotResponse:
        r"""Create storage snapshot
        Create new snapshot of the whole storage
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/snapshots'
        
        query_params = utils.get_query_params(operations.CreateFullSnapshotRequest, request)
        
        client = self._client
        
        http_res = client.request('POST', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateFullSnapshotResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateFullSnapshot200ApplicationJSON])
                res.create_full_snapshot_200_application_json_object = out
        elif http_res.status_code == 202:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateFullSnapshot202ApplicationJSON])
                res.create_full_snapshot_202_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    def create_snapshot(self, request: operations.CreateSnapshotRequest) -> operations.CreateSnapshotResponse:
        r"""Create collection snapshot
        Create new snapshot for a collection
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.CreateSnapshotRequest, base_url, '/collections/{collection_name}/snapshots', request)
        
        query_params = utils.get_query_params(operations.CreateSnapshotRequest, request)
        
        client = self._client
        
        http_res = client.request('POST', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateSnapshotResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateSnapshot200ApplicationJSON])
                res.create_snapshot_200_application_json_object = out
        elif http_res.status_code == 202:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateSnapshot202ApplicationJSON])
                res.create_snapshot_202_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    def delete_full_snapshot(self, request: operations.DeleteFullSnapshotRequest) -> operations.DeleteFullSnapshotResponse:
        r"""Delete storage snapshot
        Delete snapshot of the whole storage
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteFullSnapshotRequest, base_url, '/snapshots/{snapshot_name}', request)
        
        query_params = utils.get_query_params(operations.DeleteFullSnapshotRequest, request)
        
        client = self._client
        
        http_res = client.request('DELETE', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteFullSnapshotResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeleteFullSnapshot200ApplicationJSON])
                res.delete_full_snapshot_200_application_json_object = out
        elif http_res.status_code == 202:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeleteFullSnapshot202ApplicationJSON])
                res.delete_full_snapshot_202_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    def delete_snapshot(self, request: operations.DeleteSnapshotRequest) -> operations.DeleteSnapshotResponse:
        r"""Delete collection snapshot
        Delete snapshot for a collection
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteSnapshotRequest, base_url, '/collections/{collection_name}/snapshots/{snapshot_name}', request)
        
        query_params = utils.get_query_params(operations.DeleteSnapshotRequest, request)
        
        client = self._client
        
        http_res = client.request('DELETE', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteSnapshotResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeleteSnapshot200ApplicationJSON])
                res.delete_snapshot_200_application_json_object = out
        elif http_res.status_code == 202:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeleteSnapshot202ApplicationJSON])
                res.delete_snapshot_202_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    def get_full_snapshot(self, request: operations.GetFullSnapshotRequest) -> operations.GetFullSnapshotResponse:
        r"""Download storage snapshot
        Download specified snapshot of the whole storage as a file
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetFullSnapshotRequest, base_url, '/snapshots/{snapshot_name}', request)
        
        
        client = self._client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetFullSnapshotResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/octet-stream'):
                res.get_full_snapshot_200_application_octet_stream_binary_string = http_res.content
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    def get_snapshot(self, request: operations.GetSnapshotRequest) -> operations.GetSnapshotResponse:
        r"""Download collection snapshot
        Download specified snapshot from a collection as a file
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetSnapshotRequest, base_url, '/collections/{collection_name}/snapshots/{snapshot_name}', request)
        
        
        client = self._client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetSnapshotResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/octet-stream'):
                res.get_snapshot_200_application_octet_stream_binary_string = http_res.content
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    def list_full_snapshots(self) -> operations.ListFullSnapshotsResponse:
        r"""List of storage snapshots
        Get list of snapshots of the whole storage
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/snapshots'
        
        
        client = self._client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListFullSnapshotsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListFullSnapshots200ApplicationJSON])
                res.list_full_snapshots_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    def list_snapshots(self, request: operations.ListSnapshotsRequest) -> operations.ListSnapshotsResponse:
        r"""List collection snapshots
        Get list of snapshots for a collection
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListSnapshotsRequest, base_url, '/collections/{collection_name}/snapshots', request)
        
        
        client = self._client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListSnapshotsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListSnapshots200ApplicationJSON])
                res.list_snapshots_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    def recover_from_snapshot(self, request: operations.RecoverFromSnapshotRequest) -> operations.RecoverFromSnapshotResponse:
        r"""Recover from a snapshot
        Recover local collection data from a snapshot. This will overwrite any data, stored on this node, for the collection. If collection does not exist - it will be created.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.RecoverFromSnapshotRequest, base_url, '/collections/{collection_name}/snapshots/recover', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "snapshot_recover", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.RecoverFromSnapshotRequest, request)
        
        client = self._client
        
        http_res = client.request('PUT', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RecoverFromSnapshotResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.RecoverFromSnapshot200ApplicationJSON])
                res.recover_from_snapshot_200_application_json_object = out
        elif http_res.status_code == 202:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.RecoverFromSnapshot202ApplicationJSON])
                res.recover_from_snapshot_202_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    def recover_from_uploaded_snapshot(self, request: operations.RecoverFromUploadedSnapshotRequest) -> operations.RecoverFromUploadedSnapshotResponse:
        r"""Recover from an uploaded snapshot
        Recover local collection data from an uploaded snapshot. This will overwrite any data, stored on this node, for the collection. If collection does not exist - it will be created.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.RecoverFromUploadedSnapshotRequest, base_url, '/collections/{collection_name}/snapshots/upload', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'multipart')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.RecoverFromUploadedSnapshotRequest, request)
        
        client = self._client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RecoverFromUploadedSnapshotResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.RecoverFromUploadedSnapshot200ApplicationJSON])
                res.recover_from_uploaded_snapshot_200_application_json_object = out
        elif http_res.status_code == 202:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.RecoverFromUploadedSnapshot202ApplicationJSON])
                res.recover_from_uploaded_snapshot_202_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    