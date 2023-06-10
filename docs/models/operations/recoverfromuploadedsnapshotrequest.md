# RecoverFromUploadedSnapshotRequest


## Fields

| Field                                                                                                                 | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `request_body`                                                                                                        | [Optional[RecoverFromUploadedSnapshotRequestBody]](../../models/operations/recoverfromuploadedsnapshotrequestbody.md) | :heavy_minus_sign:                                                                                                    | Snapshot to recover from                                                                                              |
| `collection_name`                                                                                                     | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | Name of the collection                                                                                                |
| `priority`                                                                                                            | [Optional[shared.SnapshotPriority]](../../models/shared/snapshotpriority.md)                                          | :heavy_minus_sign:                                                                                                    | Defines source of truth for snapshot recovery                                                                         |
| `wait`                                                                                                                | *Optional[bool]*                                                                                                      | :heavy_minus_sign:                                                                                                    | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true.           |