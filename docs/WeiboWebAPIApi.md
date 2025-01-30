# tikhub_sdk_v2.WeiboWebAPIApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_post_detail_api_v1_weibo_web_fetch_post_detail_get**](WeiboWebAPIApi.md#fetch_post_detail_api_v1_weibo_web_fetch_post_detail_get) | **GET** /api/v1/weibo/web/fetch_post_detail | 获取单个作品数据/Get single video data
[**fetch_post_detail_api_v1_weibo_web_fetch_post_detail_get_0**](WeiboWebAPIApi.md#fetch_post_detail_api_v1_weibo_web_fetch_post_detail_get_0) | **GET** /api/v1/weibo/web/fetch_post_detail | 获取单个作品数据/Get single video data
[**fetch_search_data_api_v1_weibo_web_fetch_search_data_get**](WeiboWebAPIApi.md#fetch_search_data_api_v1_weibo_web_fetch_search_data_get) | **GET** /api/v1/weibo/web/fetch_search_data | 获取搜索数据/Get search data
[**fetch_search_data_api_v1_weibo_web_fetch_search_data_get_0**](WeiboWebAPIApi.md#fetch_search_data_api_v1_weibo_web_fetch_search_data_get_0) | **GET** /api/v1/weibo/web/fetch_search_data | 获取搜索数据/Get search data
[**fetch_short_video_data_api_v1_weibo_web_fetch_short_video_data_get**](WeiboWebAPIApi.md#fetch_short_video_data_api_v1_weibo_web_fetch_short_video_data_get) | **GET** /api/v1/weibo/web/fetch_short_video_data | 获取短视频数据/Get short video data
[**fetch_short_video_data_api_v1_weibo_web_fetch_short_video_data_get_0**](WeiboWebAPIApi.md#fetch_short_video_data_api_v1_weibo_web_fetch_short_video_data_get_0) | **GET** /api/v1/weibo/web/fetch_short_video_data | 获取短视频数据/Get short video data
[**fetch_topic_detail_api_v1_weibo_web_fetch_topic_detail_get**](WeiboWebAPIApi.md#fetch_topic_detail_api_v1_weibo_web_fetch_topic_detail_get) | **GET** /api/v1/weibo/web/fetch_topic_detail | 获取话题详情/Get topic details
[**fetch_topic_detail_api_v1_weibo_web_fetch_topic_detail_get_0**](WeiboWebAPIApi.md#fetch_topic_detail_api_v1_weibo_web_fetch_topic_detail_get_0) | **GET** /api/v1/weibo/web/fetch_topic_detail | 获取话题详情/Get topic details
[**fetch_topic_stats_api_v1_weibo_web_fetch_topic_stats_get**](WeiboWebAPIApi.md#fetch_topic_stats_api_v1_weibo_web_fetch_topic_stats_get) | **GET** /api/v1/weibo/web/fetch_topic_stats | 获取话题统计数据/Get topic statistics
[**fetch_topic_stats_api_v1_weibo_web_fetch_topic_stats_get_0**](WeiboWebAPIApi.md#fetch_topic_stats_api_v1_weibo_web_fetch_topic_stats_get_0) | **GET** /api/v1/weibo/web/fetch_topic_stats | 获取话题统计数据/Get topic statistics
[**fetch_user_info_api_v1_weibo_web_fetch_user_info_get**](WeiboWebAPIApi.md#fetch_user_info_api_v1_weibo_web_fetch_user_info_get) | **GET** /api/v1/weibo/web/fetch_user_info | 获取用户信息/Get user information
[**fetch_user_info_api_v1_weibo_web_fetch_user_info_get_0**](WeiboWebAPIApi.md#fetch_user_info_api_v1_weibo_web_fetch_user_info_get_0) | **GET** /api/v1/weibo/web/fetch_user_info | 获取用户信息/Get user information
[**fetch_user_info_v2_api_v1_weibo_web_fetch_user_info_v2_get**](WeiboWebAPIApi.md#fetch_user_info_v2_api_v1_weibo_web_fetch_user_info_v2_get) | **GET** /api/v1/weibo/web/fetch_user_info_v2 | 获取用户信息V2/Get user information V2
[**fetch_user_info_v2_api_v1_weibo_web_fetch_user_info_v2_get_0**](WeiboWebAPIApi.md#fetch_user_info_v2_api_v1_weibo_web_fetch_user_info_v2_get_0) | **GET** /api/v1/weibo/web/fetch_user_info_v2 | 获取用户信息V2/Get user information V2
[**fetch_user_posts_api_v1_weibo_web_fetch_user_posts_get**](WeiboWebAPIApi.md#fetch_user_posts_api_v1_weibo_web_fetch_user_posts_get) | **GET** /api/v1/weibo/web/fetch_user_posts | 获取微博用户文章数据/Get Weibo user article data
[**fetch_user_posts_api_v1_weibo_web_fetch_user_posts_get_0**](WeiboWebAPIApi.md#fetch_user_posts_api_v1_weibo_web_fetch_user_posts_get_0) | **GET** /api/v1/weibo/web/fetch_user_posts | 获取微博用户文章数据/Get Weibo user article data


# **fetch_post_detail_api_v1_weibo_web_fetch_post_detail_get**
> ResponseModel fetch_post_detail_api_v1_weibo_web_fetch_post_detail_get(id)

获取单个作品数据/Get single video data

# [中文] ### 用途: - 获取单个作品数据 ### 参数: - id: 作品id，从分享链接中获取  - https://weibo.com/5819018196/5092682368025584  - 作品id为：5092682368025584 ### 返回: - 作品数据  # [English] ### Purpose: - Get single video data ### Parameters: - id: Post id, obtained from the sharing link     - https://weibo.com/5819018196/5092682368025584     - The post id is: 5092682368025584 ### Return: - Post data  # [示例/Example] id = \"5092682368025584\"

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
    api_instance = tikhub_sdk_v2.WeiboWebAPIApi(api_client)
    id = '5092682368025584' # str | 作品id/Post id

    try:
        # 获取单个作品数据/Get single video data
        api_response = api_instance.fetch_post_detail_api_v1_weibo_web_fetch_post_detail_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WeiboWebAPIApi->fetch_post_detail_api_v1_weibo_web_fetch_post_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 作品id/Post id | 

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

# **fetch_post_detail_api_v1_weibo_web_fetch_post_detail_get_0**
> ResponseModel fetch_post_detail_api_v1_weibo_web_fetch_post_detail_get_0(id)

获取单个作品数据/Get single video data

# [中文] ### 用途: - 获取单个作品数据 ### 参数: - id: 作品id，从分享链接中获取  - https://weibo.com/5819018196/5092682368025584  - 作品id为：5092682368025584 ### 返回: - 作品数据  # [English] ### Purpose: - Get single video data ### Parameters: - id: Post id, obtained from the sharing link     - https://weibo.com/5819018196/5092682368025584     - The post id is: 5092682368025584 ### Return: - Post data  # [示例/Example] id = \"5092682368025584\"

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
    api_instance = tikhub_sdk_v2.WeiboWebAPIApi(api_client)
    id = '5092682368025584' # str | 作品id/Post id

    try:
        # 获取单个作品数据/Get single video data
        api_response = api_instance.fetch_post_detail_api_v1_weibo_web_fetch_post_detail_get_0(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WeiboWebAPIApi->fetch_post_detail_api_v1_weibo_web_fetch_post_detail_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 作品id/Post id | 

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

# **fetch_search_data_api_v1_weibo_web_fetch_search_data_get**
> ResponseModel fetch_search_data_api_v1_weibo_web_fetch_search_data_get(keyword, page=page, search_type=search_type)

获取搜索数据/Get search data

# [中文] ### 用途: - 获取搜索数据 ### 参数: - keyword: 关键词 - page: 页数 - search_type: 搜索类型     - **1**: 综合     - **61**: 实时     - **3**: 用户     - **60**: 热门     - **64**: 视频     - **63**: 图片     - **21**: 文章     - **38**: 话题     - **98**: 超话 ### 返回: - 搜索数据  # [English] ### Purpose: - Get search data ### Parameters: - keyword: Keyword - page: Page number - search_type: Search type     - **1**: Comprehensive     - **61**: Real-time     - **3**: User     - **60**: Hot     - **64**: Video     - **63**: Picture     - **21**: Article     - **38**: Topic     - **98**: Super topic ### Return: - Search data  # [示例/Example] keyword = \"游戏\" page = \"1\" search_type = \"1\"

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
    api_instance = tikhub_sdk_v2.WeiboWebAPIApi(api_client)
    keyword = '游戏' # str | 关键词/Keyword
page = '1' # str | 页数/Page number (optional) (default to '1')
search_type = '1' # str | 搜索类型/Search type (optional) (default to '1')

    try:
        # 获取搜索数据/Get search data
        api_response = api_instance.fetch_search_data_api_v1_weibo_web_fetch_search_data_get(keyword, page=page, search_type=search_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WeiboWebAPIApi->fetch_search_data_api_v1_weibo_web_fetch_search_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | **str**| 关键词/Keyword | 
 **page** | **str**| 页数/Page number | [optional] [default to &#39;1&#39;]
 **search_type** | **str**| 搜索类型/Search type | [optional] [default to &#39;1&#39;]

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

# **fetch_search_data_api_v1_weibo_web_fetch_search_data_get_0**
> ResponseModel fetch_search_data_api_v1_weibo_web_fetch_search_data_get_0(keyword, page=page, search_type=search_type)

获取搜索数据/Get search data

# [中文] ### 用途: - 获取搜索数据 ### 参数: - keyword: 关键词 - page: 页数 - search_type: 搜索类型     - **1**: 综合     - **61**: 实时     - **3**: 用户     - **60**: 热门     - **64**: 视频     - **63**: 图片     - **21**: 文章     - **38**: 话题     - **98**: 超话 ### 返回: - 搜索数据  # [English] ### Purpose: - Get search data ### Parameters: - keyword: Keyword - page: Page number - search_type: Search type     - **1**: Comprehensive     - **61**: Real-time     - **3**: User     - **60**: Hot     - **64**: Video     - **63**: Picture     - **21**: Article     - **38**: Topic     - **98**: Super topic ### Return: - Search data  # [示例/Example] keyword = \"游戏\" page = \"1\" search_type = \"1\"

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
    api_instance = tikhub_sdk_v2.WeiboWebAPIApi(api_client)
    keyword = '游戏' # str | 关键词/Keyword
page = '1' # str | 页数/Page number (optional) (default to '1')
search_type = '1' # str | 搜索类型/Search type (optional) (default to '1')

    try:
        # 获取搜索数据/Get search data
        api_response = api_instance.fetch_search_data_api_v1_weibo_web_fetch_search_data_get_0(keyword, page=page, search_type=search_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WeiboWebAPIApi->fetch_search_data_api_v1_weibo_web_fetch_search_data_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | **str**| 关键词/Keyword | 
 **page** | **str**| 页数/Page number | [optional] [default to &#39;1&#39;]
 **search_type** | **str**| 搜索类型/Search type | [optional] [default to &#39;1&#39;]

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

# **fetch_short_video_data_api_v1_weibo_web_fetch_short_video_data_get**
> ResponseModel fetch_short_video_data_api_v1_weibo_web_fetch_short_video_data_get(share_text)

获取短视频数据/Get short video data

# [中文] ### 用途: - 获取短视频数据 ### 参数: - share_text: 视频分享链接 ### 返回: - 短视频数据  # [English] ### Purpose: - Get short video data ### Parameters: - share_text: Video sharing link ### Return: - Short video data  # [示例/Example] share_text = \"https://video.weibo.com/show?fid=1034:4986069612167172\"

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
    api_instance = tikhub_sdk_v2.WeiboWebAPIApi(api_client)
    share_text = 'https://video.weibo.com/show?fid=1034:4986069612167172' # str | 视频分享链接/Video sharing link

    try:
        # 获取短视频数据/Get short video data
        api_response = api_instance.fetch_short_video_data_api_v1_weibo_web_fetch_short_video_data_get(share_text)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WeiboWebAPIApi->fetch_short_video_data_api_v1_weibo_web_fetch_short_video_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_text** | **str**| 视频分享链接/Video sharing link | 

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

# **fetch_short_video_data_api_v1_weibo_web_fetch_short_video_data_get_0**
> ResponseModel fetch_short_video_data_api_v1_weibo_web_fetch_short_video_data_get_0(share_text)

获取短视频数据/Get short video data

# [中文] ### 用途: - 获取短视频数据 ### 参数: - share_text: 视频分享链接 ### 返回: - 短视频数据  # [English] ### Purpose: - Get short video data ### Parameters: - share_text: Video sharing link ### Return: - Short video data  # [示例/Example] share_text = \"https://video.weibo.com/show?fid=1034:4986069612167172\"

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
    api_instance = tikhub_sdk_v2.WeiboWebAPIApi(api_client)
    share_text = 'https://video.weibo.com/show?fid=1034:4986069612167172' # str | 视频分享链接/Video sharing link

    try:
        # 获取短视频数据/Get short video data
        api_response = api_instance.fetch_short_video_data_api_v1_weibo_web_fetch_short_video_data_get_0(share_text)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WeiboWebAPIApi->fetch_short_video_data_api_v1_weibo_web_fetch_short_video_data_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_text** | **str**| 视频分享链接/Video sharing link | 

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

# **fetch_topic_detail_api_v1_weibo_web_fetch_topic_detail_get**
> ResponseModel fetch_topic_detail_api_v1_weibo_web_fetch_topic_detail_get(topic_name, page=page)

获取话题详情/Get topic details

# [中文] ### 用途: - 获取话题详情 ### 参数: - topic_name: 话题名称 - page: 页数 ### 返回: - 话题详情  # [English] ### Purpose: - Get topic details ### Parameters: - topic_name: Topic name - page: Page number ### Return: - Topic details  # [示例/Example] topic_name = \"游戏\" page = \"\"

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
    api_instance = tikhub_sdk_v2.WeiboWebAPIApi(api_client)
    topic_name = '游戏' # str | 话题名称/Topic name
page = '' # str | 页数/Page number (optional) (default to '')

    try:
        # 获取话题详情/Get topic details
        api_response = api_instance.fetch_topic_detail_api_v1_weibo_web_fetch_topic_detail_get(topic_name, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WeiboWebAPIApi->fetch_topic_detail_api_v1_weibo_web_fetch_topic_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_name** | **str**| 话题名称/Topic name | 
 **page** | **str**| 页数/Page number | [optional] [default to &#39;&#39;]

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

# **fetch_topic_detail_api_v1_weibo_web_fetch_topic_detail_get_0**
> ResponseModel fetch_topic_detail_api_v1_weibo_web_fetch_topic_detail_get_0(topic_name, page=page)

获取话题详情/Get topic details

# [中文] ### 用途: - 获取话题详情 ### 参数: - topic_name: 话题名称 - page: 页数 ### 返回: - 话题详情  # [English] ### Purpose: - Get topic details ### Parameters: - topic_name: Topic name - page: Page number ### Return: - Topic details  # [示例/Example] topic_name = \"游戏\" page = \"\"

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
    api_instance = tikhub_sdk_v2.WeiboWebAPIApi(api_client)
    topic_name = '游戏' # str | 话题名称/Topic name
page = '' # str | 页数/Page number (optional) (default to '')

    try:
        # 获取话题详情/Get topic details
        api_response = api_instance.fetch_topic_detail_api_v1_weibo_web_fetch_topic_detail_get_0(topic_name, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WeiboWebAPIApi->fetch_topic_detail_api_v1_weibo_web_fetch_topic_detail_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_name** | **str**| 话题名称/Topic name | 
 **page** | **str**| 页数/Page number | [optional] [default to &#39;&#39;]

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

# **fetch_topic_stats_api_v1_weibo_web_fetch_topic_stats_get**
> ResponseModel fetch_topic_stats_api_v1_weibo_web_fetch_topic_stats_get(topic_name)

获取话题统计数据/Get topic statistics

# [中文] ### 用途: - 获取话题统计数据 ### 参数: - topic_name: 话题名称 ### 返回: - 话题统计数据  # [English] ### Purpose: - Get topic statistics ### Parameters: - topic_name: Topic name ### Return: - Topic statistics  # [示例/Example] topic_name = \"游戏\"

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
    api_instance = tikhub_sdk_v2.WeiboWebAPIApi(api_client)
    topic_name = '游戏' # str | 话题名称/Topic name

    try:
        # 获取话题统计数据/Get topic statistics
        api_response = api_instance.fetch_topic_stats_api_v1_weibo_web_fetch_topic_stats_get(topic_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WeiboWebAPIApi->fetch_topic_stats_api_v1_weibo_web_fetch_topic_stats_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_name** | **str**| 话题名称/Topic name | 

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

# **fetch_topic_stats_api_v1_weibo_web_fetch_topic_stats_get_0**
> ResponseModel fetch_topic_stats_api_v1_weibo_web_fetch_topic_stats_get_0(topic_name)

获取话题统计数据/Get topic statistics

# [中文] ### 用途: - 获取话题统计数据 ### 参数: - topic_name: 话题名称 ### 返回: - 话题统计数据  # [English] ### Purpose: - Get topic statistics ### Parameters: - topic_name: Topic name ### Return: - Topic statistics  # [示例/Example] topic_name = \"游戏\"

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
    api_instance = tikhub_sdk_v2.WeiboWebAPIApi(api_client)
    topic_name = '游戏' # str | 话题名称/Topic name

    try:
        # 获取话题统计数据/Get topic statistics
        api_response = api_instance.fetch_topic_stats_api_v1_weibo_web_fetch_topic_stats_get_0(topic_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WeiboWebAPIApi->fetch_topic_stats_api_v1_weibo_web_fetch_topic_stats_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_name** | **str**| 话题名称/Topic name | 

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

# **fetch_user_info_api_v1_weibo_web_fetch_user_info_get**
> ResponseModel fetch_user_info_api_v1_weibo_web_fetch_user_info_get(uid)

获取用户信息/Get user information

# [中文] ### 用途: - 获取用户信息 ### 参数: - uid: 用户id ### 返回: - 用户信息  # [English] ### Purpose: - Get user information ### Parameters: - uid: User id ### Return: - User information  # [示例/Example] uid = \"7277477906\"

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
    api_instance = tikhub_sdk_v2.WeiboWebAPIApi(api_client)
    uid = '7277477906' # str | 用户id/User id

    try:
        # 获取用户信息/Get user information
        api_response = api_instance.fetch_user_info_api_v1_weibo_web_fetch_user_info_get(uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WeiboWebAPIApi->fetch_user_info_api_v1_weibo_web_fetch_user_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| 用户id/User id | 

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

# **fetch_user_info_api_v1_weibo_web_fetch_user_info_get_0**
> ResponseModel fetch_user_info_api_v1_weibo_web_fetch_user_info_get_0(uid)

获取用户信息/Get user information

# [中文] ### 用途: - 获取用户信息 ### 参数: - uid: 用户id ### 返回: - 用户信息  # [English] ### Purpose: - Get user information ### Parameters: - uid: User id ### Return: - User information  # [示例/Example] uid = \"7277477906\"

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
    api_instance = tikhub_sdk_v2.WeiboWebAPIApi(api_client)
    uid = '7277477906' # str | 用户id/User id

    try:
        # 获取用户信息/Get user information
        api_response = api_instance.fetch_user_info_api_v1_weibo_web_fetch_user_info_get_0(uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WeiboWebAPIApi->fetch_user_info_api_v1_weibo_web_fetch_user_info_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| 用户id/User id | 

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

# **fetch_user_info_v2_api_v1_weibo_web_fetch_user_info_v2_get**
> ResponseModel fetch_user_info_v2_api_v1_weibo_web_fetch_user_info_v2_get(uid)

获取用户信息V2/Get user information V2

# [中文] ### 用途: - 获取用户信息V2 ### 参数: - uid: 用户id ### 返回: - 用户信息  # [English] ### Purpose: - Get user information V2 ### Parameters: - uid: User id ### Return: - User information  # [示例/Example] uid = \"7277477906\"

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
    api_instance = tikhub_sdk_v2.WeiboWebAPIApi(api_client)
    uid = '7277477906' # str | 用户id/User id

    try:
        # 获取用户信息V2/Get user information V2
        api_response = api_instance.fetch_user_info_v2_api_v1_weibo_web_fetch_user_info_v2_get(uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WeiboWebAPIApi->fetch_user_info_v2_api_v1_weibo_web_fetch_user_info_v2_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| 用户id/User id | 

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

# **fetch_user_info_v2_api_v1_weibo_web_fetch_user_info_v2_get_0**
> ResponseModel fetch_user_info_v2_api_v1_weibo_web_fetch_user_info_v2_get_0(uid)

获取用户信息V2/Get user information V2

# [中文] ### 用途: - 获取用户信息V2 ### 参数: - uid: 用户id ### 返回: - 用户信息  # [English] ### Purpose: - Get user information V2 ### Parameters: - uid: User id ### Return: - User information  # [示例/Example] uid = \"7277477906\"

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
    api_instance = tikhub_sdk_v2.WeiboWebAPIApi(api_client)
    uid = '7277477906' # str | 用户id/User id

    try:
        # 获取用户信息V2/Get user information V2
        api_response = api_instance.fetch_user_info_v2_api_v1_weibo_web_fetch_user_info_v2_get_0(uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WeiboWebAPIApi->fetch_user_info_v2_api_v1_weibo_web_fetch_user_info_v2_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| 用户id/User id | 

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

# **fetch_user_posts_api_v1_weibo_web_fetch_user_posts_get**
> ResponseModel fetch_user_posts_api_v1_weibo_web_fetch_user_posts_get(uid, page=page, feature=feature)

获取微博用户文章数据/Get Weibo user article data

# [中文] ### 用途: - 获取微博用户文章数据 ### 参数: - uid: 用户id - page: 页数 - feature: 特征 ### 返回: - 用户文章数据  # [English] ### Purpose: - Get Weibo user article data ### Parameters: - uid: User id - page: Page number - feature: Feature ### Return: - User article data  # [示例/Example] uid = \"7277477906\" page = 1 feature = 0

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
    api_instance = tikhub_sdk_v2.WeiboWebAPIApi(api_client)
    uid = '7277477906' # str | 用户id/User id
page = 1 # int | 页数/Page number (optional) (default to 1)
feature = 0 # int | 特征/Feature (optional) (default to 0)

    try:
        # 获取微博用户文章数据/Get Weibo user article data
        api_response = api_instance.fetch_user_posts_api_v1_weibo_web_fetch_user_posts_get(uid, page=page, feature=feature)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WeiboWebAPIApi->fetch_user_posts_api_v1_weibo_web_fetch_user_posts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| 用户id/User id | 
 **page** | **int**| 页数/Page number | [optional] [default to 1]
 **feature** | **int**| 特征/Feature | [optional] [default to 0]

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

# **fetch_user_posts_api_v1_weibo_web_fetch_user_posts_get_0**
> ResponseModel fetch_user_posts_api_v1_weibo_web_fetch_user_posts_get_0(uid, page=page, feature=feature)

获取微博用户文章数据/Get Weibo user article data

# [中文] ### 用途: - 获取微博用户文章数据 ### 参数: - uid: 用户id - page: 页数 - feature: 特征 ### 返回: - 用户文章数据  # [English] ### Purpose: - Get Weibo user article data ### Parameters: - uid: User id - page: Page number - feature: Feature ### Return: - User article data  # [示例/Example] uid = \"7277477906\" page = 1 feature = 0

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
    api_instance = tikhub_sdk_v2.WeiboWebAPIApi(api_client)
    uid = '7277477906' # str | 用户id/User id
page = 1 # int | 页数/Page number (optional) (default to 1)
feature = 0 # int | 特征/Feature (optional) (default to 0)

    try:
        # 获取微博用户文章数据/Get Weibo user article data
        api_response = api_instance.fetch_user_posts_api_v1_weibo_web_fetch_user_posts_get_0(uid, page=page, feature=feature)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WeiboWebAPIApi->fetch_user_posts_api_v1_weibo_web_fetch_user_posts_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| 用户id/User id | 
 **page** | **int**| 页数/Page number | [optional] [default to 1]
 **feature** | **int**| 特征/Feature | [optional] [default to 0]

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

