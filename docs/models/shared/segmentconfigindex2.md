# SegmentConfigIndex2

Use filterable HNSW index for approximate search. Is very fast even on a very huge collections, but require additional space to store index and additional time to build it.


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `options`                                                                 | [HnswConfig](../../models/shared/hnswconfig.md)                           | :heavy_check_mark:                                                        | Config of HNSW index                                                      |
| `type`                                                                    | [SegmentConfigIndex2Type](../../models/shared/segmentconfigindex2type.md) | :heavy_check_mark:                                                        | N/A                                                                       |