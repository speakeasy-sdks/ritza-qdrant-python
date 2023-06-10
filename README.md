# ritza-qdrant-test

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/ritza-qdrant-python.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import sdk


s = sdk.SDK()


res = s.cluster.cluster_status()

if res.cluster_status_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [cluster](docs/sdks/cluster/README.md)

* [cluster_status](docs/sdks/cluster/README.md#cluster_status) - Get cluster status info
* [collection_cluster_info](docs/sdks/cluster/README.md#collection_cluster_info) - Collection cluster info
* [recover_current_peer](docs/sdks/cluster/README.md#recover_current_peer) - Tries to recover current peer Raft state.
* [remove_peer](docs/sdks/cluster/README.md#remove_peer) - Remove peer from the cluster
* [update_collection_cluster](docs/sdks/cluster/README.md#update_collection_cluster) - Update collection cluster setup

### [collections](docs/sdks/collections/README.md)

* [collection_cluster_info](docs/sdks/collections/README.md#collection_cluster_info) - Collection cluster info
* [create_collection](docs/sdks/collections/README.md#create_collection) - Create collection
* [create_field_index](docs/sdks/collections/README.md#create_field_index) - Create index for field in collection
* [create_snapshot](docs/sdks/collections/README.md#create_snapshot) - Create collection snapshot
* [delete_collection](docs/sdks/collections/README.md#delete_collection) - Delete collection
* [delete_field_index](docs/sdks/collections/README.md#delete_field_index) - Delete index for field in collection
* [delete_snapshot](docs/sdks/collections/README.md#delete_snapshot) - Delete collection snapshot
* [get_collection](docs/sdks/collections/README.md#get_collection) - Collection info
* [get_collection_aliases](docs/sdks/collections/README.md#get_collection_aliases) - List aliases for collection
* [get_collections](docs/sdks/collections/README.md#get_collections) - List collections
* [get_collections_aliases](docs/sdks/collections/README.md#get_collections_aliases) - List collections aliases
* [get_snapshot](docs/sdks/collections/README.md#get_snapshot) - Download collection snapshot
* [list_snapshots](docs/sdks/collections/README.md#list_snapshots) - List collection snapshots
* [recover_from_snapshot](docs/sdks/collections/README.md#recover_from_snapshot) - Recover from a snapshot
* [recover_from_uploaded_snapshot](docs/sdks/collections/README.md#recover_from_uploaded_snapshot) - Recover from an uploaded snapshot
* [update_aliases](docs/sdks/collections/README.md#update_aliases) - Update aliases of the collections
* [update_collection](docs/sdks/collections/README.md#update_collection) - Update collection parameters
* [update_collection_cluster](docs/sdks/collections/README.md#update_collection_cluster) - Update collection cluster setup

### [points](docs/sdks/points/README.md)

* [clear_payload](docs/sdks/points/README.md#clear_payload) - Clear payload
* [count_points](docs/sdks/points/README.md#count_points) - Count points
* [delete_payload](docs/sdks/points/README.md#delete_payload) - Delete payload
* [delete_points](docs/sdks/points/README.md#delete_points) - Delete points
* [get_point](docs/sdks/points/README.md#get_point) - Get point
* [get_points](docs/sdks/points/README.md#get_points) - Get points
* [overwrite_payload](docs/sdks/points/README.md#overwrite_payload) - Overwrite payload
* [recommend_batch_points](docs/sdks/points/README.md#recommend_batch_points) - Recommend batch points
* [recommend_points](docs/sdks/points/README.md#recommend_points) - Recommend points
* [scroll_points](docs/sdks/points/README.md#scroll_points) - Scroll points
* [search_batch_points](docs/sdks/points/README.md#search_batch_points) - Search batch points
* [search_points](docs/sdks/points/README.md#search_points) - Search points
* [set_payload](docs/sdks/points/README.md#set_payload) - Set payload
* [upsert_points](docs/sdks/points/README.md#upsert_points) - Upsert points

### [service](docs/sdks/service/README.md)

* [get_locks](docs/sdks/service/README.md#get_locks) - Get lock options
* [metrics](docs/sdks/service/README.md#metrics) - Collect Prometheus metrics data
* [post_locks](docs/sdks/service/README.md#post_locks) - Set lock options
* [telemetry](docs/sdks/service/README.md#telemetry) - Collect telemetry data

### [snapshots](docs/sdks/snapshots/README.md)

* [create_full_snapshot](docs/sdks/snapshots/README.md#create_full_snapshot) - Create storage snapshot
* [create_snapshot](docs/sdks/snapshots/README.md#create_snapshot) - Create collection snapshot
* [delete_full_snapshot](docs/sdks/snapshots/README.md#delete_full_snapshot) - Delete storage snapshot
* [delete_snapshot](docs/sdks/snapshots/README.md#delete_snapshot) - Delete collection snapshot
* [get_full_snapshot](docs/sdks/snapshots/README.md#get_full_snapshot) - Download storage snapshot
* [get_snapshot](docs/sdks/snapshots/README.md#get_snapshot) - Download collection snapshot
* [list_full_snapshots](docs/sdks/snapshots/README.md#list_full_snapshots) - List of storage snapshots
* [list_snapshots](docs/sdks/snapshots/README.md#list_snapshots) - List collection snapshots
* [recover_from_snapshot](docs/sdks/snapshots/README.md#recover_from_snapshot) - Recover from a snapshot
* [recover_from_uploaded_snapshot](docs/sdks/snapshots/README.md#recover_from_uploaded_snapshot) - Recover from an uploaded snapshot
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
