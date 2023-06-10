# ValuesCount

Values count filter request


## Fields

| Field                                  | Type                                   | Required                               | Description                            |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `gt`                                   | *Optional[int]*                        | :heavy_minus_sign:                     | point.key.length() > values_count.gt   |
| `gte`                                  | *Optional[int]*                        | :heavy_minus_sign:                     | point.key.length() >= values_count.gte |
| `lt`                                   | *Optional[int]*                        | :heavy_minus_sign:                     | point.key.length() < values_count.lt   |
| `lte`                                  | *Optional[int]*                        | :heavy_minus_sign:                     | point.key.length() <= values_count.lte |