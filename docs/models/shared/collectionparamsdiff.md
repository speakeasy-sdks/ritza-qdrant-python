# CollectionParamsDiff

Collection base params.  If none - values from service configuration file are used.


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `replication_factor`                                                               | *Optional[int]*                                                                    | :heavy_minus_sign:                                                                 | Number of replicas for each shard                                                  |
| `write_consistency_factor`                                                         | *Optional[int]*                                                                    | :heavy_minus_sign:                                                                 | Minimal number successful responses from replicas to consider operation successful |