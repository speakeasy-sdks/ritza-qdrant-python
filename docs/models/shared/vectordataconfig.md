# VectorDataConfig

Config of single vector data storage


## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `distance`                                                                                | [Distance](../../models/shared/distance.md)                                               | :heavy_check_mark:                                                                        | Type of internal tags, build from payload Distance function types used to compare vectors |
| `hnsw_config`                                                                             | *Optional[Any]*                                                                           | :heavy_minus_sign:                                                                        | Vector specific HNSW config that overrides collection config                              |
| `quantization_config`                                                                     | *Optional[Any]*                                                                           | :heavy_minus_sign:                                                                        | Vector specific quantization config that overrides collection config                      |
| `size`                                                                                    | *int*                                                                                     | :heavy_check_mark:                                                                        | Size of a vectors used                                                                    |