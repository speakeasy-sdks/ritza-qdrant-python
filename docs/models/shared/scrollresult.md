# ScrollResult

Result of the points read request


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `next_page_offset`                                         | *Optional[Any]*                                            | :heavy_minus_sign:                                         | Offset which should be used to retrieve a next page result |
| `points`                                                   | list[[Record](../../models/shared/record.md)]              | :heavy_check_mark:                                         | List of retrieved points                                   |