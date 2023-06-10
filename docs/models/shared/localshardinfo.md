# LocalShardInfo


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `points_count`                                      | *int*                                               | :heavy_check_mark:                                  | Number of points in the shard                       |
| `shard_id`                                          | *int*                                               | :heavy_check_mark:                                  | Local shard id                                      |
| `state`                                             | [ReplicaState](../../models/shared/replicastate.md) | :heavy_check_mark:                                  | State of the single shard within a replica set.     |