# TextIndexParams

Payload type with parameters


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `lowercase`                                                     | *Optional[bool]*                                                | :heavy_minus_sign:                                              | If true, lowercase all tokens. Default: true                    |
| `max_token_len`                                                 | *Optional[int]*                                                 | :heavy_minus_sign:                                              | N/A                                                             |
| `min_token_len`                                                 | *Optional[int]*                                                 | :heavy_minus_sign:                                              | N/A                                                             |
| `tokenizer`                                                     | [Optional[TokenizerType]](../../models/shared/tokenizertype.md) | :heavy_minus_sign:                                              | N/A                                                             |
| `type`                                                          | [TextIndexType](../../models/shared/textindextype.md)           | :heavy_check_mark:                                              | N/A                                                             |