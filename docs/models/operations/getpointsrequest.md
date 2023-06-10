# GetPointsRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `point_request`                                                      | [Optional[shared.PointRequest]](../../models/shared/pointrequest.md) | :heavy_minus_sign:                                                   | List of points to retrieve                                           |
| `collection_name`                                                    | *str*                                                                | :heavy_check_mark:                                                   | Name of the collection to retrieve from                              |
| `consistency`                                                        | *Optional[Any]*                                                      | :heavy_minus_sign:                                                   | Define read consistency guarantees for the operation                 |