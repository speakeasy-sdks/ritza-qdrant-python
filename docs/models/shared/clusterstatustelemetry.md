# ClusterStatusTelemetry


## Fields

| Field                                             | Type                                              | Required                                          | Description                                       |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `commit`                                          | *int*                                             | :heavy_check_mark:                                | N/A                                               |
| `consensus_thread_status`                         | *Any*                                             | :heavy_check_mark:                                | Information about current consensus thread status |
| `is_voter`                                        | *bool*                                            | :heavy_check_mark:                                | N/A                                               |
| `number_of_peers`                                 | *int*                                             | :heavy_check_mark:                                | N/A                                               |
| `peer_id`                                         | *Optional[int]*                                   | :heavy_minus_sign:                                | N/A                                               |
| `pending_operations`                              | *int*                                             | :heavy_check_mark:                                | N/A                                               |
| `role`                                            | *Optional[Any]*                                   | :heavy_minus_sign:                                | N/A                                               |
| `term`                                            | *int*                                             | :heavy_check_mark:                                | N/A                                               |