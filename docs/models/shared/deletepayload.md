# DeletePayload

delete payload on points


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `filter`                                                      | *Optional[Any]*                                               | :heavy_minus_sign:                                            | Deletes values from points that satisfy this filter condition |
| `keys`                                                        | list[*str*]                                                   | :heavy_check_mark:                                            | List of payload keys to remove from payload                   |
| `points`                                                      | list[*Any*]                                                   | :heavy_minus_sign:                                            | Deletes values from each point in this list                   |