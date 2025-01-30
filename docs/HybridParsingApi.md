# tikhub_sdk_v2.HybridParsingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hybrid_parsing_single_video_api_v1_hybrid_video_data_get**](HybridParsingApi.md#hybrid_parsing_single_video_api_v1_hybrid_video_data_get) | **GET** /api/v1/hybrid/video_data | 混合解析单一视频接口/Hybrid parsing single video endpoint
[**hybrid_parsing_single_video_api_v1_hybrid_video_data_get_0**](HybridParsingApi.md#hybrid_parsing_single_video_api_v1_hybrid_video_data_get_0) | **GET** /api/v1/hybrid/video_data | 混合解析单一视频接口/Hybrid parsing single video endpoint
[**hybrid_parsing_single_video_api_v1_hybrid_video_data_get_1**](HybridParsingApi.md#hybrid_parsing_single_video_api_v1_hybrid_video_data_get_1) | **GET** /api/v1/hybrid/video_data | 混合解析单一视频接口/Hybrid parsing single video endpoint


# **hybrid_parsing_single_video_api_v1_hybrid_video_data_get**
> ResponseModel hybrid_parsing_single_video_api_v1_hybrid_video_data_get(url, minimal=minimal, base64_url=base64_url)

混合解析单一视频接口/Hybrid parsing single video endpoint

# [中文] ### 用途: - 该接口用于解析抖音/TikTok单一视频的数据。 ### 参数: - `url`: 视频链接、分享链接、分享文本。 ### 返回: - `data`: 视频数据。  # [English] ### Purpose: - This endpoint is used to parse data of a single Douyin/TikTok video. ### Parameters: - `url`: Video link, share link, or share text. ### Returns: - `data`: Video data.  # [Example] url = \"https://v.douyin.com/L4FJNR3/\"

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
    api_instance = tikhub_sdk_v2.HybridParsingApi(api_client)
    url = 'https://v.douyin.com/L4FJNR3/' # str | 
minimal = False # bool | 是否返回最小数据/Whether to return minimal data (optional) (default to False)
base64_url = False # bool | 是否Base64编码提交URL/Base64 encoding URL (optional) (default to False)

    try:
        # 混合解析单一视频接口/Hybrid parsing single video endpoint
        api_response = api_instance.hybrid_parsing_single_video_api_v1_hybrid_video_data_get(url, minimal=minimal, base64_url=base64_url)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HybridParsingApi->hybrid_parsing_single_video_api_v1_hybrid_video_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**|  | 
 **minimal** | **bool**| 是否返回最小数据/Whether to return minimal data | [optional] [default to False]
 **base64_url** | **bool**| 是否Base64编码提交URL/Base64 encoding URL | [optional] [default to False]

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

# **hybrid_parsing_single_video_api_v1_hybrid_video_data_get_0**
> ResponseModel hybrid_parsing_single_video_api_v1_hybrid_video_data_get_0(url, minimal=minimal, base64_url=base64_url)

混合解析单一视频接口/Hybrid parsing single video endpoint

# [中文] ### 用途: - 该接口用于解析抖音/TikTok单一视频的数据。 ### 参数: - `url`: 视频链接、分享链接、分享文本。 ### 返回: - `data`: 视频数据。  # [English] ### Purpose: - This endpoint is used to parse data of a single Douyin/TikTok video. ### Parameters: - `url`: Video link, share link, or share text. ### Returns: - `data`: Video data.  # [Example] url = \"https://v.douyin.com/L4FJNR3/\"

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
    api_instance = tikhub_sdk_v2.HybridParsingApi(api_client)
    url = 'https://v.douyin.com/L4FJNR3/' # str | 
minimal = False # bool | 是否返回最小数据/Whether to return minimal data (optional) (default to False)
base64_url = False # bool | 是否Base64编码提交URL/Base64 encoding URL (optional) (default to False)

    try:
        # 混合解析单一视频接口/Hybrid parsing single video endpoint
        api_response = api_instance.hybrid_parsing_single_video_api_v1_hybrid_video_data_get_0(url, minimal=minimal, base64_url=base64_url)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HybridParsingApi->hybrid_parsing_single_video_api_v1_hybrid_video_data_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**|  | 
 **minimal** | **bool**| 是否返回最小数据/Whether to return minimal data | [optional] [default to False]
 **base64_url** | **bool**| 是否Base64编码提交URL/Base64 encoding URL | [optional] [default to False]

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

# **hybrid_parsing_single_video_api_v1_hybrid_video_data_get_1**
> ResponseModel hybrid_parsing_single_video_api_v1_hybrid_video_data_get_1(url, minimal=minimal, base64_url=base64_url)

混合解析单一视频接口/Hybrid parsing single video endpoint

# [中文] ### 用途: - 该接口用于解析抖音/TikTok单一视频的数据。 ### 参数: - `url`: 视频链接、分享链接、分享文本。 ### 返回: - `data`: 视频数据。  # [English] ### Purpose: - This endpoint is used to parse data of a single Douyin/TikTok video. ### Parameters: - `url`: Video link, share link, or share text. ### Returns: - `data`: Video data.  # [Example] url = \"https://v.douyin.com/L4FJNR3/\"

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
    api_instance = tikhub_sdk_v2.HybridParsingApi(api_client)
    url = 'https://v.douyin.com/L4FJNR3/' # str | 
minimal = False # bool | 是否返回最小数据/Whether to return minimal data (optional) (default to False)
base64_url = False # bool | 是否Base64编码提交URL/Base64 encoding URL (optional) (default to False)

    try:
        # 混合解析单一视频接口/Hybrid parsing single video endpoint
        api_response = api_instance.hybrid_parsing_single_video_api_v1_hybrid_video_data_get_1(url, minimal=minimal, base64_url=base64_url)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HybridParsingApi->hybrid_parsing_single_video_api_v1_hybrid_video_data_get_1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**|  | 
 **minimal** | **bool**| 是否返回最小数据/Whether to return minimal data | [optional] [default to False]
 **base64_url** | **bool**| 是否Base64编码提交URL/Base64 encoding URL | [optional] [default to False]

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

