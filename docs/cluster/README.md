# cluster

## Overview

Service distributed setup

### Available Operations

* [cluster_status](#cluster_status) - Get cluster status info
* [collection_cluster_info](#collection_cluster_info) - Collection cluster info
* [recover_current_peer](#recover_current_peer) - Tries to recover current peer Raft state.
* [remove_peer](#remove_peer) - Remove peer from the cluster
* [update_collection_cluster](#update_collection_cluster) - Update collection cluster setup

## cluster_status

Get information about the current state and composition of the cluster

### Example Usage

```python
import sdk


s = sdk.SDK()


res = s.cluster.cluster_status()

if res.cluster_status_200_application_json_object is not None:
    # handle response
```

## collection_cluster_info

Get cluster information for a collection

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()

req = operations.CollectionClusterInfoRequest(
    collection_name='corrupti',
)

res = s.cluster.collection_cluster_info(req)

if res.collection_cluster_info_200_application_json_object is not None:
    # handle response
```

## recover_current_peer

Tries to recover current peer Raft state.

### Example Usage

```python
import sdk


s = sdk.SDK()


res = s.cluster.recover_current_peer()

if res.recover_current_peer_200_application_json_object is not None:
    # handle response
```

## remove_peer

Tries to remove peer from the cluster. Will return an error if peer has shards on it.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()

req = operations.RemovePeerRequest(
    force=False,
    peer_id=592845,
)

res = s.cluster.remove_peer(req)

if res.remove_peer_200_application_json_object is not None:
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
            from_peer_id=844266,
            shard_id=602763,
            to_peer_id=857946,
        ),
    ),
    collection_name='corrupti',
    timeout=847252,
)

res = s.cluster.update_collection_cluster(req)

if res.update_collection_cluster_200_application_json_object is not None:
    # handle response
```
