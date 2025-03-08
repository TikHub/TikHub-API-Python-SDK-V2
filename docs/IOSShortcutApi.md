# tikhub_sdk_v2.IOSShortcutApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_shortcut_api_v1_ios_shortcut_shortcut_get**](IOSShortcutApi.md#get_shortcut_api_v1_ios_shortcut_shortcut_get) | **GET** /api/v1/ios_shortcut/shortcut | 用于iOS快捷指令的版本更新信息/Version update information for iOS shortcuts
[**get_shortcut_api_v1_ios_shortcut_shortcut_get_0**](IOSShortcutApi.md#get_shortcut_api_v1_ios_shortcut_shortcut_get_0) | **GET** /api/v1/ios_shortcut/shortcut | 用于iOS快捷指令的版本更新信息/Version update information for iOS shortcuts


# **get_shortcut_api_v1_ios_shortcut_shortcut_get**
> IOsShortcut get_shortcut_api_v1_ios_shortcut_shortcut_get()

用于iOS快捷指令的版本更新信息/Version update information for iOS shortcuts

### Example

* Bearer Authentication (bearer):
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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = tikhub_sdk_v2.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with tikhub_sdk_v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tikhub_sdk_v2.IOSShortcutApi(api_client)
    
    try:
        # 用于iOS快捷指令的版本更新信息/Version update information for iOS shortcuts
        api_response = api_instance.get_shortcut_api_v1_ios_shortcut_shortcut_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IOSShortcutApi->get_shortcut_api_v1_ios_shortcut_shortcut_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IOsShortcut**](IOsShortcut.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shortcut_api_v1_ios_shortcut_shortcut_get_0**
> IOsShortcut get_shortcut_api_v1_ios_shortcut_shortcut_get_0()

用于iOS快捷指令的版本更新信息/Version update information for iOS shortcuts

### Example

* Bearer Authentication (bearer):
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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = tikhub_sdk_v2.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with tikhub_sdk_v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tikhub_sdk_v2.IOSShortcutApi(api_client)
    
    try:
        # 用于iOS快捷指令的版本更新信息/Version update information for iOS shortcuts
        api_response = api_instance.get_shortcut_api_v1_ios_shortcut_shortcut_get_0()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IOSShortcutApi->get_shortcut_api_v1_ios_shortcut_shortcut_get_0: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IOsShortcut**](IOsShortcut.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

