# SearchPointsRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `search_request`                                                       | [Optional[shared.SearchRequest]](../../models/shared/searchrequest.md) | :heavy_minus_sign:                                                     | Search request with optional filtering                                 |
| `collection_name`                                                      | *str*                                                                  | :heavy_check_mark:                                                     | Name of the collection to search in                                    |
| `consistency`                                                          | *Optional[Any]*                                                        | :heavy_minus_sign:                                                     | Define read consistency guarantees for the operation                   |