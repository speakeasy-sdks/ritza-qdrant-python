# SearchBatchPointsRequest


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `search_request_batch`                                                           | [Optional[shared.SearchRequestBatch]](../../models/shared/searchrequestbatch.md) | :heavy_minus_sign:                                                               | Search batch request                                                             |
| `collection_name`                                                                | *str*                                                                            | :heavy_check_mark:                                                               | Name of the collection to search in                                              |
| `consistency`                                                                    | *Optional[Any]*                                                                  | :heavy_minus_sign:                                                               | Define read consistency guarantees for the operation                             |