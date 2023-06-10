# LookupLocation

Defines a location to use for looking up the vector. Specifies collection and vector field name.


## Fields

| Field                                                                                                            | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `collection`                                                                                                     | *str*                                                                                                            | :heavy_check_mark:                                                                                               | Name of the collection used for lookup                                                                           |
| `vector`                                                                                                         | *Optional[str]*                                                                                                  | :heavy_minus_sign:                                                                                               | Optional name of the vector field within the collection. If not provided, the default vector field will be used. |