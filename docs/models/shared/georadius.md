# GeoRadius

Geo filter request

Matches coordinates inside the circle of `radius` and center with coordinates `center`


## Fields

| Field                                       | Type                                        | Required                                    | Description                                 |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| `center`                                    | [GeoPoint](../../models/shared/geopoint.md) | :heavy_check_mark:                          | Geo point payload schema                    |
| `radius`                                    | *float*                                     | :heavy_check_mark:                          | Radius of the area in meters                |