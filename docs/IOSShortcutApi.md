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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

