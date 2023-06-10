# SegmentTelemetry


## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `config`                                                                                  | [SegmentConfig](../../models/shared/segmentconfig.md)                                     | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `info`                                                                                    | [SegmentInfo](../../models/shared/segmentinfo.md)                                         | :heavy_check_mark:                                                                        | Aggregated information about segment                                                      |
| `payload_field_indices`                                                                   | list[[PayloadIndexTelemetry](../../models/shared/payloadindextelemetry.md)]               | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `vector_index_searches`                                                                   | list[[VectorIndexSearchesTelemetry](../../models/shared/vectorindexsearchestelemetry.md)] | :heavy_check_mark:                                                                        | N/A                                                                                       |