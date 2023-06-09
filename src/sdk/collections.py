"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from sdk import utils
from sdk.models import operations, shared
from typing import Optional

class Collections:
    r"""Searchable collections of points."""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def collection_cluster_info(self, request: operations.CollectionClusterInfoRequest) -> operations.CollectionClusterInfoResponse:
        r"""Collection cluster info
        Get cluster information for a collection
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.CollectionClusterInfoRequest, base_url, '/collections/{collection_name}/cluster', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CollectionClusterInfoResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CollectionClusterInfo200ApplicationJSON])
                res.collection_cluster_info_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    
    def create_collection(self, request: operations.CreateCollectionRequest) -> operations.CreateCollectionResponse:
        r"""Create collection
        Create new collection with given parameters
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.CreateCollectionRequest, base_url, '/collections/{collection_name}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "create_collection", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.CreateCollectionRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('PUT', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateCollectionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateCollection200ApplicationJSON])
                res.create_collection_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    
    def create_field_index(self, request: operations.CreateFieldIndexRequest) -> operations.CreateFieldIndexResponse:
        r"""Create index for field in collection
        Create index for field in collection
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.CreateFieldIndexRequest, base_url, '/collections/{collection_name}/index', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "create_field_index", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.CreateFieldIndexRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('PUT', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateFieldIndexResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateFieldIndex200ApplicationJSON])
                res.create_field_index_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    
    def create_snapshot(self, request: operations.CreateSnapshotRequest) -> operations.CreateSnapshotResponse:
        r"""Create collection snapshot
        Create new snapshot for a collection
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.CreateSnapshotRequest, base_url, '/collections/{collection_name}/snapshots', request)
        headers = {}
        query_params = utils.get_query_params(operations.CreateSnapshotRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0.7, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, params=query_params, headers=headers)
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

    
    def delete_collection(self, request: operations.DeleteCollectionRequest) -> operations.DeleteCollectionResponse:
        r"""Delete collection
        Drop collection and all associated data
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteCollectionRequest, base_url, '/collections/{collection_name}', request)
        headers = {}
        query_params = utils.get_query_params(operations.DeleteCollectionRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('DELETE', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteCollectionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeleteCollection200ApplicationJSON])
                res.delete_collection_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    
    def delete_field_index(self, request: operations.DeleteFieldIndexRequest) -> operations.DeleteFieldIndexResponse:
        r"""Delete index for field in collection
        Delete field index for collection
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteFieldIndexRequest, base_url, '/collections/{collection_name}/index/{field_name}', request)
        headers = {}
        query_params = utils.get_query_params(operations.DeleteFieldIndexRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('DELETE', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteFieldIndexResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeleteFieldIndex200ApplicationJSON])
                res.delete_field_index_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    
    def delete_snapshot(self, request: operations.DeleteSnapshotRequest) -> operations.DeleteSnapshotResponse:
        r"""Delete collection snapshot
        Delete snapshot for a collection
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteSnapshotRequest, base_url, '/collections/{collection_name}/snapshots/{snapshot_name}', request)
        headers = {}
        query_params = utils.get_query_params(operations.DeleteSnapshotRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0.7, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('DELETE', url, params=query_params, headers=headers)
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

    
    def get_collection(self, request: operations.GetCollectionRequest) -> operations.GetCollectionResponse:
        r"""Collection info
        Get detailed information about specified existing collection
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetCollectionRequest, base_url, '/collections/{collection_name}', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCollectionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCollection200ApplicationJSON])
                res.get_collection_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    
    def get_collection_aliases(self, request: operations.GetCollectionAliasesRequest) -> operations.GetCollectionAliasesResponse:
        r"""List aliases for collection
        Get list of all aliases for a collection
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetCollectionAliasesRequest, base_url, '/collections/{collection_name}/aliases', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCollectionAliasesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCollectionAliases200ApplicationJSON])
                res.get_collection_aliases_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    
    def get_collections(self) -> operations.GetCollectionsResponse:
        r"""List collections
        Get list name of all existing collections
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/collections'
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCollectionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCollections200ApplicationJSON])
                res.get_collections_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    
    def get_collections_aliases(self) -> operations.GetCollectionsAliasesResponse:
        r"""List collections aliases
        Get list of all existing collections aliases
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/aliases'
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCollectionsAliasesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetCollectionsAliases200ApplicationJSON])
                res.get_collections_aliases_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    
    def get_snapshot(self, request: operations.GetSnapshotRequest) -> operations.GetSnapshotResponse:
        r"""Download collection snapshot
        Download specified snapshot from a collection as a file
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetSnapshotRequest, base_url, '/collections/{collection_name}/snapshots/{snapshot_name}', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/octet-stream;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
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

    
    def list_snapshots(self, request: operations.ListSnapshotsRequest) -> operations.ListSnapshotsResponse:
        r"""List collection snapshots
        Get list of snapshots for a collection
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ListSnapshotsRequest, base_url, '/collections/{collection_name}/snapshots', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
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
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.RecoverFromSnapshotRequest, base_url, '/collections/{collection_name}/snapshots/recover', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "snapshot_recover", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.RecoverFromSnapshotRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0.7, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
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
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.RecoverFromUploadedSnapshotRequest, base_url, '/collections/{collection_name}/snapshots/upload', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'multipart')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.RecoverFromUploadedSnapshotRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0.7, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
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

    
    def update_aliases(self, request: operations.UpdateAliasesRequest) -> operations.UpdateAliasesResponse:
        r"""Update aliases of the collections"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/collections/aliases'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "change_aliases_operation", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.UpdateAliasesRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateAliasesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UpdateAliases200ApplicationJSON])
                res.update_aliases_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    
    def update_collection(self, request: operations.UpdateCollectionRequest) -> operations.UpdateCollectionResponse:
        r"""Update collection parameters
        Update parameters of the existing collection
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.UpdateCollectionRequest, base_url, '/collections/{collection_name}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "update_collection", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.UpdateCollectionRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('PATCH', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateCollectionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UpdateCollection200ApplicationJSON])
                res.update_collection_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    
    def update_collection_cluster(self, request: operations.UpdateCollectionClusterRequest) -> operations.UpdateCollectionClusterResponse:
        r"""Update collection cluster setup"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.UpdateCollectionClusterRequest, base_url, '/collections/{collection_name}/cluster', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.UpdateCollectionClusterRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateCollectionClusterResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UpdateCollectionCluster200ApplicationJSON])
                res.update_collection_cluster_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    