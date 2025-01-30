# tikhub_sdk_v2.HealthCheckApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_check_api_v1_health_check_get**](HealthCheckApi.md#health_check_api_v1_health_check_get) | **GET** /api/v1/health/check | 检查服务器是否正确响应请求 / Check if the server responds to requests correctly
[**health_check_api_v1_health_check_get_0**](HealthCheckApi.md#health_check_api_v1_health_check_get_0) | **GET** /api/v1/health/check | 检查服务器是否正确响应请求 / Check if the server responds to requests correctly


# **health_check_api_v1_health_check_get**
> HealthCheckResponse health_check_api_v1_health_check_get()

检查服务器是否正确响应请求 / Check if the server responds to requests correctly

# [中文]  ### 用途说明:  - 检查服务器是否正确响应请求。  ### 参数说明:  - 无参数。  ### 返回结果:  - `status`: 服务器状态，正常为 `ok`。  # [English]  ### Purpose:  - Check if the server responds to requests correctly.  ### Parameter Description:  - No parameters.  ### Return Result:  - `status`: Server status, normal is `ok`.

### Example

```python
from __future__ import print_function
import time
import tikhub_sdk_v2
from tikhub_sdk_v2.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tikhub_sdk_v2.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with tikhub_sdk_v2.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tikhub_sdk_v2.HealthCheckApi(api_client)
    
    try:
        # 检查服务器是否正确响应请求 / Check if the server responds to requests correctly
        api_response = api_instance.health_check_api_v1_health_check_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HealthCheckApi->health_check_api_v1_health_check_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HealthCheckResponse**](HealthCheckResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 服务器响应成功 / Server responds successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_check_api_v1_health_check_get_0**
> HealthCheckResponse health_check_api_v1_health_check_get_0()

检查服务器是否正确响应请求 / Check if the server responds to requests correctly

# [中文]  ### 用途说明:  - 检查服务器是否正确响应请求。  ### 参数说明:  - 无参数。  ### 返回结果:  - `status`: 服务器状态，正常为 `ok`。  # [English]  ### Purpose:  - Check if the server responds to requests correctly.  ### Parameter Description:  - No parameters.  ### Return Result:  - `status`: Server status, normal is `ok`.

### Example

```python
from __future__ import print_function
import time
import tikhub_sdk_v2
from tikhub_sdk_v2.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tikhub_sdk_v2.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with tikhub_sdk_v2.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tikhub_sdk_v2.HealthCheckApi(api_client)
    
    try:
        # 检查服务器是否正确响应请求 / Check if the server responds to requests correctly
        api_response = api_instance.health_check_api_v1_health_check_get_0()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HealthCheckApi->health_check_api_v1_health_check_get_0: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HealthCheckResponse**](HealthCheckResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 服务器响应成功 / Server responds successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

