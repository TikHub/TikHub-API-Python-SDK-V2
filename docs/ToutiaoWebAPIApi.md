# tikhub_sdk_v2.ToutiaoWebAPIApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_article_info_api_v1_toutiao_web_get_article_info_get**](ToutiaoWebAPIApi.md#get_article_info_api_v1_toutiao_web_get_article_info_get) | **GET** /api/v1/toutiao/web/get_article_info | 获取指定文章的信息/Get information of specified article
[**get_article_info_api_v1_toutiao_web_get_article_info_get_0**](ToutiaoWebAPIApi.md#get_article_info_api_v1_toutiao_web_get_article_info_get_0) | **GET** /api/v1/toutiao/web/get_article_info | 获取指定文章的信息/Get information of specified article
[**get_video_info_api_v1_toutiao_web_get_video_info_get**](ToutiaoWebAPIApi.md#get_video_info_api_v1_toutiao_web_get_video_info_get) | **GET** /api/v1/toutiao/web/get_video_info | 获取指定视频的信息/Get information of specified video
[**get_video_info_api_v1_toutiao_web_get_video_info_get_0**](ToutiaoWebAPIApi.md#get_video_info_api_v1_toutiao_web_get_video_info_get_0) | **GET** /api/v1/toutiao/web/get_video_info | 获取指定视频的信息/Get information of specified video


# **get_article_info_api_v1_toutiao_web_get_article_info_get**
> ResponseModel get_article_info_api_v1_toutiao_web_get_article_info_get(aweme_id)

获取指定文章的信息/Get information of specified article

# [中文] ### 用途: - 获取指定文章的信息 ### 参数: - aweme_id: 作品ID，可以从链接中获取     - 例如: https://www.toutiao.com/article/7450114952884503059/ ### 返回: - 作品信息  # [English] ### Purpose: - Get information of specified post ### Parameters: - item_id: Post ID, can be obtained from the link     - For example: https://www.toutiao.com/article/7450114952884503059/ ### Return: - Post information  # [示例/Example] aweme_id = \"7450114952884503059\"

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
    api_instance = tikhub_sdk_v2.ToutiaoWebAPIApi(api_client)
    aweme_id = '7450114952884503059' # str | 作品ID/Post ID

    try:
        # 获取指定文章的信息/Get information of specified article
        api_response = api_instance.get_article_info_api_v1_toutiao_web_get_article_info_get(aweme_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ToutiaoWebAPIApi->get_article_info_api_v1_toutiao_web_get_article_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aweme_id** | **str**| 作品ID/Post ID | 

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

# **get_article_info_api_v1_toutiao_web_get_article_info_get_0**
> ResponseModel get_article_info_api_v1_toutiao_web_get_article_info_get_0(aweme_id)

获取指定文章的信息/Get information of specified article

# [中文] ### 用途: - 获取指定文章的信息 ### 参数: - aweme_id: 作品ID，可以从链接中获取     - 例如: https://www.toutiao.com/article/7450114952884503059/ ### 返回: - 作品信息  # [English] ### Purpose: - Get information of specified post ### Parameters: - item_id: Post ID, can be obtained from the link     - For example: https://www.toutiao.com/article/7450114952884503059/ ### Return: - Post information  # [示例/Example] aweme_id = \"7450114952884503059\"

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
    api_instance = tikhub_sdk_v2.ToutiaoWebAPIApi(api_client)
    aweme_id = '7450114952884503059' # str | 作品ID/Post ID

    try:
        # 获取指定文章的信息/Get information of specified article
        api_response = api_instance.get_article_info_api_v1_toutiao_web_get_article_info_get_0(aweme_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ToutiaoWebAPIApi->get_article_info_api_v1_toutiao_web_get_article_info_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aweme_id** | **str**| 作品ID/Post ID | 

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

# **get_video_info_api_v1_toutiao_web_get_video_info_get**
> ResponseModel get_video_info_api_v1_toutiao_web_get_video_info_get(aweme_id)

获取指定视频的信息/Get information of specified video

# [中文] ### 用途: - 获取指定视频的信息 ### 参数: - aweme_id: 作品ID，可以从链接中获取     - 例如: https://www.toutiao.com/video/7431543350882206242/ ### 返回: - 作品信息  # [English] ### Purpose: - Get information of specified video ### Parameters: - item_id: Post ID, can be obtained from the link     - For example: https://www.toutiao.com/video/7431543350882206242/ ### Return: - Post information  # [示例/Example] aweme_id = \"7431543350882206242\"

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
    api_instance = tikhub_sdk_v2.ToutiaoWebAPIApi(api_client)
    aweme_id = '7431543350882206242' # str | 作品ID/Post ID

    try:
        # 获取指定视频的信息/Get information of specified video
        api_response = api_instance.get_video_info_api_v1_toutiao_web_get_video_info_get(aweme_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ToutiaoWebAPIApi->get_video_info_api_v1_toutiao_web_get_video_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aweme_id** | **str**| 作品ID/Post ID | 

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

# **get_video_info_api_v1_toutiao_web_get_video_info_get_0**
> ResponseModel get_video_info_api_v1_toutiao_web_get_video_info_get_0(aweme_id)

获取指定视频的信息/Get information of specified video

# [中文] ### 用途: - 获取指定视频的信息 ### 参数: - aweme_id: 作品ID，可以从链接中获取     - 例如: https://www.toutiao.com/video/7431543350882206242/ ### 返回: - 作品信息  # [English] ### Purpose: - Get information of specified video ### Parameters: - item_id: Post ID, can be obtained from the link     - For example: https://www.toutiao.com/video/7431543350882206242/ ### Return: - Post information  # [示例/Example] aweme_id = \"7431543350882206242\"

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
    api_instance = tikhub_sdk_v2.ToutiaoWebAPIApi(api_client)
    aweme_id = '7431543350882206242' # str | 作品ID/Post ID

    try:
        # 获取指定视频的信息/Get information of specified video
        api_response = api_instance.get_video_info_api_v1_toutiao_web_get_video_info_get_0(aweme_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ToutiaoWebAPIApi->get_video_info_api_v1_toutiao_web_get_video_info_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aweme_id** | **str**| 作品ID/Post ID | 

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

