# tikhub_sdk_v2.KuaishouWebAPIApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get**](KuaishouWebAPIApi.md#fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get) | **GET** /api/v1/kuaishou/web/fetch_one_video_by_url | 根据链接获取单个作品数据/Fetch single video by URL
[**fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get_0**](KuaishouWebAPIApi.md#fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get_0) | **GET** /api/v1/kuaishou/web/fetch_one_video_by_url | 根据链接获取单个作品数据/Fetch single video by URL
[**fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get**](KuaishouWebAPIApi.md#fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get) | **GET** /api/v1/kuaishou/web/fetch_one_video_v2 | 快手单一视频查询接口V2/Kuaishou single video query API V2
[**fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get_0**](KuaishouWebAPIApi.md#fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get_0) | **GET** /api/v1/kuaishou/web/fetch_one_video_v2 | 快手单一视频查询接口V2/Kuaishou single video query API V2


# **fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get**
> ResponseModel fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get(url)

根据链接获取单个作品数据/Fetch single video by URL

# [中文] ### 用途: - 根据链接获取单个作品数据 ### 参数: - url: 作品链接 ### 返回: - 视频数据  # [English] ### Purpose: - Fetch single video by URL ### Parameters: - url: Photo URL ### Returns: - Video data  # [示例/Example] url = \"https://v.kuaishou.com/GKTpYm\"

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
    api_instance = tikhub_sdk_v2.KuaishouWebAPIApi(api_client)
    url = 'https://v.kuaishou.com/GKTpYm' # str | 

    try:
        # 根据链接获取单个作品数据/Fetch single video by URL
        api_response = api_instance.fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get(url)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KuaishouWebAPIApi->fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**|  | 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get_0**
> ResponseModel fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get_0(url)

根据链接获取单个作品数据/Fetch single video by URL

# [中文] ### 用途: - 根据链接获取单个作品数据 ### 参数: - url: 作品链接 ### 返回: - 视频数据  # [English] ### Purpose: - Fetch single video by URL ### Parameters: - url: Photo URL ### Returns: - Video data  # [示例/Example] url = \"https://v.kuaishou.com/GKTpYm\"

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
    api_instance = tikhub_sdk_v2.KuaishouWebAPIApi(api_client)
    url = 'https://v.kuaishou.com/GKTpYm' # str | 

    try:
        # 根据链接获取单个作品数据/Fetch single video by URL
        api_response = api_instance.fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get_0(url)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KuaishouWebAPIApi->fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**|  | 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get**
> ResponseModel fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get(photo_id)

快手单一视频查询接口V2/Kuaishou single video query API V2

# [中文] ### 用途: - 快手单一视频查询接口V2 ### 参数: - photo_id: 作品ID，作品ID可以从作品链接中提取 ### 返回: - 视频数据  # [English] ### Purpose: - Kuaishou single video query API V2 ### Parameters: - photo_id: Photo ID, the photo ID can be extracted from the photo link ### Returns: - Video data  # [示例/Example] photo_id = \"3xtdqvdnqd3psuc\"

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
    api_instance = tikhub_sdk_v2.KuaishouWebAPIApi(api_client)
    photo_id = '3xtdqvdnqd3psuc' # str | 

    try:
        # 快手单一视频查询接口V2/Kuaishou single video query API V2
        api_response = api_instance.fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get(photo_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KuaishouWebAPIApi->fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **photo_id** | **str**|  | 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get_0**
> ResponseModel fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get_0(photo_id)

快手单一视频查询接口V2/Kuaishou single video query API V2

# [中文] ### 用途: - 快手单一视频查询接口V2 ### 参数: - photo_id: 作品ID，作品ID可以从作品链接中提取 ### 返回: - 视频数据  # [English] ### Purpose: - Kuaishou single video query API V2 ### Parameters: - photo_id: Photo ID, the photo ID can be extracted from the photo link ### Returns: - Video data  # [示例/Example] photo_id = \"3xtdqvdnqd3psuc\"

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
    api_instance = tikhub_sdk_v2.KuaishouWebAPIApi(api_client)
    photo_id = '3xtdqvdnqd3psuc' # str | 

    try:
        # 快手单一视频查询接口V2/Kuaishou single video query API V2
        api_response = api_instance.fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get_0(photo_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KuaishouWebAPIApi->fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **photo_id** | **str**|  | 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

