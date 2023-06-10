# RemovePeerRequest


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `force`                                                      | *Optional[bool]*                                             | :heavy_minus_sign:                                           | If true - removes peer even if it has shards/replicas on it. |
| `peer_id`                                                    | *int*                                                        | :heavy_check_mark:                                           | Id of the peer                                               |