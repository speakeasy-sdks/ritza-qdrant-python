# DeleteFieldIndexRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `collection_name`                                                      | *str*                                                                  | :heavy_check_mark:                                                     | Name of the collection                                                 |
| `field_name`                                                           | *str*                                                                  | :heavy_check_mark:                                                     | Name of the field where to delete the index                            |
| `ordering`                                                             | [Optional[shared.WriteOrdering]](../../models/shared/writeordering.md) | :heavy_minus_sign:                                                     | define ordering guarantees for the operation                           |
| `wait`                                                                 | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | If true, wait for changes to actually happen                           |