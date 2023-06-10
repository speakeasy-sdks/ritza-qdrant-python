# CreateFieldIndexRequest


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `create_field_index`                                                         | [Optional[shared.CreateFieldIndex]](../../models/shared/createfieldindex.md) | :heavy_minus_sign:                                                           | Field name                                                                   |
| `collection_name`                                                            | *str*                                                                        | :heavy_check_mark:                                                           | Name of the collection                                                       |
| `ordering`                                                                   | [Optional[shared.WriteOrdering]](../../models/shared/writeordering.md)       | :heavy_minus_sign:                                                           | define ordering guarantees for the operation                                 |
| `wait`                                                                       | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | If true, wait for changes to actually happen                                 |