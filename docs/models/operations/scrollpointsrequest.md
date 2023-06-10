# ScrollPointsRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `scroll_request`                                                       | [Optional[shared.ScrollRequest]](../../models/shared/scrollrequest.md) | :heavy_minus_sign:                                                     | Pagination and filter parameters                                       |
| `collection_name`                                                      | *str*                                                                  | :heavy_check_mark:                                                     | Name of the collection to retrieve from                                |
| `consistency`                                                          | *Optional[Any]*                                                        | :heavy_minus_sign:                                                     | Define read consistency guarantees for the operation                   |