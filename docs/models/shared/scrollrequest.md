# ScrollRequest

Scroll request - paginate over all points which matches given condition


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `filter`                                                                            | *Optional[Any]*                                                                     | :heavy_minus_sign:                                                                  | Look only for points which satisfies this conditions. If not provided - all points. |
| `limit`                                                                             | *Optional[int]*                                                                     | :heavy_minus_sign:                                                                  | Page size. Default: 10                                                              |
| `offset`                                                                            | *Optional[Any]*                                                                     | :heavy_minus_sign:                                                                  | Start ID to read points from.                                                       |
| `with_payload`                                                                      | *Optional[Any]*                                                                     | :heavy_minus_sign:                                                                  | Select which payload to return with the response. Default: All                      |
| `with_vector`                                                                       | *Optional[Any]*                                                                     | :heavy_minus_sign:                                                                  | Options for specifying which vector to include                                      |