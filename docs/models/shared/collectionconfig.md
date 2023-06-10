# CollectionConfig


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `hnsw_config`                                               | [HnswConfig](../../models/shared/hnswconfig.md)             | :heavy_check_mark:                                          | Config of HNSW index                                        |
| `optimizer_config`                                          | [OptimizersConfig](../../models/shared/optimizersconfig.md) | :heavy_check_mark:                                          | N/A                                                         |
| `params`                                                    | [CollectionParams](../../models/shared/collectionparams.md) | :heavy_check_mark:                                          | N/A                                                         |
| `quantization_config`                                       | *Optional[Any]*                                             | :heavy_minus_sign:                                          | N/A                                                         |
| `wal_config`                                                | [WalConfig](../../models/shared/walconfig.md)               | :heavy_check_mark:                                          | N/A                                                         |