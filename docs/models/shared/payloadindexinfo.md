# PayloadIndexInfo

Display payload field type & index information


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `data_type`                                                   | [PayloadSchemaType](../../models/shared/payloadschematype.md) | :heavy_check_mark:                                            | All possible names of payload types                           |
| `params`                                                      | *Optional[Any]*                                               | :heavy_minus_sign:                                            | N/A                                                           |
| `points`                                                      | *int*                                                         | :heavy_check_mark:                                            | Number of points indexed with this index                      |