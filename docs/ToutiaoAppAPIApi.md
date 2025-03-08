# tikhub_sdk_v2.ToutiaoAppAPIApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_article_info_api_v1_toutiao_app_get_article_info_get**](ToutiaoAppAPIApi.md#get_article_info_api_v1_toutiao_app_get_article_info_get) | **GET** /api/v1/toutiao/app/get_article_info | 获取指定文章的信息/Get information of specified article
[**get_article_info_api_v1_toutiao_app_get_article_info_get_0**](ToutiaoAppAPIApi.md#get_article_info_api_v1_toutiao_app_get_article_info_get_0) | **GET** /api/v1/toutiao/app/get_article_info | 获取指定文章的信息/Get information of specified article
[**get_comments_api_v1_toutiao_app_get_comments_get**](ToutiaoAppAPIApi.md#get_comments_api_v1_toutiao_app_get_comments_get) | **GET** /api/v1/toutiao/app/get_comments | 获取指定作品的评论/Get comments of specified post
[**get_comments_api_v1_toutiao_app_get_comments_get_0**](ToutiaoAppAPIApi.md#get_comments_api_v1_toutiao_app_get_comments_get_0) | **GET** /api/v1/toutiao/app/get_comments | 获取指定作品的评论/Get comments of specified post
[**get_user_id_api_v1_toutiao_app_get_user_id_get**](ToutiaoAppAPIApi.md#get_user_id_api_v1_toutiao_app_get_user_id_get) | **GET** /api/v1/toutiao/app/get_user_id | 从头条用户主页获取用户user_id/Get user_id from user profile
[**get_user_id_api_v1_toutiao_app_get_user_id_get_0**](ToutiaoAppAPIApi.md#get_user_id_api_v1_toutiao_app_get_user_id_get_0) | **GET** /api/v1/toutiao/app/get_user_id | 从头条用户主页获取用户user_id/Get user_id from user profile
[**get_user_info_api_v1_toutiao_app_get_user_info_get**](ToutiaoAppAPIApi.md#get_user_info_api_v1_toutiao_app_get_user_info_get) | **GET** /api/v1/toutiao/app/get_user_info | 获取指定用户的信息/Get information of specified user
[**get_user_info_api_v1_toutiao_app_get_user_info_get_0**](ToutiaoAppAPIApi.md#get_user_info_api_v1_toutiao_app_get_user_info_get_0) | **GET** /api/v1/toutiao/app/get_user_info | 获取指定用户的信息/Get information of specified user
[**get_video_info_api_v1_toutiao_app_get_video_info_get**](ToutiaoAppAPIApi.md#get_video_info_api_v1_toutiao_app_get_video_info_get) | **GET** /api/v1/toutiao/app/get_video_info | 获取指定视频的信息/Get information of specified video
[**get_video_info_api_v1_toutiao_app_get_video_info_get_0**](ToutiaoAppAPIApi.md#get_video_info_api_v1_toutiao_app_get_video_info_get_0) | **GET** /api/v1/toutiao/app/get_video_info | 获取指定视频的信息/Get information of specified video


# **get_article_info_api_v1_toutiao_app_get_article_info_get**
> ResponseModel get_article_info_api_v1_toutiao_app_get_article_info_get(group_id)

获取指定文章的信息/Get information of specified article

# [中文] ### 用途: - 获取指定文章的信息 ### 参数: - group_id: 作品ID，可以从链接中获取     - 例如: https://www.toutiao.com/article/7450114952884503059/ ### 返回: - 作品信息  # [English] ### Purpose: - Get information of specified post ### Parameters: - group_id: Post ID, can be obtained from the link     - For example: https://www.toutiao.com/article/7450114952884503059/ ### Return: - Post information  # [示例/Example] group_id = \"7450114952884503059\"

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
    api_instance = tikhub_sdk_v2.ToutiaoAppAPIApi(api_client)
    group_id = '7450114952884503059' # str | 作品ID/Post ID

    try:
        # 获取指定文章的信息/Get information of specified article
        api_response = api_instance.get_article_info_api_v1_toutiao_app_get_article_info_get(group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ToutiaoAppAPIApi->get_article_info_api_v1_toutiao_app_get_article_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| 作品ID/Post ID | 

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

# **get_article_info_api_v1_toutiao_app_get_article_info_get_0**
> ResponseModel get_article_info_api_v1_toutiao_app_get_article_info_get_0(group_id)

获取指定文章的信息/Get information of specified article

# [中文] ### 用途: - 获取指定文章的信息 ### 参数: - group_id: 作品ID，可以从链接中获取     - 例如: https://www.toutiao.com/article/7450114952884503059/ ### 返回: - 作品信息  # [English] ### Purpose: - Get information of specified post ### Parameters: - group_id: Post ID, can be obtained from the link     - For example: https://www.toutiao.com/article/7450114952884503059/ ### Return: - Post information  # [示例/Example] group_id = \"7450114952884503059\"

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
    api_instance = tikhub_sdk_v2.ToutiaoAppAPIApi(api_client)
    group_id = '7450114952884503059' # str | 作品ID/Post ID

    try:
        # 获取指定文章的信息/Get information of specified article
        api_response = api_instance.get_article_info_api_v1_toutiao_app_get_article_info_get_0(group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ToutiaoAppAPIApi->get_article_info_api_v1_toutiao_app_get_article_info_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| 作品ID/Post ID | 

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

# **get_comments_api_v1_toutiao_app_get_comments_get**
> ResponseModel get_comments_api_v1_toutiao_app_get_comments_get(group_id, offset)

获取指定作品的评论/Get comments of specified post

# [中文] ### 用途: - 获取指定作品的评论 ### 参数: - group_id: 作品ID，可以从链接中获取     - 例如: https://www.toutiao.com/i7453372680222523931/ - offset: 偏移量，用于分页，默认为0，然后每次加20 ### 返回: - 评论列表  # [English] ### Purpose: - Get comments of specified post ### Parameters: - group_id: Post ID, can be obtained from the link     - For example: https://www.toutiao.com/i7453372680222523931/ - offset: Offset, used for pagination, default is 0, then add 20 each time ### Return: - Comment list  # [示例/Example] group_id = \"7453372680222523931\" offset = \"0\"

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
    api_instance = tikhub_sdk_v2.ToutiaoAppAPIApi(api_client)
    group_id = '7453372680222523931' # str | 作品ID/Post ID
offset = '0' # str | 偏移量/Offset

    try:
        # 获取指定作品的评论/Get comments of specified post
        api_response = api_instance.get_comments_api_v1_toutiao_app_get_comments_get(group_id, offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ToutiaoAppAPIApi->get_comments_api_v1_toutiao_app_get_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| 作品ID/Post ID | 
 **offset** | **str**| 偏移量/Offset | 

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

# **get_comments_api_v1_toutiao_app_get_comments_get_0**
> ResponseModel get_comments_api_v1_toutiao_app_get_comments_get_0(group_id, offset)

获取指定作品的评论/Get comments of specified post

# [中文] ### 用途: - 获取指定作品的评论 ### 参数: - group_id: 作品ID，可以从链接中获取     - 例如: https://www.toutiao.com/i7453372680222523931/ - offset: 偏移量，用于分页，默认为0，然后每次加20 ### 返回: - 评论列表  # [English] ### Purpose: - Get comments of specified post ### Parameters: - group_id: Post ID, can be obtained from the link     - For example: https://www.toutiao.com/i7453372680222523931/ - offset: Offset, used for pagination, default is 0, then add 20 each time ### Return: - Comment list  # [示例/Example] group_id = \"7453372680222523931\" offset = \"0\"

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
    api_instance = tikhub_sdk_v2.ToutiaoAppAPIApi(api_client)
    group_id = '7453372680222523931' # str | 作品ID/Post ID
offset = '0' # str | 偏移量/Offset

    try:
        # 获取指定作品的评论/Get comments of specified post
        api_response = api_instance.get_comments_api_v1_toutiao_app_get_comments_get_0(group_id, offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ToutiaoAppAPIApi->get_comments_api_v1_toutiao_app_get_comments_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| 作品ID/Post ID | 
 **offset** | **str**| 偏移量/Offset | 

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

# **get_user_id_api_v1_toutiao_app_get_user_id_get**
> ResponseModel get_user_id_api_v1_toutiao_app_get_user_id_get(user_profile_url)

从头条用户主页获取用户user_id/Get user_id from user profile

# [中文] ### 用途: - 从头条用户主页获取用户user_id ### 参数: - user_profile_url: 用户主页链接     - 例如: https://www.toutiao.com/c/user/token/MS4wLjABAAAAwK6echNksY69R8l2vcZudupfhTItbGSGt-8ineO5UaB4L-djqkYDgB6TkAdMvrmW/ ### 返回: - 用户ID  # [English] ### Purpose: - Get user_id from user profile ### Parameters: - user_profile_url: User profile URL     - For example: https://www.toutiao.com/c/user/token/MS4wLjABAAAAwK6echNksY69R8l2vcZudupfhTItbGSGt-8ineO5UaB4L-djqkYDgB6TkAdMvrmW/ ### Return: - User ID  # [示例/Example] user_profile_url = \"https://www.toutiao.com/c/user/token/MS4wLjABAAAAwK6echNksY69R8l2vcZudupfhTItbGSGt-8ineO5UaB4L-djqkYDgB6TkAdMvrmW/\"

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
    api_instance = tikhub_sdk_v2.ToutiaoAppAPIApi(api_client)
    user_profile_url = 'https://www.toutiao.com/c/user/token/MS4wLjABAAAAwK6echNksY69R8l2vcZudupfhTItbGSGt-8ineO5UaB4L-djqkYDgB6TkAdMvrmW/' # str | 用户主页链接/User profile URL

    try:
        # 从头条用户主页获取用户user_id/Get user_id from user profile
        api_response = api_instance.get_user_id_api_v1_toutiao_app_get_user_id_get(user_profile_url)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ToutiaoAppAPIApi->get_user_id_api_v1_toutiao_app_get_user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_profile_url** | **str**| 用户主页链接/User profile URL | 

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

# **get_user_id_api_v1_toutiao_app_get_user_id_get_0**
> ResponseModel get_user_id_api_v1_toutiao_app_get_user_id_get_0(user_profile_url)

从头条用户主页获取用户user_id/Get user_id from user profile

# [中文] ### 用途: - 从头条用户主页获取用户user_id ### 参数: - user_profile_url: 用户主页链接     - 例如: https://www.toutiao.com/c/user/token/MS4wLjABAAAAwK6echNksY69R8l2vcZudupfhTItbGSGt-8ineO5UaB4L-djqkYDgB6TkAdMvrmW/ ### 返回: - 用户ID  # [English] ### Purpose: - Get user_id from user profile ### Parameters: - user_profile_url: User profile URL     - For example: https://www.toutiao.com/c/user/token/MS4wLjABAAAAwK6echNksY69R8l2vcZudupfhTItbGSGt-8ineO5UaB4L-djqkYDgB6TkAdMvrmW/ ### Return: - User ID  # [示例/Example] user_profile_url = \"https://www.toutiao.com/c/user/token/MS4wLjABAAAAwK6echNksY69R8l2vcZudupfhTItbGSGt-8ineO5UaB4L-djqkYDgB6TkAdMvrmW/\"

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
    api_instance = tikhub_sdk_v2.ToutiaoAppAPIApi(api_client)
    user_profile_url = 'https://www.toutiao.com/c/user/token/MS4wLjABAAAAwK6echNksY69R8l2vcZudupfhTItbGSGt-8ineO5UaB4L-djqkYDgB6TkAdMvrmW/' # str | 用户主页链接/User profile URL

    try:
        # 从头条用户主页获取用户user_id/Get user_id from user profile
        api_response = api_instance.get_user_id_api_v1_toutiao_app_get_user_id_get_0(user_profile_url)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ToutiaoAppAPIApi->get_user_id_api_v1_toutiao_app_get_user_id_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_profile_url** | **str**| 用户主页链接/User profile URL | 

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

# **get_user_info_api_v1_toutiao_app_get_user_info_get**
> ResponseModel get_user_info_api_v1_toutiao_app_get_user_info_get(user_id)

获取指定用户的信息/Get information of specified user

# [中文] ### 用途: - 获取指定用户的信息 ### 参数: - user_id: 用户ID，可以从以下接口获取：     - `/api/v1/toutiao/app/get_user_id` ### 返回: - 用户信息  # [English] ### Purpose: - Get information of specified user ### Parameters: - user_id: User ID, can be obtained from the following API:     - `/api/v1/toutiao/app/get_user_id` ### Return: - User information  # [示例/Example] user_id = \"1352838578180211\"

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
    api_instance = tikhub_sdk_v2.ToutiaoAppAPIApi(api_client)
    user_id = '1352838578180211' # str | 用户ID/User ID

    try:
        # 获取指定用户的信息/Get information of specified user
        api_response = api_instance.get_user_info_api_v1_toutiao_app_get_user_info_get(user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ToutiaoAppAPIApi->get_user_info_api_v1_toutiao_app_get_user_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| 用户ID/User ID | 

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

# **get_user_info_api_v1_toutiao_app_get_user_info_get_0**
> ResponseModel get_user_info_api_v1_toutiao_app_get_user_info_get_0(user_id)

获取指定用户的信息/Get information of specified user

# [中文] ### 用途: - 获取指定用户的信息 ### 参数: - user_id: 用户ID，可以从以下接口获取：     - `/api/v1/toutiao/app/get_user_id` ### 返回: - 用户信息  # [English] ### Purpose: - Get information of specified user ### Parameters: - user_id: User ID, can be obtained from the following API:     - `/api/v1/toutiao/app/get_user_id` ### Return: - User information  # [示例/Example] user_id = \"1352838578180211\"

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
    api_instance = tikhub_sdk_v2.ToutiaoAppAPIApi(api_client)
    user_id = '1352838578180211' # str | 用户ID/User ID

    try:
        # 获取指定用户的信息/Get information of specified user
        api_response = api_instance.get_user_info_api_v1_toutiao_app_get_user_info_get_0(user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ToutiaoAppAPIApi->get_user_info_api_v1_toutiao_app_get_user_info_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| 用户ID/User ID | 

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

# **get_video_info_api_v1_toutiao_app_get_video_info_get**
> ResponseModel get_video_info_api_v1_toutiao_app_get_video_info_get(group_id)

获取指定视频的信息/Get information of specified video

# [中文] ### 用途: - 获取指定视频的信息 ### 参数: - group_id: 作品ID，可以从链接中获取     - 例如: https://www.toutiao.com/video/7431543350882206242/ ### 返回: - 作品信息  # [English] ### Purpose: - Get information of specified video ### Parameters: - group_id: Post ID, can be obtained from the link     - For example: https://www.toutiao.com/video/7431543350882206242/ ### Return: - Post information  # [示例/Example] group_id = \"7431543350882206242\"

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
    api_instance = tikhub_sdk_v2.ToutiaoAppAPIApi(api_client)
    group_id = '7431543350882206242' # str | 作品ID/Post ID

    try:
        # 获取指定视频的信息/Get information of specified video
        api_response = api_instance.get_video_info_api_v1_toutiao_app_get_video_info_get(group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ToutiaoAppAPIApi->get_video_info_api_v1_toutiao_app_get_video_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| 作品ID/Post ID | 

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

# **get_video_info_api_v1_toutiao_app_get_video_info_get_0**
> ResponseModel get_video_info_api_v1_toutiao_app_get_video_info_get_0(group_id)

获取指定视频的信息/Get information of specified video

# [中文] ### 用途: - 获取指定视频的信息 ### 参数: - group_id: 作品ID，可以从链接中获取     - 例如: https://www.toutiao.com/video/7431543350882206242/ ### 返回: - 作品信息  # [English] ### Purpose: - Get information of specified video ### Parameters: - group_id: Post ID, can be obtained from the link     - For example: https://www.toutiao.com/video/7431543350882206242/ ### Return: - Post information  # [示例/Example] group_id = \"7431543350882206242\"

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
    api_instance = tikhub_sdk_v2.ToutiaoAppAPIApi(api_client)
    group_id = '7431543350882206242' # str | 作品ID/Post ID

    try:
        # 获取指定视频的信息/Get information of specified video
        api_response = api_instance.get_video_info_api_v1_toutiao_app_get_video_info_get_0(group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ToutiaoAppAPIApi->get_video_info_api_v1_toutiao_app_get_video_info_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| 作品ID/Post ID | 

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

