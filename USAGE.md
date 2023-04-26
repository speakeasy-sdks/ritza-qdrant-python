<!-- Start SDK Example Usage -->
```python
import sdk


s = sdk.SDK()


res = s.cluster.cluster_status()

if res.cluster_status_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->