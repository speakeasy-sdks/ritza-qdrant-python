# VectorParams

Params of single vector data storage


## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `distance`                                                                                | [Distance](../../models/shared/distance.md)                                               | :heavy_check_mark:                                                                        | Type of internal tags, build from payload Distance function types used to compare vectors |
| `hnsw_config`                                                                             | *Optional[Any]*                                                                           | :heavy_minus_sign:                                                                        | Custom params for HNSW index. If none - values from collection configuration are used.    |
| `quantization_config`                                                                     | *Optional[Any]*                                                                           | :heavy_minus_sign:                                                                        | Custom params for quantization. If none - values from collection configuration are used.  |
| `size`                                                                                    | *int*                                                                                     | :heavy_check_mark:                                                                        | Size of a vectors used                                                                    |