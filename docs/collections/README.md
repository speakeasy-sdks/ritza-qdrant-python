# collections

## Overview

Searchable collections of points.

### Available Operations

* [collection_cluster_info](#collection_cluster_info) - Collection cluster info
* [create_collection](#create_collection) - Create collection
* [create_field_index](#create_field_index) - Create index for field in collection
* [create_snapshot](#create_snapshot) - Create collection snapshot
* [delete_collection](#delete_collection) - Delete collection
* [delete_field_index](#delete_field_index) - Delete index for field in collection
* [delete_snapshot](#delete_snapshot) - Delete collection snapshot
* [get_collection](#get_collection) - Collection info
* [get_collection_aliases](#get_collection_aliases) - List aliases for collection
* [get_collections](#get_collections) - List collections
* [get_collections_aliases](#get_collections_aliases) - List collections aliases
* [get_snapshot](#get_snapshot) - Download collection snapshot
* [list_snapshots](#list_snapshots) - List collection snapshots
* [recover_from_snapshot](#recover_from_snapshot) - Recover from a snapshot
* [recover_from_uploaded_snapshot](#recover_from_uploaded_snapshot) - Recover from an uploaded snapshot
* [update_aliases](#update_aliases) - Update aliases of the collections
* [update_collection](#update_collection) - Update collection parameters
* [update_collection_cluster](#update_collection_cluster) - Update collection cluster setup

## collection_cluster_info

Get cluster information for a collection

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()


req = operations.CollectionClusterInfoRequest(
    collection_name='vel',
)

res = s.collections.collection_cluster_info(req)

if res.collection_cluster_info_200_application_json_object is not None:
    # handle response
```

## create_collection

Create new collection with given parameters

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()


req = operations.CreateCollectionRequest(
    create_collection=shared.CreateCollection(
        hnsw_config='deserunt',
        init_from=shared.InitFrom(
            collection='iure',
        ),
        on_disk_payload=False,
        optimizers_config=shared.OptimizersConfigDiff(
            default_segment_number=891773,
            deleted_threshold=567.13,
            flush_interval_sec=963663,
            indexing_threshold=272656,
            max_optimization_threads=383441,
            max_segment_size=477665,
            memmap_threshold=791725,
            vacuum_min_vector_number=812169,
        ),
        quantization_config='iusto',
        replication_factor=568045,
        shard_number=392785,
        vectors=shared.VectorParams(
            distance=shared.DistanceEnum.DOT,
            hnsw_config='ab',
            quantization_config=shared.ScalarQuantization(
                scalar=shared.ScalarQuantizationConfig(
                    always_ram=False,
                    quantile=871.29,
                    type=shared.ScalarTypeEnum.INT8,
                ),
            ),
            size=648172,
        ),
        wal_config=shared.WalConfigDiff(
            wal_capacity_mb=368241,
            wal_segments_ahead=832620,
        ),
        write_consistency_factor=957156,
    ),
    collection_name='quo',
    timeout=140350,
)

res = s.collections.create_collection(req)

if res.create_collection_200_application_json_object is not None:
    # handle response
```

## create_field_index

Create index for field in collection

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()


req = operations.CreateFieldIndexRequest(
    create_field_index=shared.CreateFieldIndex(
        field_name='at',
        field_schema='maiores',
    ),
    collection_name='molestiae',
    ordering=shared.WriteOrderingEnum.STRONG,
    wait=False,
)

res = s.collections.create_field_index(req)

if res.create_field_index_200_application_json_object is not None:
    # handle response
```

## create_snapshot

Create new snapshot for a collection

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()


req = operations.CreateSnapshotRequest(
    collection_name='quod',
    wait=False,
)

res = s.collections.create_snapshot(req)

if res.create_snapshot_200_application_json_object is not None:
    # handle response
```

## delete_collection

Drop collection and all associated data

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()


req = operations.DeleteCollectionRequest(
    collection_name='esse',
    timeout=520478,
)

res = s.collections.delete_collection(req)

if res.delete_collection_200_application_json_object is not None:
    # handle response
```

## delete_field_index

Delete field index for collection

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()


req = operations.DeleteFieldIndexRequest(
    collection_name='porro',
    field_name='dolorum',
    ordering=shared.WriteOrderingEnum.WEAK,
    wait=False,
)

res = s.collections.delete_field_index(req)

if res.delete_field_index_200_application_json_object is not None:
    # handle response
```

## delete_snapshot

Delete snapshot for a collection

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()


req = operations.DeleteSnapshotRequest(
    collection_name='nam',
    snapshot_name='officia',
    wait=False,
)

res = s.collections.delete_snapshot(req)

if res.delete_snapshot_200_application_json_object is not None:
    # handle response
```

## get_collection

Get detailed information about specified existing collection

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()


req = operations.GetCollectionRequest(
    collection_name='occaecati',
)

res = s.collections.get_collection(req)

if res.get_collection_200_application_json_object is not None:
    # handle response
```

## get_collection_aliases

Get list of all aliases for a collection

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()


req = operations.GetCollectionAliasesRequest(
    collection_name='fugit',
)

res = s.collections.get_collection_aliases(req)

if res.get_collection_aliases_200_application_json_object is not None:
    # handle response
```

## get_collections

Get list name of all existing collections

### Example Usage

```python
import sdk


s = sdk.SDK()


res = s.collections.get_collections()

if res.get_collections_200_application_json_object is not None:
    # handle response
```

## get_collections_aliases

Get list of all existing collections aliases

### Example Usage

```python
import sdk


s = sdk.SDK()


res = s.collections.get_collections_aliases()

if res.get_collections_aliases_200_application_json_object is not None:
    # handle response
```

## get_snapshot

Download specified snapshot from a collection as a file

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()


req = operations.GetSnapshotRequest(
    collection_name='deleniti',
    snapshot_name='hic',
)

res = s.collections.get_snapshot(req)

if res.get_snapshot_200_application_octet_stream_binary_string is not None:
    # handle response
```

## list_snapshots

Get list of snapshots for a collection

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()


req = operations.ListSnapshotsRequest(
    collection_name='optio',
)

res = s.collections.list_snapshots(req)

if res.list_snapshots_200_application_json_object is not None:
    # handle response
```

## recover_from_snapshot

Recover local collection data from a snapshot. This will overwrite any data, stored on this node, for the collection. If collection does not exist - it will be created.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()


req = operations.RecoverFromSnapshotRequest(
    snapshot_recover=shared.SnapshotRecover(
        location='https://canine-harmonise.info',
        priority=shared.SnapshotPriorityEnum.SNAPSHOT,
    ),
    collection_name='impedit',
    wait=False,
)

res = s.collections.recover_from_snapshot(req)

if res.recover_from_snapshot_200_application_json_object is not None:
    # handle response
```

## recover_from_uploaded_snapshot

Recover local collection data from an uploaded snapshot. This will overwrite any data, stored on this node, for the collection. If collection does not exist - it will be created.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()


req = operations.RecoverFromUploadedSnapshotRequest(
    request_body=operations.RecoverFromUploadedSnapshotRequestBody(
        snapshot=operations.RecoverFromUploadedSnapshotRequestBodySnapshot(
            content='cum'.encode(),
            snapshot='esse',
        ),
    ),
    collection_name='ipsum',
    priority=shared.SnapshotPriorityEnum.REPLICA,
    wait=False,
)

res = s.collections.recover_from_uploaded_snapshot(req)

if res.recover_from_uploaded_snapshot_200_application_json_object is not None:
    # handle response
```

## update_aliases

Update aliases of the collections

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()


req = operations.UpdateAliasesRequest(
    change_aliases_operation=shared.ChangeAliasesOperation(
        actions=[
            shared.CreateAliasOperation(
                create_alias=shared.CreateAlias(
                    alias_name='ad',
                    collection_name='natus',
                ),
            ),
        ],
    ),
    timeout=149675,
)

res = s.collections.update_aliases(req)

if res.update_aliases_200_application_json_object is not None:
    # handle response
```

## update_collection

Update parameters of the existing collection

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()


req = operations.UpdateCollectionRequest(
    update_collection=shared.UpdateCollection(
        optimizers_config='dolor',
        params='laboriosam',
    ),
    collection_name='hic',
    timeout=902599,
)

res = s.collections.update_collection(req)

if res.update_collection_200_application_json_object is not None:
    # handle response
```

## update_collection_cluster

Update collection cluster setup

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()


req = operations.UpdateCollectionClusterRequest(
    request_body=shared.AbortTransferOperation(
        abort_transfer=shared.MoveShard(
            from_peer_id=449950,
            shard_id=359508,
            to_peer_id=613064,
        ),
    ),
    collection_name='iure',
    timeout=902349,
)

res = s.collections.update_collection_cluster(req)

if res.update_collection_cluster_200_application_json_object is not None:
    # handle response
```
