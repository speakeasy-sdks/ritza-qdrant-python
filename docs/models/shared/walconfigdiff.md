# WalConfigDiff

Custom params for WAL. If none - values from service configuration file are used.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `wal_capacity_mb`                                            | *Optional[int]*                                              | :heavy_minus_sign:                                           | Size of a single WAL segment in MB                           |
| `wal_segments_ahead`                                         | *Optional[int]*                                              | :heavy_minus_sign:                                           | Number of WAL segments to create ahead of actually used ones |