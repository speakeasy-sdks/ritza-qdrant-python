# SegmentConfig


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `index`                                                                | *Any*                                                                  | :heavy_check_mark:                                                     | Vector index configuration of the segment                              |
| `payload_storage_type`                                                 | *Optional[Any]*                                                        | :heavy_minus_sign:                                                     | Type of payload storage                                                |
| `quantization_config`                                                  | *Optional[Any]*                                                        | :heavy_minus_sign:                                                     | Quantization parameters. If none - quantization is disabled.           |
| `storage_type`                                                         | *Any*                                                                  | :heavy_check_mark:                                                     | Type of vector storage                                                 |
| `vector_data`                                                          | dict[str, [VectorDataConfig](../../models/shared/vectordataconfig.md)] | :heavy_check_mark:                                                     | N/A                                                                    |