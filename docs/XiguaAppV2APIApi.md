# tikhub_sdk_v2.XiguaAppV2APIApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_one_video_api_v1_xigua_app_v2_fetch_one_video_get**](XiguaAppV2APIApi.md#fetch_one_video_api_v1_xigua_app_v2_fetch_one_video_get) | **GET** /api/v1/xigua/app/v2/fetch_one_video | 获取单个作品数据/Get single video data
[**fetch_one_video_api_v1_xigua_app_v2_fetch_one_video_get_0**](XiguaAppV2APIApi.md#fetch_one_video_api_v1_xigua_app_v2_fetch_one_video_get_0) | **GET** /api/v1/xigua/app/v2/fetch_one_video | 获取单个作品数据/Get single video data
[**fetch_one_video_play_url_api_v1_xigua_app_v2_fetch_one_video_play_url_get**](XiguaAppV2APIApi.md#fetch_one_video_play_url_api_v1_xigua_app_v2_fetch_one_video_play_url_get) | **GET** /api/v1/xigua/app/v2/fetch_one_video_play_url | 获取单个作品的播放链接/Get single video play URL
[**fetch_one_video_play_url_api_v1_xigua_app_v2_fetch_one_video_play_url_get_0**](XiguaAppV2APIApi.md#fetch_one_video_play_url_api_v1_xigua_app_v2_fetch_one_video_play_url_get_0) | **GET** /api/v1/xigua/app/v2/fetch_one_video_play_url | 获取单个作品的播放链接/Get single video play URL
[**fetch_user_info_api_v1_xigua_app_v2_fetch_user_info_get**](XiguaAppV2APIApi.md#fetch_user_info_api_v1_xigua_app_v2_fetch_user_info_get) | **GET** /api/v1/xigua/app/v2/fetch_user_info | 个人信息/Personal information
[**fetch_user_info_api_v1_xigua_app_v2_fetch_user_info_get_0**](XiguaAppV2APIApi.md#fetch_user_info_api_v1_xigua_app_v2_fetch_user_info_get_0) | **GET** /api/v1/xigua/app/v2/fetch_user_info | 个人信息/Personal information
[**fetch_user_post_list_api_v1_xigua_app_v2_fetch_user_post_list_get**](XiguaAppV2APIApi.md#fetch_user_post_list_api_v1_xigua_app_v2_fetch_user_post_list_get) | **GET** /api/v1/xigua/app/v2/fetch_user_post_list | 获取个人作品列表/Get user post list
[**fetch_user_post_list_api_v1_xigua_app_v2_fetch_user_post_list_get_0**](XiguaAppV2APIApi.md#fetch_user_post_list_api_v1_xigua_app_v2_fetch_user_post_list_get_0) | **GET** /api/v1/xigua/app/v2/fetch_user_post_list | 获取个人作品列表/Get user post list
[**fetch_video_comment_list_api_v1_xigua_app_v2_fetch_video_comment_list_get**](XiguaAppV2APIApi.md#fetch_video_comment_list_api_v1_xigua_app_v2_fetch_video_comment_list_get) | **GET** /api/v1/xigua/app/v2/fetch_video_comment_list | 视频评论列表/Video comment list
[**fetch_video_comment_list_api_v1_xigua_app_v2_fetch_video_comment_list_get_0**](XiguaAppV2APIApi.md#fetch_video_comment_list_api_v1_xigua_app_v2_fetch_video_comment_list_get_0) | **GET** /api/v1/xigua/app/v2/fetch_video_comment_list | 视频评论列表/Video comment list
[**search_video_api_v1_xigua_app_v2_search_video_get**](XiguaAppV2APIApi.md#search_video_api_v1_xigua_app_v2_search_video_get) | **GET** /api/v1/xigua/app/v2/search_video | 搜索视频/Search video
[**search_video_api_v1_xigua_app_v2_search_video_get_0**](XiguaAppV2APIApi.md#search_video_api_v1_xigua_app_v2_search_video_get_0) | **GET** /api/v1/xigua/app/v2/search_video | 搜索视频/Search video


# **fetch_one_video_api_v1_xigua_app_v2_fetch_one_video_get**
> ResponseModel fetch_one_video_api_v1_xigua_app_v2_fetch_one_video_get(item_id)

获取单个作品数据/Get single video data

# [中文] ### 用途: - 获取单个作品数据 ### 参数: - item_id: 作品id ### 返回: - 作品数据，其中包含视频链接的Base64编码播放地址，需要前端解码后使用，或者使用 /fetch_one_video_play_url 获取播放链接。  # [English] ### Purpose: - Get single video data ### Parameters: - item_id: Video id ### Return: - Video data, which contains the Base64 encoded playback address of the video link, which needs to be decoded and used by the front end, or use /fetch_one_video_play_url to get the playback link.  # [示例/Example] item_id: \"7354954305222377999\"

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
    api_instance = tikhub_sdk_v2.XiguaAppV2APIApi(api_client)
    item_id = '7354954305222377999' # str | 作品id/Video id

    try:
        # 获取单个作品数据/Get single video data
        api_response = api_instance.fetch_one_video_api_v1_xigua_app_v2_fetch_one_video_get(item_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling XiguaAppV2APIApi->fetch_one_video_api_v1_xigua_app_v2_fetch_one_video_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| 作品id/Video id | 

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

# **fetch_one_video_api_v1_xigua_app_v2_fetch_one_video_get_0**
> ResponseModel fetch_one_video_api_v1_xigua_app_v2_fetch_one_video_get_0(item_id)

获取单个作品数据/Get single video data

# [中文] ### 用途: - 获取单个作品数据 ### 参数: - item_id: 作品id ### 返回: - 作品数据，其中包含视频链接的Base64编码播放地址，需要前端解码后使用，或者使用 /fetch_one_video_play_url 获取播放链接。  # [English] ### Purpose: - Get single video data ### Parameters: - item_id: Video id ### Return: - Video data, which contains the Base64 encoded playback address of the video link, which needs to be decoded and used by the front end, or use /fetch_one_video_play_url to get the playback link.  # [示例/Example] item_id: \"7354954305222377999\"

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
    api_instance = tikhub_sdk_v2.XiguaAppV2APIApi(api_client)
    item_id = '7354954305222377999' # str | 作品id/Video id

    try:
        # 获取单个作品数据/Get single video data
        api_response = api_instance.fetch_one_video_api_v1_xigua_app_v2_fetch_one_video_get_0(item_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling XiguaAppV2APIApi->fetch_one_video_api_v1_xigua_app_v2_fetch_one_video_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| 作品id/Video id | 

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

# **fetch_one_video_play_url_api_v1_xigua_app_v2_fetch_one_video_play_url_get**
> ResponseModel fetch_one_video_play_url_api_v1_xigua_app_v2_fetch_one_video_play_url_get(item_id)

获取单个作品的播放链接/Get single video play URL

# [中文] ### 用途: - 获取单个作品的播放链接，此接口返回的是已经解码后的播放链接，可以直接使用。 ### 参数: - item_id: 作品id ### 返回: - 作品的播放链接的明文链接。  # [English] ### Purpose: - Get single video play URL, the interface returns the decoded play URL, which can be used directly. ### Parameters: - item_id: Video id ### Return: - Play URL of the video, plaintext link.  # [示例/Example] item_id: \"7354954305222377999\"

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
    api_instance = tikhub_sdk_v2.XiguaAppV2APIApi(api_client)
    item_id = '7354954305222377999' # str | 作品id/Video id

    try:
        # 获取单个作品的播放链接/Get single video play URL
        api_response = api_instance.fetch_one_video_play_url_api_v1_xigua_app_v2_fetch_one_video_play_url_get(item_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling XiguaAppV2APIApi->fetch_one_video_play_url_api_v1_xigua_app_v2_fetch_one_video_play_url_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| 作品id/Video id | 

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

# **fetch_one_video_play_url_api_v1_xigua_app_v2_fetch_one_video_play_url_get_0**
> ResponseModel fetch_one_video_play_url_api_v1_xigua_app_v2_fetch_one_video_play_url_get_0(item_id)

获取单个作品的播放链接/Get single video play URL

# [中文] ### 用途: - 获取单个作品的播放链接，此接口返回的是已经解码后的播放链接，可以直接使用。 ### 参数: - item_id: 作品id ### 返回: - 作品的播放链接的明文链接。  # [English] ### Purpose: - Get single video play URL, the interface returns the decoded play URL, which can be used directly. ### Parameters: - item_id: Video id ### Return: - Play URL of the video, plaintext link.  # [示例/Example] item_id: \"7354954305222377999\"

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
    api_instance = tikhub_sdk_v2.XiguaAppV2APIApi(api_client)
    item_id = '7354954305222377999' # str | 作品id/Video id

    try:
        # 获取单个作品的播放链接/Get single video play URL
        api_response = api_instance.fetch_one_video_play_url_api_v1_xigua_app_v2_fetch_one_video_play_url_get_0(item_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling XiguaAppV2APIApi->fetch_one_video_play_url_api_v1_xigua_app_v2_fetch_one_video_play_url_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| 作品id/Video id | 

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

# **fetch_user_info_api_v1_xigua_app_v2_fetch_user_info_get**
> ResponseModel fetch_user_info_api_v1_xigua_app_v2_fetch_user_info_get(user_id)

个人信息/Personal information

# [中文] ### 用途: - 个人信息 ### 参数: - user_id: 用户id ### 返回: - 个人信息  # [English] ### Purpose: - Personal information ### Parameters: - user_id: User id ### Return: - Personal information  # [示例/Example] user_id: \"52712347586\"

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
    api_instance = tikhub_sdk_v2.XiguaAppV2APIApi(api_client)
    user_id = '52712347586' # str | 用户id/User id

    try:
        # 个人信息/Personal information
        api_response = api_instance.fetch_user_info_api_v1_xigua_app_v2_fetch_user_info_get(user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling XiguaAppV2APIApi->fetch_user_info_api_v1_xigua_app_v2_fetch_user_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| 用户id/User id | 

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

# **fetch_user_info_api_v1_xigua_app_v2_fetch_user_info_get_0**
> ResponseModel fetch_user_info_api_v1_xigua_app_v2_fetch_user_info_get_0(user_id)

个人信息/Personal information

# [中文] ### 用途: - 个人信息 ### 参数: - user_id: 用户id ### 返回: - 个人信息  # [English] ### Purpose: - Personal information ### Parameters: - user_id: User id ### Return: - Personal information  # [示例/Example] user_id: \"52712347586\"

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
    api_instance = tikhub_sdk_v2.XiguaAppV2APIApi(api_client)
    user_id = '52712347586' # str | 用户id/User id

    try:
        # 个人信息/Personal information
        api_response = api_instance.fetch_user_info_api_v1_xigua_app_v2_fetch_user_info_get_0(user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling XiguaAppV2APIApi->fetch_user_info_api_v1_xigua_app_v2_fetch_user_info_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| 用户id/User id | 

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

# **fetch_user_post_list_api_v1_xigua_app_v2_fetch_user_post_list_get**
> ResponseModel fetch_user_post_list_api_v1_xigua_app_v2_fetch_user_post_list_get(user_id, max_behot_time=max_behot_time)

获取个人作品列表/Get user post list

# [中文] ### 用途: - 获取个人作品列表 ### 参数: - user_id: 用户id - max_behot_time: 最大行为时间，默认空，第一次请求传空，后续请求传上一次请求返回数据中的JSON中的值。 - max_behot_time的值可以是JSON路径为：$.data.data.[-1].behot_time - 也就是data中的最后一个元素的cursor值 ### 返回: - 作品列表  # [English] ### Purpose: - Get user post list ### Parameters: - user_id: User id - max_behot_time: Maximum behavior time, default empty, pass empty for the first request, pass the max_behot_time returned by the previous request for subsequent requests - The value of max_behot_time can be the JSON path: $.data.data.[-1].behot_time - That is, the cursor value of the last element in data ### Return: - Post list  # [示例/Example] user_id = \"1922379661976311\" max_behot_time = \"\"

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
    api_instance = tikhub_sdk_v2.XiguaAppV2APIApi(api_client)
    user_id = '1922379661976311' # str | 用户id/User id
max_behot_time = 'max_behot_time_example' # str | 最大行为时间/Maximum behavior time (optional)

    try:
        # 获取个人作品列表/Get user post list
        api_response = api_instance.fetch_user_post_list_api_v1_xigua_app_v2_fetch_user_post_list_get(user_id, max_behot_time=max_behot_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling XiguaAppV2APIApi->fetch_user_post_list_api_v1_xigua_app_v2_fetch_user_post_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| 用户id/User id | 
 **max_behot_time** | **str**| 最大行为时间/Maximum behavior time | [optional] 

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

# **fetch_user_post_list_api_v1_xigua_app_v2_fetch_user_post_list_get_0**
> ResponseModel fetch_user_post_list_api_v1_xigua_app_v2_fetch_user_post_list_get_0(user_id, max_behot_time=max_behot_time)

获取个人作品列表/Get user post list

# [中文] ### 用途: - 获取个人作品列表 ### 参数: - user_id: 用户id - max_behot_time: 最大行为时间，默认空，第一次请求传空，后续请求传上一次请求返回数据中的JSON中的值。 - max_behot_time的值可以是JSON路径为：$.data.data.[-1].behot_time - 也就是data中的最后一个元素的cursor值 ### 返回: - 作品列表  # [English] ### Purpose: - Get user post list ### Parameters: - user_id: User id - max_behot_time: Maximum behavior time, default empty, pass empty for the first request, pass the max_behot_time returned by the previous request for subsequent requests - The value of max_behot_time can be the JSON path: $.data.data.[-1].behot_time - That is, the cursor value of the last element in data ### Return: - Post list  # [示例/Example] user_id = \"1922379661976311\" max_behot_time = \"\"

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
    api_instance = tikhub_sdk_v2.XiguaAppV2APIApi(api_client)
    user_id = '1922379661976311' # str | 用户id/User id
max_behot_time = 'max_behot_time_example' # str | 最大行为时间/Maximum behavior time (optional)

    try:
        # 获取个人作品列表/Get user post list
        api_response = api_instance.fetch_user_post_list_api_v1_xigua_app_v2_fetch_user_post_list_get_0(user_id, max_behot_time=max_behot_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling XiguaAppV2APIApi->fetch_user_post_list_api_v1_xigua_app_v2_fetch_user_post_list_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| 用户id/User id | 
 **max_behot_time** | **str**| 最大行为时间/Maximum behavior time | [optional] 

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

# **fetch_video_comment_list_api_v1_xigua_app_v2_fetch_video_comment_list_get**
> ResponseModel fetch_video_comment_list_api_v1_xigua_app_v2_fetch_video_comment_list_get(item_id, offset=offset, count=count)

视频评论列表/Video comment list

# [中文] ### 用途: - 视频评论列表 ### 参数: - item_id: 作品id - offset: 偏移量，第一次请求传0，后续请求传上一次请求返回的offset - count: 数量，默认20，建议保持默认。 ### 返回: - 评论列表  # [English] ### Purpose: - Video comment list ### Parameters: - item_id: Video id - offset: Offset, pass 0 for the first request, pass the offset returned by the previous request for subsequent requests - count: Quantity, default 20, it is recommended to keep the default. ### Return: - Comment list  # [示例/Example] item_id: \"7354954305222377999\"

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
    api_instance = tikhub_sdk_v2.XiguaAppV2APIApi(api_client)
    item_id = '7354954305222377999' # str | 作品id/Video id
offset = 0 # int | 偏移量/Offset (optional) (default to 0)
count = 20 # int | 数量/Count (optional) (default to 20)

    try:
        # 视频评论列表/Video comment list
        api_response = api_instance.fetch_video_comment_list_api_v1_xigua_app_v2_fetch_video_comment_list_get(item_id, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling XiguaAppV2APIApi->fetch_video_comment_list_api_v1_xigua_app_v2_fetch_video_comment_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| 作品id/Video id | 
 **offset** | **int**| 偏移量/Offset | [optional] [default to 0]
 **count** | **int**| 数量/Count | [optional] [default to 20]

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

# **fetch_video_comment_list_api_v1_xigua_app_v2_fetch_video_comment_list_get_0**
> ResponseModel fetch_video_comment_list_api_v1_xigua_app_v2_fetch_video_comment_list_get_0(item_id, offset=offset, count=count)

视频评论列表/Video comment list

# [中文] ### 用途: - 视频评论列表 ### 参数: - item_id: 作品id - offset: 偏移量，第一次请求传0，后续请求传上一次请求返回的offset - count: 数量，默认20，建议保持默认。 ### 返回: - 评论列表  # [English] ### Purpose: - Video comment list ### Parameters: - item_id: Video id - offset: Offset, pass 0 for the first request, pass the offset returned by the previous request for subsequent requests - count: Quantity, default 20, it is recommended to keep the default. ### Return: - Comment list  # [示例/Example] item_id: \"7354954305222377999\"

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
    api_instance = tikhub_sdk_v2.XiguaAppV2APIApi(api_client)
    item_id = '7354954305222377999' # str | 作品id/Video id
offset = 0 # int | 偏移量/Offset (optional) (default to 0)
count = 20 # int | 数量/Count (optional) (default to 20)

    try:
        # 视频评论列表/Video comment list
        api_response = api_instance.fetch_video_comment_list_api_v1_xigua_app_v2_fetch_video_comment_list_get_0(item_id, offset=offset, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling XiguaAppV2APIApi->fetch_video_comment_list_api_v1_xigua_app_v2_fetch_video_comment_list_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| 作品id/Video id | 
 **offset** | **int**| 偏移量/Offset | [optional] [default to 0]
 **count** | **int**| 数量/Count | [optional] [default to 20]

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

# **search_video_api_v1_xigua_app_v2_search_video_get**
> ResponseModel search_video_api_v1_xigua_app_v2_search_video_get(keyword, offset=offset, order_type=order_type, min_duration=min_duration, max_duration=max_duration)

搜索视频/Search video

# [中文] ### 用途: - 搜索视频 ### 参数: - keyword: 关键词 - offset: 偏移量，第一次请求传0，后续请求传上一次请求返回的offset - order_type: 排序方式，为空时按照默认排序，以下为可选排序方式。     - 最新: publish_time     - 最热: play_count - min_duration: 最小时长，默认空，单位秒。 - max_duration: 最大时长，默认空，单位秒。 ### 返回: - 视频列表  # [English] ### Purpose: - Search video ### Parameters: - keyword: Keyword - offset: Offset, pass 0 for the first request, pass the offset returned by the previous request for subsequent requests - order_type: Order type, empty for default sorting, the following are optional sorting methods.     - Newest: publish_time     - Hottest: play_count - min_duration: Minimum duration, default empty, in seconds. - max_duration: Maximum duration, default empty, in seconds. ### Return: - Video list  # [示例/Example] > 搜索关键字为“抖音”的视频，按照播放量排序，时长1-180秒(1-3分钟) > Search for videos with the keyword \"抖音\", sorted by play count, duration 1-180 seconds (1-3 minutes) keyword: \"抖音\" order_type: \"play_count\" min_duration: 1 max_duration: 180

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
    api_instance = tikhub_sdk_v2.XiguaAppV2APIApi(api_client)
    keyword = '抖音' # str | 关键词/Keyword
offset = 0 # int | 偏移量/Offset (optional) (default to 0)
order_type = 'order_type_example' # str | 排序方式/Order type (optional)
min_duration = 56 # int | 最小时长/Minimum duration (optional)
max_duration = 56 # int | 最大时长/Maximum duration (optional)

    try:
        # 搜索视频/Search video
        api_response = api_instance.search_video_api_v1_xigua_app_v2_search_video_get(keyword, offset=offset, order_type=order_type, min_duration=min_duration, max_duration=max_duration)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling XiguaAppV2APIApi->search_video_api_v1_xigua_app_v2_search_video_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | **str**| 关键词/Keyword | 
 **offset** | **int**| 偏移量/Offset | [optional] [default to 0]
 **order_type** | **str**| 排序方式/Order type | [optional] 
 **min_duration** | **int**| 最小时长/Minimum duration | [optional] 
 **max_duration** | **int**| 最大时长/Maximum duration | [optional] 

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

# **search_video_api_v1_xigua_app_v2_search_video_get_0**
> ResponseModel search_video_api_v1_xigua_app_v2_search_video_get_0(keyword, offset=offset, order_type=order_type, min_duration=min_duration, max_duration=max_duration)

搜索视频/Search video

# [中文] ### 用途: - 搜索视频 ### 参数: - keyword: 关键词 - offset: 偏移量，第一次请求传0，后续请求传上一次请求返回的offset - order_type: 排序方式，为空时按照默认排序，以下为可选排序方式。     - 最新: publish_time     - 最热: play_count - min_duration: 最小时长，默认空，单位秒。 - max_duration: 最大时长，默认空，单位秒。 ### 返回: - 视频列表  # [English] ### Purpose: - Search video ### Parameters: - keyword: Keyword - offset: Offset, pass 0 for the first request, pass the offset returned by the previous request for subsequent requests - order_type: Order type, empty for default sorting, the following are optional sorting methods.     - Newest: publish_time     - Hottest: play_count - min_duration: Minimum duration, default empty, in seconds. - max_duration: Maximum duration, default empty, in seconds. ### Return: - Video list  # [示例/Example] > 搜索关键字为“抖音”的视频，按照播放量排序，时长1-180秒(1-3分钟) > Search for videos with the keyword \"抖音\", sorted by play count, duration 1-180 seconds (1-3 minutes) keyword: \"抖音\" order_type: \"play_count\" min_duration: 1 max_duration: 180

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
    api_instance = tikhub_sdk_v2.XiguaAppV2APIApi(api_client)
    keyword = '抖音' # str | 关键词/Keyword
offset = 0 # int | 偏移量/Offset (optional) (default to 0)
order_type = 'order_type_example' # str | 排序方式/Order type (optional)
min_duration = 56 # int | 最小时长/Minimum duration (optional)
max_duration = 56 # int | 最大时长/Maximum duration (optional)

    try:
        # 搜索视频/Search video
        api_response = api_instance.search_video_api_v1_xigua_app_v2_search_video_get_0(keyword, offset=offset, order_type=order_type, min_duration=min_duration, max_duration=max_duration)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling XiguaAppV2APIApi->search_video_api_v1_xigua_app_v2_search_video_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | **str**| 关键词/Keyword | 
 **offset** | **int**| 偏移量/Offset | [optional] [default to 0]
 **order_type** | **str**| 排序方式/Order type | [optional] 
 **min_duration** | **int**| 最小时长/Minimum duration | [optional] 
 **max_duration** | **int**| 最大时长/Maximum duration | [optional] 

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

