# ReplicaSetTelemetry


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `id`                                                                      | *int*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `local`                                                                   | *Optional[Any]*                                                           | :heavy_minus_sign:                                                        | N/A                                                                       |
| `remote`                                                                  | list[[RemoteShardTelemetry](../../models/shared/remoteshardtelemetry.md)] | :heavy_check_mark:                                                        | N/A                                                                       |
| `replicate_states`                                                        | dict[str, [ReplicaState](../../models/shared/replicastate.md)]            | :heavy_check_mark:                                                        | N/A                                                                       |