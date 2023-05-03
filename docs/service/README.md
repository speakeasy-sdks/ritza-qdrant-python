# service

## Overview

Service management

### Available Operations

* [get_locks](#get_locks) - Get lock options
* [metrics](#metrics) - Collect Prometheus metrics data
* [post_locks](#post_locks) - Set lock options
* [telemetry](#telemetry) - Collect telemetry data

## get_locks

Get lock options. If write is locked, all write operations and collection creation are forbidden

### Example Usage

```python
import sdk


s = sdk.SDK()


res = s.service.get_locks()

if res.get_locks_200_application_json_object is not None:
    # handle response
```

## metrics

Collect metrics data including app info, collections info, cluster info and statistics

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()


req = operations.MetricsRequest(
    anonymize=False,
)

res = s.service.metrics(req)

if res.metrics_200_text_plain_string is not None:
    # handle response
```

## post_locks

Set lock options. If write is locked, all write operations and collection creation are forbidden. Returns previous lock options

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK()


req = shared.LocksOption(
    error_message='consectetur',
    write=False,
)

res = s.service.post_locks(req)

if res.post_locks_200_application_json_object is not None:
    # handle response
```

## telemetry

Collect telemetry data including app info, system info, collections info, cluster info, configs and statistics

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()


req = operations.TelemetryRequest(
    anonymize=False,
)

res = s.service.telemetry(req)

if res.telemetry_200_application_json_object is not None:
    # handle response
```
