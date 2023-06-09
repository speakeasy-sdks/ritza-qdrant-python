# snapshots

## Overview

Storage and collections snapshots

### Available Operations

* [create_full_snapshot](#create_full_snapshot) - Create storage snapshot
* [create_snapshot](#create_snapshot) - Create collection snapshot
* [delete_full_snapshot](#delete_full_snapshot) - Delete storage snapshot
* [delete_snapshot](#delete_snapshot) - Delete collection snapshot
* [get_full_snapshot](#get_full_snapshot) - Download storage snapshot
* [get_snapshot](#get_snapshot) - Download collection snapshot
* [list_full_snapshots](#list_full_snapshots) - List of storage snapshots
* [list_snapshots](#list_snapshots) - List collection snapshots
* [recover_from_snapshot](#recover_from_snapshot) - Recover from a snapshot
* [recover_from_uploaded_snapshot](#recover_from_uploaded_snapshot) - Recover from an uploaded snapshot

## create_full_snapshot

Create new snapshot of the whole storage

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()

req = operations.CreateFullSnapshotRequest(
    wait=False,
)

res = s.snapshots.create_full_snapshot(req)

if res.create_full_snapshot_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateFullSnapshotRequest](../../models/operations/createfullsnapshotrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.CreateFullSnapshotResponse](../../models/operations/createfullsnapshotresponse.md)**


## create_snapshot

Create new snapshot for a collection

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()

req = operations.CreateSnapshotRequest(
    collection_name='nesciunt',
    wait=False,
)

res = s.snapshots.create_snapshot(req)

if res.create_snapshot_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateSnapshotRequest](../../models/operations/createsnapshotrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.CreateSnapshotResponse](../../models/operations/createsnapshotresponse.md)**


## delete_full_snapshot

Delete snapshot of the whole storage

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()

req = operations.DeleteFullSnapshotRequest(
    snapshot_name='quaerat',
    wait=False,
)

res = s.snapshots.delete_full_snapshot(req)

if res.delete_full_snapshot_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.DeleteFullSnapshotRequest](../../models/operations/deletefullsnapshotrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.DeleteFullSnapshotResponse](../../models/operations/deletefullsnapshotresponse.md)**


## delete_snapshot

Delete snapshot for a collection

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()

req = operations.DeleteSnapshotRequest(
    collection_name='itaque',
    snapshot_name='minus',
    wait=False,
)

res = s.snapshots.delete_snapshot(req)

if res.delete_snapshot_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.DeleteSnapshotRequest](../../models/operations/deletesnapshotrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.DeleteSnapshotResponse](../../models/operations/deletesnapshotresponse.md)**


## get_full_snapshot

Download specified snapshot of the whole storage as a file

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()

req = operations.GetFullSnapshotRequest(
    snapshot_name='sunt',
)

res = s.snapshots.get_full_snapshot(req)

if res.get_full_snapshot_200_application_octet_stream_binary_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetFullSnapshotRequest](../../models/operations/getfullsnapshotrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetFullSnapshotResponse](../../models/operations/getfullsnapshotresponse.md)**


## get_snapshot

Download specified snapshot from a collection as a file

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()

req = operations.GetSnapshotRequest(
    collection_name='distinctio',
    snapshot_name='iusto',
)

res = s.snapshots.get_snapshot(req)

if res.get_snapshot_200_application_octet_stream_binary_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetSnapshotRequest](../../models/operations/getsnapshotrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetSnapshotResponse](../../models/operations/getsnapshotresponse.md)**


## list_full_snapshots

Get list of snapshots of the whole storage

### Example Usage

```python
import sdk


s = sdk.SDK()


res = s.snapshots.list_full_snapshots()

if res.list_full_snapshots_200_application_json_object is not None:
    # handle response
```


### Response

**[operations.ListFullSnapshotsResponse](../../models/operations/listfullsnapshotsresponse.md)**


## list_snapshots

Get list of snapshots for a collection

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()

req = operations.ListSnapshotsRequest(
    collection_name='quas',
)

res = s.snapshots.list_snapshots(req)

if res.list_snapshots_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListSnapshotsRequest](../../models/operations/listsnapshotsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.ListSnapshotsResponse](../../models/operations/listsnapshotsresponse.md)**


## recover_from_snapshot

Recover local collection data from a snapshot. This will overwrite any data, stored on this node, for the collection. If collection does not exist - it will be created.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()

req = operations.RecoverFromSnapshotRequest(
    snapshot_recover=shared.SnapshotRecover(
        location='http://rotten-cuff-link.info',
        priority='alias',
    ),
    collection_name='rem',
    wait=False,
)

res = s.snapshots.recover_from_snapshot(req)

if res.recover_from_snapshot_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.RecoverFromSnapshotRequest](../../models/operations/recoverfromsnapshotrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.RecoverFromSnapshotResponse](../../models/operations/recoverfromsnapshotresponse.md)**


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
            content='aut'.encode(),
            snapshot='quos',
        ),
    ),
    collection_name='laudantium',
    priority=shared.SnapshotPriority.REPLICA,
    wait=False,
)

res = s.snapshots.recover_from_uploaded_snapshot(req)

if res.recover_from_uploaded_snapshot_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.RecoverFromUploadedSnapshotRequest](../../models/operations/recoverfromuploadedsnapshotrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.RecoverFromUploadedSnapshotResponse](../../models/operations/recoverfromuploadedsnapshotresponse.md)**

