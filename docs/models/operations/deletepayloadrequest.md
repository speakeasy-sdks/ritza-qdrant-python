# DeletePayloadRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `delete_payload`                                                       | [Optional[shared.DeletePayload]](../../models/shared/deletepayload.md) | :heavy_minus_sign:                                                     | delete payload on points                                               |
| `collection_name`                                                      | *str*                                                                  | :heavy_check_mark:                                                     | Name of the collection to delete from                                  |
| `ordering`                                                             | [Optional[shared.WriteOrdering]](../../models/shared/writeordering.md) | :heavy_minus_sign:                                                     | define ordering guarantees for the operation                           |
| `wait`                                                                 | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | If true, wait for changes to actually happen                           |