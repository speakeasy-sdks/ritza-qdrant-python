# RecommendPointsRequest


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `recommend_request`                                                          | [Optional[shared.RecommendRequest]](../../models/shared/recommendrequest.md) | :heavy_minus_sign:                                                           | Request points based on positive and negative examples.                      |
| `collection_name`                                                            | *str*                                                                        | :heavy_check_mark:                                                           | Name of the collection to search in                                          |
| `consistency`                                                                | *Optional[Any]*                                                              | :heavy_minus_sign:                                                           | Define read consistency guarantees for the operation                         |