# ScoredPoint

Search result


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `id`                                                 | *Any*                                                | :heavy_check_mark:                                   | Type, used for specifying point ID in user interface |
| `payload`                                            | *Optional[Any]*                                      | :heavy_minus_sign:                                   | Payload - values assigned to the point               |
| `score`                                              | *float*                                              | :heavy_check_mark:                                   | Points vector distance to the query vector           |
| `vector`                                             | *Optional[Any]*                                      | :heavy_minus_sign:                                   | Vector of the point                                  |
| `version`                                            | *int*                                                | :heavy_check_mark:                                   | Point version                                        |