# CollectionClusterInfo

Current clustering distribution for the collection


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `local_shards`                                                      | list[[LocalShardInfo](../../models/shared/localshardinfo.md)]       | :heavy_check_mark:                                                  | Local shards                                                        |
| `peer_id`                                                           | *int*                                                               | :heavy_check_mark:                                                  | ID of this peer                                                     |
| `remote_shards`                                                     | list[[RemoteShardInfo](../../models/shared/remoteshardinfo.md)]     | :heavy_check_mark:                                                  | Remote shards                                                       |
| `shard_count`                                                       | *int*                                                               | :heavy_check_mark:                                                  | Total number of shards                                              |
| `shard_transfers`                                                   | list[[ShardTransferInfo](../../models/shared/shardtransferinfo.md)] | :heavy_check_mark:                                                  | Shard transfers                                                     |