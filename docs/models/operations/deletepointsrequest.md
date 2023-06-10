# DeletePointsRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request_body`                                                         | *Optional[Any]*                                                        | :heavy_minus_sign:                                                     | Operation to perform on points                                         |
| `collection_name`                                                      | *str*                                                                  | :heavy_check_mark:                                                     | Name of the collection to delete from                                  |
| `ordering`                                                             | [Optional[shared.WriteOrdering]](../../models/shared/writeordering.md) | :heavy_minus_sign:                                                     | define ordering guarantees for the operation                           |
| `wait`                                                                 | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | If true, wait for changes to actually happen                           |