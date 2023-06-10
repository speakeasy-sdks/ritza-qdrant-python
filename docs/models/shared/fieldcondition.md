# FieldCondition

All possible payload filtering conditions


## Fields

| Field                                             | Type                                              | Required                                          | Description                                       |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `geo_bounding_box`                                | *Optional[Any]*                                   | :heavy_minus_sign:                                | Check if points geo location lies in a given area |
| `geo_radius`                                      | *Optional[Any]*                                   | :heavy_minus_sign:                                | Check if geo point is within a given radius       |
| `key`                                             | *str*                                             | :heavy_check_mark:                                | Payload key                                       |
| `match`                                           | *Optional[Any]*                                   | :heavy_minus_sign:                                | Check if point has field with a given value       |
| `range`                                           | *Optional[Any]*                                   | :heavy_minus_sign:                                | Check if points value lies in a given range       |
| `values_count`                                    | *Optional[Any]*                                   | :heavy_minus_sign:                                | Check number of values of the field               |