# WalConfig


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `wal_capacity_mb`                                            | *int*                                                        | :heavy_check_mark:                                           | Size of a single WAL segment in MB                           |
| `wal_segments_ahead`                                         | *int*                                                        | :heavy_check_mark:                                           | Number of WAL segments to create ahead of actually used ones |