# SegmentInfo

Aggregated information about segment


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `disk_usage_bytes`                                                     | *int*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `index_schema`                                                         | dict[str, [PayloadIndexInfo](../../models/shared/payloadindexinfo.md)] | :heavy_check_mark:                                                     | N/A                                                                    |
| `is_appendable`                                                        | *bool*                                                                 | :heavy_check_mark:                                                     | N/A                                                                    |
| `num_deleted_vectors`                                                  | *int*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `num_points`                                                           | *int*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `num_vectors`                                                          | *int*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `ram_usage_bytes`                                                      | *int*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `segment_type`                                                         | [SegmentType](../../models/shared/segmenttype.md)                      | :heavy_check_mark:                                                     | Type of segment                                                        |