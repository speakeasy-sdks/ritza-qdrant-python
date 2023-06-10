# RemoteShardInfo


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `peer_id`                                           | *int*                                               | :heavy_check_mark:                                  | Remote peer id                                      |
| `shard_id`                                          | *int*                                               | :heavy_check_mark:                                  | Remote shard id                                     |
| `state`                                             | [ReplicaState](../../models/shared/replicastate.md) | :heavy_check_mark:                                  | State of the single shard within a replica set.     |