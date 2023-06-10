# SetPayloadRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `set_payload`                                                          | [Optional[shared.SetPayload]](../../models/shared/setpayload.md)       | :heavy_minus_sign:                                                     | Set payload on points                                                  |
| `collection_name`                                                      | *str*                                                                  | :heavy_check_mark:                                                     | Name of the collection to set from                                     |
| `ordering`                                                             | [Optional[shared.WriteOrdering]](../../models/shared/writeordering.md) | :heavy_minus_sign:                                                     | define ordering guarantees for the operation                           |
| `wait`                                                                 | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | If true, wait for changes to actually happen                           |