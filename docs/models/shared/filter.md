# Filter

Look only for points which satisfies this conditions


## Fields

| Field                                         | Type                                          | Required                                      | Description                                   |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `must`                                        | list[*Any*]                                   | :heavy_minus_sign:                            | All conditions must match                     |
| `must_not`                                    | list[*Any*]                                   | :heavy_minus_sign:                            | All conditions must NOT match                 |
| `should`                                      | list[*Any*]                                   | :heavy_minus_sign:                            | At least one of those conditions should match |