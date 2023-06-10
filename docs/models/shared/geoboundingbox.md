# GeoBoundingBox

Geo filter request

Matches coordinates inside the rectangle, described by coordinates of lop-left and bottom-right edges


## Fields

| Field                                       | Type                                        | Required                                    | Description                                 |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| `bottom_right`                              | [GeoPoint](../../models/shared/geopoint.md) | :heavy_check_mark:                          | Geo point payload schema                    |
| `top_left`                                  | [GeoPoint](../../models/shared/geopoint.md) | :heavy_check_mark:                          | Geo point payload schema                    |