# GetLocksResponse


## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `content_type`                                                                                | *str*                                                                                         | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `error_response`                                                                              | [Optional[shared.ErrorResponse]](../../models/shared/errorresponse.md)                        | :heavy_minus_sign:                                                                            | error                                                                                         |
| `status_code`                                                                                 | *int*                                                                                         | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `raw_response`                                                                                | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)         | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `get_locks_200_application_json_object`                                                       | [Optional[GetLocks200ApplicationJSON]](../../models/operations/getlocks200applicationjson.md) | :heavy_minus_sign:                                                                            | successful operation                                                                          |