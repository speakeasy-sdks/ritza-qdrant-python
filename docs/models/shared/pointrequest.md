# PointRequest

List of points to retrieve


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `ids`                                                          | list[*Any*]                                                    | :heavy_check_mark:                                             | Look for points with ids                                       |
| `with_payload`                                                 | *Optional[Any]*                                                | :heavy_minus_sign:                                             | Select which payload to return with the response. Default: All |
| `with_vector`                                                  | *Optional[Any]*                                                | :heavy_minus_sign:                                             | Options for specifying which vector to include                 |