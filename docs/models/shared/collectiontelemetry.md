# CollectionTelemetry


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `config`                                                                | [CollectionConfig](../../models/shared/collectionconfig.md)             | :heavy_check_mark:                                                      | N/A                                                                     |
| `id`                                                                    | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `init_time_ms`                                                          | *int*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `shards`                                                                | list[[ReplicaSetTelemetry](../../models/shared/replicasettelemetry.md)] | :heavy_check_mark:                                                      | N/A                                                                     |
| `transfers`                                                             | list[[ShardTransferInfo](../../models/shared/shardtransferinfo.md)]     | :heavy_check_mark:                                                      | N/A                                                                     |