"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from .cluster import Cluster
from .collections import Collections
from .points import Points
from .service import Service
from .snapshots import Snapshots

SERVERS = [
    "https://localhost:8080",
]
"""Contains the list of servers available to the SDK"""

class SDK:
    r"""API description for Qdrant vector search engine.
    
    This document describes CRUD and search operations on collections of points (vectors with payload).
    
    Qdrant supports any combinations of `should`, `must` and `must_not` conditions, which makes it possible to use in applications when object could not be described solely by vector. It could be location features, availability flags, and other custom properties businesses should take into account.
    ## Examples
    This examples cover the most basic use-cases - collection creation and basic vector search.
    ### Create collection
    First - let's create a collection with dot-production metric.
    ```
    curl -X PUT 'http://localhost:6333/collections/test_collection' \
      -H 'Content-Type: application/json' \
      --data-raw '{
        \"vectors\": {
          \"size\": 4,
          \"distance\": \"Dot\"
        }
      }'
    
    ```
    Expected response:
    ```
    {
        \"result\": true,
        \"status\": \"ok\",
        \"time\": 0.031095451
    }
    ```
    We can ensure that collection was created:
    ```
    curl 'http://localhost:6333/collections/test_collection'
    ```
    Expected response:
    ```
    {
      \"result\": {
        \"status\": \"green\",
        \"vectors_count\": 0,
        \"segments_count\": 5,
        \"disk_data_size\": 0,
        \"ram_data_size\": 0,
        \"config\": {
          \"params\": {
            \"vectors\": {
              \"size\": 4,
              \"distance\": \"Dot\"
            }
          },
          \"hnsw_config\": {
            \"m\": 16,
            \"ef_construct\": 100,
            \"full_scan_threshold\": 10000
          },
          \"optimizer_config\": {
            \"deleted_threshold\": 0.2,
            \"vacuum_min_vector_number\": 1000,
            \"max_segment_number\": 5,
            \"memmap_threshold\": 50000,
            \"indexing_threshold\": 20000,
            \"flush_interval_sec\": 1
          },
          \"wal_config\": {
            \"wal_capacity_mb\": 32,
            \"wal_segments_ahead\": 0
          }
        }
      },
      \"status\": \"ok\",
      \"time\": 2.1199e-05
    }
    ```
    
    ### Add points
    Let's now add vectors with some payload:
    ```
    curl -L -X PUT 'http://localhost:6333/collections/test_collection/points?wait=true' \ -H 'Content-Type: application/json' \ --data-raw '{
      \"points\": [
        {\"id\": 1, \"vector\": [0.05, 0.61, 0.76, 0.74], \"payload\": {\"city\": \"Berlin\"}},
        {\"id\": 2, \"vector\": [0.19, 0.81, 0.75, 0.11], \"payload\": {\"city\": [\"Berlin\", \"London\"] }},
        {\"id\": 3, \"vector\": [0.36, 0.55, 0.47, 0.94], \"payload\": {\"city\": [\"Berlin\", \"Moscow\"] }},
        {\"id\": 4, \"vector\": [0.18, 0.01, 0.85, 0.80], \"payload\": {\"city\": [\"London\", \"Moscow\"] }},
        {\"id\": 5, \"vector\": [0.24, 0.18, 0.22, 0.44], \"payload\": {\"count\": [0]}},
        {\"id\": 6, \"vector\": [0.35, 0.08, 0.11, 0.44]}
      ]
    }'
    ```
    Expected response:
    ```
    {
        \"result\": {
            \"operation_id\": 0,
            \"status\": \"completed\"
        },
        \"status\": \"ok\",
        \"time\": 0.000206061
    }
    ```
    ### Search with filtering
    Let's start with a basic request:
    ```
    curl -L -X POST 'http://localhost:6333/collections/test_collection/points/search' \ -H 'Content-Type: application/json' \ --data-raw '{
        \"vector\": [0.2,0.1,0.9,0.7],
        \"top\": 3
    }'
    ```
    Expected response:
    ```
    {
        \"result\": [
            { \"id\": 4, \"score\": 1.362, \"payload\": null, \"version\": 0 },
            { \"id\": 1, \"score\": 1.273, \"payload\": null, \"version\": 0 },
            { \"id\": 3, \"score\": 1.208, \"payload\": null, \"version\": 0 }
        ],
        \"status\": \"ok\",
        \"time\": 0.000055785
    }
    ```
    But result is different if we add a filter:
    ```
    curl -L -X POST 'http://localhost:6333/collections/test_collection/points/search' \ -H 'Content-Type: application/json' \ --data-raw '{
        \"filter\": {
            \"should\": [
                {
                    \"key\": \"city\",
                    \"match\": {
                        \"value\": \"London\"
                    }
                }
            ]
        },
        \"vector\": [0.2, 0.1, 0.9, 0.7],
        \"top\": 3
    }'
    ```
    Expected response:
    ```
    {
        \"result\": [
            { \"id\": 4, \"score\": 1.362, \"payload\": null, \"version\": 0 },
            { \"id\": 2, \"score\": 0.871, \"payload\": null, \"version\": 0 }
        ],
        \"status\": \"ok\",
        \"time\": 0.000093972
    }
    ```
    https://qdrant.tech/documentation/ - Find out more about Qdrant applications and demo
    """
    cluster: Cluster
    r"""Service distributed setup"""
    collections: Collections
    r"""Searchable collections of points."""
    points: Points
    r"""Float-point vectors with payload."""
    service: Service
    r"""Service management"""
    snapshots: Snapshots
    r"""Storage and collections snapshots"""

    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "1.2.0"
    _gen_version: str = "2.23.2"

    def __init__(self,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session        
        """
        self._client = requests_http.Session()
        
        
        if server_url is not None:
            if url_params is not None:
                self._server_url = utils.template_url(server_url, url_params)
            else:
                self._server_url = server_url

        if client is not None:
            self._client = client
        
        self._security_client = self._client
        

        self._init_sdks()
    
    def _init_sdks(self):
        self.cluster = Cluster(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.collections = Collections(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.points = Points(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.service = Service(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.snapshots = Snapshots(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    