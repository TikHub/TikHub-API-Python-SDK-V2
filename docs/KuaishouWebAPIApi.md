# tikhub_sdk_v2.KuaishouWebAPIApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_home_page_info_api_v1_kuaishou_web_fetch_home_page_info_get**](KuaishouWebAPIApi.md#fetch_home_page_info_api_v1_kuaishou_web_fetch_home_page_info_get) | **GET** /api/v1/kuaishou/web/fetch_home_page_info | 获取主页信息数据/Get home page info data
[**fetch_home_page_info_api_v1_kuaishou_web_fetch_home_page_info_get_0**](KuaishouWebAPIApi.md#fetch_home_page_info_api_v1_kuaishou_web_fetch_home_page_info_get_0) | **GET** /api/v1/kuaishou/web/fetch_home_page_info | 获取主页信息数据/Get home page info data
[**fetch_home_page_video_api_v1_kuaishou_web_fetch_home_page_video_get**](KuaishouWebAPIApi.md#fetch_home_page_video_api_v1_kuaishou_web_fetch_home_page_video_get) | **GET** /api/v1/kuaishou/web/fetch_home_page_video | 获取主页视频数据/Get home page video data
[**fetch_home_page_video_api_v1_kuaishou_web_fetch_home_page_video_get_0**](KuaishouWebAPIApi.md#fetch_home_page_video_api_v1_kuaishou_web_fetch_home_page_video_get_0) | **GET** /api/v1/kuaishou/web/fetch_home_page_video | 获取主页视频数据/Get home page video data
[**fetch_one_video_api_v1_kuaishou_web_fetch_one_video_get**](KuaishouWebAPIApi.md#fetch_one_video_api_v1_kuaishou_web_fetch_one_video_get) | **GET** /api/v1/kuaishou/web/fetch_one_video | 获取单个作品数据/Get single video data
[**fetch_one_video_api_v1_kuaishou_web_fetch_one_video_get_0**](KuaishouWebAPIApi.md#fetch_one_video_api_v1_kuaishou_web_fetch_one_video_get_0) | **GET** /api/v1/kuaishou/web/fetch_one_video | 获取单个作品数据/Get single video data
[**fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get**](KuaishouWebAPIApi.md#fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get) | **GET** /api/v1/kuaishou/web/fetch_one_video_by_url | 根据链接获取单个作品数据/Fetch single video by URL
[**fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get_0**](KuaishouWebAPIApi.md#fetch_one_video_by_url_api_v1_kuaishou_web_fetch_one_video_by_url_get_0) | **GET** /api/v1/kuaishou/web/fetch_one_video_by_url | 根据链接获取单个作品数据/Fetch single video by URL
[**fetch_one_video_by_url_v2_api_v1_kuaishou_web_fetch_one_video_by_url_v2_get**](KuaishouWebAPIApi.md#fetch_one_video_by_url_v2_api_v1_kuaishou_web_fetch_one_video_by_url_v2_get) | **GET** /api/v1/kuaishou/web/fetch_one_video_by_url_v2 | 根据链接获取单个作品数据V2/Fetch single video by URL V2
[**fetch_one_video_by_url_v2_api_v1_kuaishou_web_fetch_one_video_by_url_v2_get_0**](KuaishouWebAPIApi.md#fetch_one_video_by_url_v2_api_v1_kuaishou_web_fetch_one_video_by_url_v2_get_0) | **GET** /api/v1/kuaishou/web/fetch_one_video_by_url_v2 | 根据链接获取单个作品数据V2/Fetch single video by URL V2
[**fetch_one_video_comment_api_v1_kuaishou_web_fetch_one_video_comment_get**](KuaishouWebAPIApi.md#fetch_one_video_comment_api_v1_kuaishou_web_fetch_one_video_comment_get) | **GET** /api/v1/kuaishou/web/fetch_one_video_comment | 获取单个作品评论数据/Get single video comment data
[**fetch_one_video_comment_api_v1_kuaishou_web_fetch_one_video_comment_get_0**](KuaishouWebAPIApi.md#fetch_one_video_comment_api_v1_kuaishou_web_fetch_one_video_comment_get_0) | **GET** /api/v1/kuaishou/web/fetch_one_video_comment | 获取单个作品评论数据/Get single video comment data
[**fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get**](KuaishouWebAPIApi.md#fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get) | **GET** /api/v1/kuaishou/web/fetch_one_video_v2 | 快手单一视频查询接口V2/Kuaishou single video query API V2
[**fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get_0**](KuaishouWebAPIApi.md#fetch_one_video_v2_api_v1_kuaishou_web_fetch_one_video_v2_get_0) | **GET** /api/v1/kuaishou/web/fetch_one_video_v2 | 快手单一视频查询接口V2/Kuaishou single video query API V2
[**fetch_user_info_api_v1_kuaishou_web_fetch_user_info_get**](KuaishouWebAPIApi.md#fetch_user_info_api_v1_kuaishou_web_fetch_user_info_get) | **GET** /api/v1/kuaishou/web/fetch_user_info | 获取主页信息数据/Get home page info data
[**fetch_user_info_api_v1_kuaishou_web_fetch_user_info_get_0**](KuaishouWebAPIApi.md#fetch_user_info_api_v1_kuaishou_web_fetch_user_info_get_0) | **GET** /api/v1/kuaishou/web/fetch_user_info | 获取主页信息数据/Get home page info data


# **fetch_home_page_info_api_v1_kuaishou_web_fetch_home_page_info_get**
> ResponseModel fetch_home_page_info_api_v1_kuaishou_web_fetch_home_page_info_get(user_id)

获取主页信息数据/Get home page info data

# [中文] ### 用途: - 获取主页信息数据 ### 参数: - user_id: 用户ID ### 返回: - 主页信息数据  # [English] ### Purpose: - Fetch home page info data ### Parameters: - user_id: User ID ### Returns: - Home page info data  # [示例/Example] user_id = \"3xduik3j7us2ge6\"

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
    user_id = '3xduik3j7us2ge6' # str | 

    try:
        # 获取主页信息数据/Get home page info data
        api_response = api_instance.fetch_home_page_info_api_v1_kuaishou_web_fetch_home_page_info_get(user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KuaishouWebAPIApi->fetch_home_page_info_api_v1_kuaishou_web_fetch_home_page_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

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

# **fetch_home_page_info_api_v1_kuaishou_web_fetch_home_page_info_get_0**
> ResponseModel fetch_home_page_info_api_v1_kuaishou_web_fetch_home_page_info_get_0(user_id)

获取主页信息数据/Get home page info data

# [中文] ### 用途: - 获取主页信息数据 ### 参数: - user_id: 用户ID ### 返回: - 主页信息数据  # [English] ### Purpose: - Fetch home page info data ### Parameters: - user_id: User ID ### Returns: - Home page info data  # [示例/Example] user_id = \"3xduik3j7us2ge6\"

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
    user_id = '3xduik3j7us2ge6' # str | 

    try:
        # 获取主页信息数据/Get home page info data
        api_response = api_instance.fetch_home_page_info_api_v1_kuaishou_web_fetch_home_page_info_get_0(user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KuaishouWebAPIApi->fetch_home_page_info_api_v1_kuaishou_web_fetch_home_page_info_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

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

# **fetch_home_page_video_api_v1_kuaishou_web_fetch_home_page_video_get**
> ResponseModel fetch_home_page_video_api_v1_kuaishou_web_fetch_home_page_video_get(user_id=user_id, user_profile_url=user_profile_url, pcursor=pcursor)

获取主页视频数据/Get home page video data

# [中文] ### 用途: - 获取主页视频数据 ### 参数: - user_id: 用户ID - user_profile_url: 用户主页链接，user_id和user_profile_url必须传一个 - pcursor: 视频游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。 ### 返回: - 视频数据  # [English] ### Purpose: - Fetch home page video data ### Parameters: - user_id: User ID - user_profile_url: User profile URL, one of user_id and user_profile_url must be passed - pcursor: Video cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests. ### Returns: - Videos data  # [示例/Example] user_id = \"3xduik3j7us2ge6\" user_profile_url = \"https://www.kuaishou.com/profile/3xduik3j7us2ge6\" pcursor = '1.718349959396E12'

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
    user_id = '3xduik3j7us2ge6' # str |  (optional)
user_profile_url = 'https://www.kuaishou.com/profile/3xduik3j7us2ge6' # str |  (optional)
pcursor = 'pcursor_example' # str |  (optional)

    try:
        # 获取主页视频数据/Get home page video data
        api_response = api_instance.fetch_home_page_video_api_v1_kuaishou_web_fetch_home_page_video_get(user_id=user_id, user_profile_url=user_profile_url, pcursor=pcursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KuaishouWebAPIApi->fetch_home_page_video_api_v1_kuaishou_web_fetch_home_page_video_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | [optional] 
 **user_profile_url** | **str**|  | [optional] 
 **pcursor** | **str**|  | [optional] 

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

# **fetch_home_page_video_api_v1_kuaishou_web_fetch_home_page_video_get_0**
> ResponseModel fetch_home_page_video_api_v1_kuaishou_web_fetch_home_page_video_get_0(user_id=user_id, user_profile_url=user_profile_url, pcursor=pcursor)

获取主页视频数据/Get home page video data

# [中文] ### 用途: - 获取主页视频数据 ### 参数: - user_id: 用户ID - user_profile_url: 用户主页链接，user_id和user_profile_url必须传一个 - pcursor: 视频游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。 ### 返回: - 视频数据  # [English] ### Purpose: - Fetch home page video data ### Parameters: - user_id: User ID - user_profile_url: User profile URL, one of user_id and user_profile_url must be passed - pcursor: Video cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests. ### Returns: - Videos data  # [示例/Example] user_id = \"3xduik3j7us2ge6\" user_profile_url = \"https://www.kuaishou.com/profile/3xduik3j7us2ge6\" pcursor = '1.718349959396E12'

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
    user_id = '3xduik3j7us2ge6' # str |  (optional)
user_profile_url = 'https://www.kuaishou.com/profile/3xduik3j7us2ge6' # str |  (optional)
pcursor = 'pcursor_example' # str |  (optional)

    try:
        # 获取主页视频数据/Get home page video data
        api_response = api_instance.fetch_home_page_video_api_v1_kuaishou_web_fetch_home_page_video_get_0(user_id=user_id, user_profile_url=user_profile_url, pcursor=pcursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KuaishouWebAPIApi->fetch_home_page_video_api_v1_kuaishou_web_fetch_home_page_video_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | [optional] 
 **user_profile_url** | **str**|  | [optional] 
 **pcursor** | **str**|  | [optional] 

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

# **fetch_one_video_api_v1_kuaishou_web_fetch_one_video_get**
> ResponseModel fetch_one_video_api_v1_kuaishou_web_fetch_one_video_get(share_text)

获取单个作品数据/Get single video data

# [中文] ### 用途: - 获取单个作品数据，此接口不支持图文作品。 ### 参数: - share_text: 作品分享链接 ### 返回: - 视频数据  # [English] ### Purpose: - Fetch single video data, this interface does not support photo only posts. ### Parameters: - share_text: Photo share link ### Returns: - Video data  # [示例/Example] share_text = \"https://www.kuaishou.com/f/X-f2k5KJpiXN1SY\"

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
    share_text = 'https://www.kuaishou.com/f/X-f2k5KJpiXN1SY' # str | 

    try:
        # 获取单个作品数据/Get single video data
        api_response = api_instance.fetch_one_video_api_v1_kuaishou_web_fetch_one_video_get(share_text)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KuaishouWebAPIApi->fetch_one_video_api_v1_kuaishou_web_fetch_one_video_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_text** | **str**|  | 

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

# **fetch_one_video_api_v1_kuaishou_web_fetch_one_video_get_0**
> ResponseModel fetch_one_video_api_v1_kuaishou_web_fetch_one_video_get_0(share_text)

获取单个作品数据/Get single video data

# [中文] ### 用途: - 获取单个作品数据，此接口不支持图文作品。 ### 参数: - share_text: 作品分享链接 ### 返回: - 视频数据  # [English] ### Purpose: - Fetch single video data, this interface does not support photo only posts. ### Parameters: - share_text: Photo share link ### Returns: - Video data  # [示例/Example] share_text = \"https://www.kuaishou.com/f/X-f2k5KJpiXN1SY\"

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
    share_text = 'https://www.kuaishou.com/f/X-f2k5KJpiXN1SY' # str | 

    try:
        # 获取单个作品数据/Get single video data
        api_response = api_instance.fetch_one_video_api_v1_kuaishou_web_fetch_one_video_get_0(share_text)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KuaishouWebAPIApi->fetch_one_video_api_v1_kuaishou_web_fetch_one_video_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_text** | **str**|  | 

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

# **fetch_one_video_by_url_v2_api_v1_kuaishou_web_fetch_one_video_by_url_v2_get**
> ResponseModel fetch_one_video_by_url_v2_api_v1_kuaishou_web_fetch_one_video_by_url_v2_get(url)

根据链接获取单个作品数据V2/Fetch single video by URL V2

# [中文] ### 用途: - 根据链接获取单个作品数据V2 ### 参数: - url: 作品链接 ### 返回: - 视频数据  # [English] ### Purpose: - Fetch single video by URL V2 ### Parameters: - url: Photo URL ### Returns: - Video data  # [示例/Example] url = \"https://v.kuaishou.com/GKTpYm\"

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
        # 根据链接获取单个作品数据V2/Fetch single video by URL V2
        api_response = api_instance.fetch_one_video_by_url_v2_api_v1_kuaishou_web_fetch_one_video_by_url_v2_get(url)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KuaishouWebAPIApi->fetch_one_video_by_url_v2_api_v1_kuaishou_web_fetch_one_video_by_url_v2_get: %s\n" % e)
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

# **fetch_one_video_by_url_v2_api_v1_kuaishou_web_fetch_one_video_by_url_v2_get_0**
> ResponseModel fetch_one_video_by_url_v2_api_v1_kuaishou_web_fetch_one_video_by_url_v2_get_0(url)

根据链接获取单个作品数据V2/Fetch single video by URL V2

# [中文] ### 用途: - 根据链接获取单个作品数据V2 ### 参数: - url: 作品链接 ### 返回: - 视频数据  # [English] ### Purpose: - Fetch single video by URL V2 ### Parameters: - url: Photo URL ### Returns: - Video data  # [示例/Example] url = \"https://v.kuaishou.com/GKTpYm\"

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
        # 根据链接获取单个作品数据V2/Fetch single video by URL V2
        api_response = api_instance.fetch_one_video_by_url_v2_api_v1_kuaishou_web_fetch_one_video_by_url_v2_get_0(url)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KuaishouWebAPIApi->fetch_one_video_by_url_v2_api_v1_kuaishou_web_fetch_one_video_by_url_v2_get_0: %s\n" % e)
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

# **fetch_one_video_comment_api_v1_kuaishou_web_fetch_one_video_comment_get**
> ResponseModel fetch_one_video_comment_api_v1_kuaishou_web_fetch_one_video_comment_get(photo_id, pcursor=pcursor)

获取单个作品评论数据/Get single video comment data

# [中文] ### 用途: - 获取单个作品评论数据 ### 参数: - photo_id: 作品ID - pcursor: 评论游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。 ### 返回: - 评论数据  # [English] ### Purpose: - Fetch single video comment data ### Parameters: - photo_id: Photo ID - pcursor: Comment cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests. ### Returns: - Comments data  # [示例/Example] photo_id = \"3x7gxp2zhgjv832\" pcursor = None

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
    photo_id = '3x7gxp2zhgjv832' # str | 
pcursor = 'pcursor_example' # str |  (optional)

    try:
        # 获取单个作品评论数据/Get single video comment data
        api_response = api_instance.fetch_one_video_comment_api_v1_kuaishou_web_fetch_one_video_comment_get(photo_id, pcursor=pcursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KuaishouWebAPIApi->fetch_one_video_comment_api_v1_kuaishou_web_fetch_one_video_comment_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **photo_id** | **str**|  | 
 **pcursor** | **str**|  | [optional] 

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

# **fetch_one_video_comment_api_v1_kuaishou_web_fetch_one_video_comment_get_0**
> ResponseModel fetch_one_video_comment_api_v1_kuaishou_web_fetch_one_video_comment_get_0(photo_id, pcursor=pcursor)

获取单个作品评论数据/Get single video comment data

# [中文] ### 用途: - 获取单个作品评论数据 ### 参数: - photo_id: 作品ID - pcursor: 评论游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。 ### 返回: - 评论数据  # [English] ### Purpose: - Fetch single video comment data ### Parameters: - photo_id: Photo ID - pcursor: Comment cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests. ### Returns: - Comments data  # [示例/Example] photo_id = \"3x7gxp2zhgjv832\" pcursor = None

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
    photo_id = '3x7gxp2zhgjv832' # str | 
pcursor = 'pcursor_example' # str |  (optional)

    try:
        # 获取单个作品评论数据/Get single video comment data
        api_response = api_instance.fetch_one_video_comment_api_v1_kuaishou_web_fetch_one_video_comment_get_0(photo_id, pcursor=pcursor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KuaishouWebAPIApi->fetch_one_video_comment_api_v1_kuaishou_web_fetch_one_video_comment_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **photo_id** | **str**|  | 
 **pcursor** | **str**|  | [optional] 

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

# **fetch_user_info_api_v1_kuaishou_web_fetch_user_info_get**
> ResponseModel fetch_user_info_api_v1_kuaishou_web_fetch_user_info_get(share_text)

获取主页信息数据/Get home page info data

# [中文] ### 用途: - 获取主页信息数据 ### 参数: - share_text: APP用户主页分享链接 ### 返回: - 主页信息数据  # [English] ### Purpose: - Fetch home page info data ### Parameters: - share_text: APP user home page share link ### Returns: - Home page info data  # [示例/Example] share_text = \"https://v.kuaishou.com/2LS90E\"

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
    share_text = 'https://v.kuaishou.com/2LS90E' # str | 

    try:
        # 获取主页信息数据/Get home page info data
        api_response = api_instance.fetch_user_info_api_v1_kuaishou_web_fetch_user_info_get(share_text)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KuaishouWebAPIApi->fetch_user_info_api_v1_kuaishou_web_fetch_user_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_text** | **str**|  | 

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

# **fetch_user_info_api_v1_kuaishou_web_fetch_user_info_get_0**
> ResponseModel fetch_user_info_api_v1_kuaishou_web_fetch_user_info_get_0(share_text)

获取主页信息数据/Get home page info data

# [中文] ### 用途: - 获取主页信息数据 ### 参数: - share_text: APP用户主页分享链接 ### 返回: - 主页信息数据  # [English] ### Purpose: - Fetch home page info data ### Parameters: - share_text: APP user home page share link ### Returns: - Home page info data  # [示例/Example] share_text = \"https://v.kuaishou.com/2LS90E\"

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
    share_text = 'https://v.kuaishou.com/2LS90E' # str | 

    try:
        # 获取主页信息数据/Get home page info data
        api_response = api_instance.fetch_user_info_api_v1_kuaishou_web_fetch_user_info_get_0(share_text)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KuaishouWebAPIApi->fetch_user_info_api_v1_kuaishou_web_fetch_user_info_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_text** | **str**|  | 

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

