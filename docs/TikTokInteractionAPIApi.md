# tikhub_sdk_v2.TikTokInteractionAPIApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_for_scope_api_v1_tiktok_interaction_apply_get**](TikTokInteractionAPIApi.md#apply_for_scope_api_v1_tiktok_interaction_apply_get) | **GET** /api/v1/tiktok/interaction/apply | 申请使用TikTok交互API权限（Scope）/Apply for TikTok Interaction API permission (Scope)
[**apply_for_scope_api_v1_tiktok_interaction_apply_get_0**](TikTokInteractionAPIApi.md#apply_for_scope_api_v1_tiktok_interaction_apply_get_0) | **GET** /api/v1/tiktok/interaction/apply | 申请使用TikTok交互API权限（Scope）/Apply for TikTok Interaction API permission (Scope)
[**collect_api_v1_tiktok_interaction_collect_post**](TikTokInteractionAPIApi.md#collect_api_v1_tiktok_interaction_collect_post) | **POST** /api/v1/tiktok/interaction/collect | 收藏/Collect
[**collect_api_v1_tiktok_interaction_collect_post_0**](TikTokInteractionAPIApi.md#collect_api_v1_tiktok_interaction_collect_post_0) | **POST** /api/v1/tiktok/interaction/collect | 收藏/Collect
[**follow_api_v1_tiktok_interaction_follow_post**](TikTokInteractionAPIApi.md#follow_api_v1_tiktok_interaction_follow_post) | **POST** /api/v1/tiktok/interaction/follow | 关注/Follow
[**follow_api_v1_tiktok_interaction_follow_post_0**](TikTokInteractionAPIApi.md#follow_api_v1_tiktok_interaction_follow_post_0) | **POST** /api/v1/tiktok/interaction/follow | 关注/Follow
[**forward_api_v1_tiktok_interaction_forward_post**](TikTokInteractionAPIApi.md#forward_api_v1_tiktok_interaction_forward_post) | **POST** /api/v1/tiktok/interaction/forward | 转发/Forward
[**forward_api_v1_tiktok_interaction_forward_post_0**](TikTokInteractionAPIApi.md#forward_api_v1_tiktok_interaction_forward_post_0) | **POST** /api/v1/tiktok/interaction/forward | 转发/Forward
[**like_api_v1_tiktok_interaction_like_post**](TikTokInteractionAPIApi.md#like_api_v1_tiktok_interaction_like_post) | **POST** /api/v1/tiktok/interaction/like | 点赞/Like
[**like_api_v1_tiktok_interaction_like_post_0**](TikTokInteractionAPIApi.md#like_api_v1_tiktok_interaction_like_post_0) | **POST** /api/v1/tiktok/interaction/like | 点赞/Like
[**post_comment_api_v1_tiktok_interaction_post_comment_post**](TikTokInteractionAPIApi.md#post_comment_api_v1_tiktok_interaction_post_comment_post) | **POST** /api/v1/tiktok/interaction/post_comment | 发送评论/Post comment
[**post_comment_api_v1_tiktok_interaction_post_comment_post_0**](TikTokInteractionAPIApi.md#post_comment_api_v1_tiktok_interaction_post_comment_post_0) | **POST** /api/v1/tiktok/interaction/post_comment | 发送评论/Post comment
[**reply_comment_api_v1_tiktok_interaction_reply_comment_post**](TikTokInteractionAPIApi.md#reply_comment_api_v1_tiktok_interaction_reply_comment_post) | **POST** /api/v1/tiktok/interaction/reply_comment | 回复评论/Reply to comment
[**reply_comment_api_v1_tiktok_interaction_reply_comment_post_0**](TikTokInteractionAPIApi.md#reply_comment_api_v1_tiktok_interaction_reply_comment_post_0) | **POST** /api/v1/tiktok/interaction/reply_comment | 回复评论/Reply to comment


# **apply_for_scope_api_v1_tiktok_interaction_apply_get**
> ResponseModel apply_for_scope_api_v1_tiktok_interaction_apply_get(api_key, invite_code)

申请使用TikTok交互API权限（Scope）/Apply for TikTok Interaction API permission (Scope)

# [通知] - 此接口已经废弃，用户现在无需手动申请调用权限，只需要在用户后台更新API Key的对应权限即可，即API Key对应的的Scope。 # [中文] ### 接口用途: - 申请使用TikTok交互API的接口权限（Scope），请在使用交互类接口之前申请，否则将无法正常请求。 ### 申请流程: - 申请接口权限需要邀请码，如果你没有邀请码，可以在Discord服务器中联系管理员获取。 - Discord服务器链接: [TikHub Discord](https://discord.gg/aMEAS8Xsvz) ### 申请须知: - 此权限仅限于当前提交的API Key，不可跨API Key使用。 - 用户需要使用美国地区注册且有效的的TikTok账号进行登录，否则保证将无法正常请求。 - 用户需要使用美国地区的代理IP进行获取Cookie，否则将保证无法正常请求。 - 用户需要使用美国地区的代理IP进行请求，否则将无法保证正常请求。 ### 用户守则以及责任: - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。 - 请不要将接口权限分享给他人，否则我们将会停止对你的服务。 - 接口请求目前暂时定为每秒5次请求。 ### 返回: - 申请结果以及申请的邀请码，请自行保留邀请码，以便后续使用。  # [Notice] - This interface has been deprecated, users no longer need to apply for permission to call the API, just update the corresponding permission of the API Key in the user background, that is, the Scope corresponding to the API Key. # [English] ### Purpose: - Apply for the interface permission (Scope) of TikTok Interaction API, please apply before using the interactive interface, otherwise the request will not be made normally. ### Application process: - Applying for interface permissions requires an invitation code, if you do not have an invitation code, you can contact the administrator on the Discord server. - Discord server link: [TikHub Discord](https://discord.gg/aMEAS8Xsvz) ### Application notes: - This permission is limited to the API Key submitted, and cannot be used across API Keys. - Users need to log in with a registered and valid TikTok account in the United States, otherwise the request will not be made normally. - Users need to use a proxy IP in the United States to obtain cookies, otherwise the request will not be made normally. - Users need to use a proxy IP in the United States for requests, otherwise the request will not be made normally. ### User guidelines and responsibilities: - Please do not use interactive interfaces to harass others, or engage in illegal or irregular operations, otherwise we will stop providing services to you, and all responsibilities will be borne by you. - Please do not share the interface permission with others, otherwise we will stop providing services to you. - The interface request is currently set to 5 requests per second. ### Return: - Application results and the invitation code applied for, please keep the invitation code for subsequent use.  # [示例/Example] ```python # Python Code invite_code = \"Your_Invite_Code\" ```

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
    api_instance = tikhub_sdk_v2.TikTokInteractionAPIApi(api_client)
    api_key = 'api_key_example' # str | 
invite_code = 'invite_code_example' # str | 

    try:
        # 申请使用TikTok交互API权限（Scope）/Apply for TikTok Interaction API permission (Scope)
        api_response = api_instance.apply_for_scope_api_v1_tiktok_interaction_apply_get(api_key, invite_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TikTokInteractionAPIApi->apply_for_scope_api_v1_tiktok_interaction_apply_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **invite_code** | **str**|  | 

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

# **apply_for_scope_api_v1_tiktok_interaction_apply_get_0**
> ResponseModel apply_for_scope_api_v1_tiktok_interaction_apply_get_0(api_key, invite_code)

申请使用TikTok交互API权限（Scope）/Apply for TikTok Interaction API permission (Scope)

# [通知] - 此接口已经废弃，用户现在无需手动申请调用权限，只需要在用户后台更新API Key的对应权限即可，即API Key对应的的Scope。 # [中文] ### 接口用途: - 申请使用TikTok交互API的接口权限（Scope），请在使用交互类接口之前申请，否则将无法正常请求。 ### 申请流程: - 申请接口权限需要邀请码，如果你没有邀请码，可以在Discord服务器中联系管理员获取。 - Discord服务器链接: [TikHub Discord](https://discord.gg/aMEAS8Xsvz) ### 申请须知: - 此权限仅限于当前提交的API Key，不可跨API Key使用。 - 用户需要使用美国地区注册且有效的的TikTok账号进行登录，否则保证将无法正常请求。 - 用户需要使用美国地区的代理IP进行获取Cookie，否则将保证无法正常请求。 - 用户需要使用美国地区的代理IP进行请求，否则将无法保证正常请求。 ### 用户守则以及责任: - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。 - 请不要将接口权限分享给他人，否则我们将会停止对你的服务。 - 接口请求目前暂时定为每秒5次请求。 ### 返回: - 申请结果以及申请的邀请码，请自行保留邀请码，以便后续使用。  # [Notice] - This interface has been deprecated, users no longer need to apply for permission to call the API, just update the corresponding permission of the API Key in the user background, that is, the Scope corresponding to the API Key. # [English] ### Purpose: - Apply for the interface permission (Scope) of TikTok Interaction API, please apply before using the interactive interface, otherwise the request will not be made normally. ### Application process: - Applying for interface permissions requires an invitation code, if you do not have an invitation code, you can contact the administrator on the Discord server. - Discord server link: [TikHub Discord](https://discord.gg/aMEAS8Xsvz) ### Application notes: - This permission is limited to the API Key submitted, and cannot be used across API Keys. - Users need to log in with a registered and valid TikTok account in the United States, otherwise the request will not be made normally. - Users need to use a proxy IP in the United States to obtain cookies, otherwise the request will not be made normally. - Users need to use a proxy IP in the United States for requests, otherwise the request will not be made normally. ### User guidelines and responsibilities: - Please do not use interactive interfaces to harass others, or engage in illegal or irregular operations, otherwise we will stop providing services to you, and all responsibilities will be borne by you. - Please do not share the interface permission with others, otherwise we will stop providing services to you. - The interface request is currently set to 5 requests per second. ### Return: - Application results and the invitation code applied for, please keep the invitation code for subsequent use.  # [示例/Example] ```python # Python Code invite_code = \"Your_Invite_Code\" ```

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
    api_instance = tikhub_sdk_v2.TikTokInteractionAPIApi(api_client)
    api_key = 'api_key_example' # str | 
invite_code = 'invite_code_example' # str | 

    try:
        # 申请使用TikTok交互API权限（Scope）/Apply for TikTok Interaction API permission (Scope)
        api_response = api_instance.apply_for_scope_api_v1_tiktok_interaction_apply_get_0(api_key, invite_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TikTokInteractionAPIApi->apply_for_scope_api_v1_tiktok_interaction_apply_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **invite_code** | **str**|  | 

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

# **collect_api_v1_tiktok_interaction_collect_post**
> ResponseModel collect_api_v1_tiktok_interaction_collect_post(collect_request=collect_request)

收藏/Collect

# [中文] ### 用途: - 使用用户Cookie收藏指定视频，当前请尽可能使用美国地区的TikTok账号，并且在获取Cookie时请使用美国地区的代理IP。 ### 注意: - 交互类接口都需要使用用户的Cookie，因此请确保你的Cookie是有效的，否则将无法正常请求。 - 交互类的接口可能会导致账号异常或封禁，因此请谨慎使用，建议使用代理IP进行请求。 - 交互类接口的最终结果可能会受到TikTok风控系统的影响，大多数情况跟你所使用的账号有关，比如新注册的账号可能无法关注用户或点赞视频，我们无法处理基于账号的风控问题。 - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。 ### 参数: - aweme_id: 视频id，可以从分享链接中获取，例如：https://www.tiktok.com/@username/video/7419966340443819295 - cookie: 用户Cookie，可以从浏览器中登录自己的TikTok账号，然后复制Cookie信息，提交时请使用URL编码Cookie字符串。 - device_id: 设备id，可选，如果不填写则会自动生成，如果需要自定义设备id，请使用设备信息接口获取设备id。 - iid: 设备安装id，可选，如果不填写则会自动生成，如果需要自定义设备iid，请使用设备信息接口获取设备iid。 - proxy: 代理IP，可选，如果不填写则会使用服务器IP进行请求（不推荐），建议使用代理IP进行请求防止账号异常获被封禁，支持格式如下：     - 代理IP:端口     - 用户名:密码@代理IP:端口 ### 返回: - 点赞结果以及评论数据和设备信息，请自行保留设备信息，如请求时使用的`device_id`以及`iid`，以便后续调用接口时使用，频繁更换设备信息可能会导致账号异常或封禁。  # [English] ### Purpose: - Collect a specified video using user cookies, please try to use TikTok accounts in the United States as much as possible, and use proxy IPs in the United States when obtaining cookies. ### Note: - Interactive interfaces all need to use the user's Cookie, so please make sure that your Cookie is valid, otherwise the request will not be made normally. - Interactive interfaces may cause account exceptions or bans, so please use them with caution, and it is recommended to use proxy IPs for requests. - The final result of the interactive interface may be affected by the TikTok risk control system, and in most cases it is related to the account you are using, for example, a newly registered account may not be able to follow users or like videos, and we cannot handle risk control issues based on accounts. - Please do not use interactive interfaces to harass others, or engage in illegal or irregular operations, otherwise we will stop providing services to you, and all responsibilities will be borne by you. ### Parameters: - aweme_id: Video id, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/7419966340443819295 - cookie: User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-encoded Cookie string when submitting. - device_id: Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, please use the device information interface to get the device id. - iid: Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device iid, please use the device information interface to get the device iid. - proxy: Proxy IP, optional, if not filled in, the server IP will be used for the request (not recommended), it is recommended to use a proxy IP for the request to prevent account exceptions or bans, support the following formats:     - Proxy IP:Port     - Username:Password@Proxy IP:Port ### Return: - Like results, comment data and device information, please keep the device information, such as the `device_id` and `iid` used when requesting, for subsequent calls to the interface, frequent replacement of device information may cause account exceptions or bans.  # [示例/Example] ```python # Python Code cookie = urllib.parse.quote(\"Your_Cookie_From_Browser\") payload = {     \"aweme_id\": \"7419966340443819295\",     \"cookie\": cookie,     \"proxy\": \"\", } ```

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
    api_instance = tikhub_sdk_v2.TikTokInteractionAPIApi(api_client)
    collect_request = tikhub_sdk_v2.CollectRequest() # CollectRequest |  (optional)

    try:
        # 收藏/Collect
        api_response = api_instance.collect_api_v1_tiktok_interaction_collect_post(collect_request=collect_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TikTokInteractionAPIApi->collect_api_v1_tiktok_interaction_collect_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collect_request** | [**CollectRequest**](CollectRequest.md)|  | [optional] 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collect_api_v1_tiktok_interaction_collect_post_0**
> ResponseModel collect_api_v1_tiktok_interaction_collect_post_0(collect_request=collect_request)

收藏/Collect

# [中文] ### 用途: - 使用用户Cookie收藏指定视频，当前请尽可能使用美国地区的TikTok账号，并且在获取Cookie时请使用美国地区的代理IP。 ### 注意: - 交互类接口都需要使用用户的Cookie，因此请确保你的Cookie是有效的，否则将无法正常请求。 - 交互类的接口可能会导致账号异常或封禁，因此请谨慎使用，建议使用代理IP进行请求。 - 交互类接口的最终结果可能会受到TikTok风控系统的影响，大多数情况跟你所使用的账号有关，比如新注册的账号可能无法关注用户或点赞视频，我们无法处理基于账号的风控问题。 - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。 ### 参数: - aweme_id: 视频id，可以从分享链接中获取，例如：https://www.tiktok.com/@username/video/7419966340443819295 - cookie: 用户Cookie，可以从浏览器中登录自己的TikTok账号，然后复制Cookie信息，提交时请使用URL编码Cookie字符串。 - device_id: 设备id，可选，如果不填写则会自动生成，如果需要自定义设备id，请使用设备信息接口获取设备id。 - iid: 设备安装id，可选，如果不填写则会自动生成，如果需要自定义设备iid，请使用设备信息接口获取设备iid。 - proxy: 代理IP，可选，如果不填写则会使用服务器IP进行请求（不推荐），建议使用代理IP进行请求防止账号异常获被封禁，支持格式如下：     - 代理IP:端口     - 用户名:密码@代理IP:端口 ### 返回: - 点赞结果以及评论数据和设备信息，请自行保留设备信息，如请求时使用的`device_id`以及`iid`，以便后续调用接口时使用，频繁更换设备信息可能会导致账号异常或封禁。  # [English] ### Purpose: - Collect a specified video using user cookies, please try to use TikTok accounts in the United States as much as possible, and use proxy IPs in the United States when obtaining cookies. ### Note: - Interactive interfaces all need to use the user's Cookie, so please make sure that your Cookie is valid, otherwise the request will not be made normally. - Interactive interfaces may cause account exceptions or bans, so please use them with caution, and it is recommended to use proxy IPs for requests. - The final result of the interactive interface may be affected by the TikTok risk control system, and in most cases it is related to the account you are using, for example, a newly registered account may not be able to follow users or like videos, and we cannot handle risk control issues based on accounts. - Please do not use interactive interfaces to harass others, or engage in illegal or irregular operations, otherwise we will stop providing services to you, and all responsibilities will be borne by you. ### Parameters: - aweme_id: Video id, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/7419966340443819295 - cookie: User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-encoded Cookie string when submitting. - device_id: Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, please use the device information interface to get the device id. - iid: Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device iid, please use the device information interface to get the device iid. - proxy: Proxy IP, optional, if not filled in, the server IP will be used for the request (not recommended), it is recommended to use a proxy IP for the request to prevent account exceptions or bans, support the following formats:     - Proxy IP:Port     - Username:Password@Proxy IP:Port ### Return: - Like results, comment data and device information, please keep the device information, such as the `device_id` and `iid` used when requesting, for subsequent calls to the interface, frequent replacement of device information may cause account exceptions or bans.  # [示例/Example] ```python # Python Code cookie = urllib.parse.quote(\"Your_Cookie_From_Browser\") payload = {     \"aweme_id\": \"7419966340443819295\",     \"cookie\": cookie,     \"proxy\": \"\", } ```

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
    api_instance = tikhub_sdk_v2.TikTokInteractionAPIApi(api_client)
    collect_request = tikhub_sdk_v2.CollectRequest() # CollectRequest |  (optional)

    try:
        # 收藏/Collect
        api_response = api_instance.collect_api_v1_tiktok_interaction_collect_post_0(collect_request=collect_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TikTokInteractionAPIApi->collect_api_v1_tiktok_interaction_collect_post_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collect_request** | [**CollectRequest**](CollectRequest.md)|  | [optional] 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **follow_api_v1_tiktok_interaction_follow_post**
> ResponseModel follow_api_v1_tiktok_interaction_follow_post(follow_request=follow_request)

关注/Follow

# [中文] ### 用途: - 使用用户Cookie关注指定用户，当前请尽可能使用美国地区的TikTok账号，并且在获取Cookie时请使用美国地区的代理IP。 ### 注意: - 交互类接口都需要使用用户的Cookie，因此请确保你的Cookie是有效的，否则将无法正常请求。 - 交互类的接口可能会导致账号异常或封禁，因此请谨慎使用，建议使用代理IP进行请求。 - 交互类接口的最终结果可能会受到TikTok风控系统的影响，大多数情况跟你所使用的账号有关，比如新注册的账号可能无法关注用户或点赞视频，我们无法处理基于账号的风控问题。 - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。 ### 参数: - user_id: 用户id，可以从接口`/api/v1/tiktok/app/v3/handler_user_profile`获取。 - sec_user_id: 用户sec_id，可以从分接口`/api/v1/tiktok/web/get_sec_user_id`获取。 - cookie: 用户Cookie，可以从浏览器中登录自己的TikTok账号，然后复制Cookie信息，提交时请使用URL编码Cookie字符串。 - device_id: 设备id，可选，如果不填写则会自动生成，如果需要自定义设备id，请使用设备信息接口获取设备id。 - iid: 设备安装id，可选，如果不填写则会自动生成，如果需要自定义设备iid，请使用设备信息接口获取设备iid。 - proxy: 代理IP，可选，如果不填写则会使用服务器IP进行请求（不推荐），建议使用代理IP进行请求防止账号异常获被封禁，支持格式如下：     - 代理IP:端口     - 用户名:密码@代理IP:端口 ### 返回: - 关注结果以及评论数据和设备信息，请自行保留设备信息，如请求时使用的`device_id`以及`iid`，以便后续调用接口时使用，频繁更换设备信息可能会导致账号异常或封禁。  # [English] ### Purpose: - Follow a specified user using user cookies, please try to use TikTok accounts in the United States as much as possible, and use proxy IPs in the United States when obtaining cookies. ### Note: - Interactive interfaces all need to use the user's Cookie, so please make sure that your Cookie is valid, otherwise the request will not be made normally. - Interactive interfaces may cause account exceptions or bans, so please use them with caution, and it is recommended to use proxy IPs for requests. - The final result of the interactive interface may be affected by the TikTok risk control system, and in most cases it is related to the account you are using, for example, a newly registered account may not be able to follow users or like videos, and we cannot handle risk control issues based on accounts. - Please do not use interactive interfaces to harass others, or engage in illegal or irregular operations, otherwise we will stop providing services to you, and all responsibilities will be borne by you. ### Parameters: - user_id: User id, which can be obtained from the sub-interface `/api/v1/tiktok/app/v3/handler_user_profile`. - sec_user_id: User sec_id, which can be obtained from the sub-interface `/api/v1/tiktok/web/get_sec_user_id`. - cookie: User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-encoded Cookie string when submitting. - device_id: Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, please use the device information interface to get the device id. - iid: Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device iid, please use the device information interface to get the device iid. - proxy: Proxy IP, optional, if not filled in, the server IP will be used for the request (not recommended), it is recommended to use a proxy IP for the request to prevent account exceptions or bans, support the following formats:     - Proxy IP:Port     - Username:Password@Proxy IP:Port ### Return: - Follow results, comment data and device information, please keep the device information, such as the `device_id` and `iid` used when requesting, for subsequent calls to the interface, frequent replacement of device information may cause account exceptions or bans.  # [示例/Example] ```python # Python Code cookie = urllib.parse.quote(\"Your_Cookie_From_Browser\") payload = {     \"user_id\": \"6881290705605477381\",     \"sec_user_id\": \"MS4wLjABAAAAqB08cUbXaDWqbD6MCga2RbGTuhfO2EsHayBYx08NDrN7IE3jQuRDNNN6YwyfH6_6\",     \"cookie\": cookie,     \"proxy\": \"\", } ```

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
    api_instance = tikhub_sdk_v2.TikTokInteractionAPIApi(api_client)
    follow_request = tikhub_sdk_v2.FollowRequest() # FollowRequest |  (optional)

    try:
        # 关注/Follow
        api_response = api_instance.follow_api_v1_tiktok_interaction_follow_post(follow_request=follow_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TikTokInteractionAPIApi->follow_api_v1_tiktok_interaction_follow_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **follow_request** | [**FollowRequest**](FollowRequest.md)|  | [optional] 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **follow_api_v1_tiktok_interaction_follow_post_0**
> ResponseModel follow_api_v1_tiktok_interaction_follow_post_0(follow_request=follow_request)

关注/Follow

# [中文] ### 用途: - 使用用户Cookie关注指定用户，当前请尽可能使用美国地区的TikTok账号，并且在获取Cookie时请使用美国地区的代理IP。 ### 注意: - 交互类接口都需要使用用户的Cookie，因此请确保你的Cookie是有效的，否则将无法正常请求。 - 交互类的接口可能会导致账号异常或封禁，因此请谨慎使用，建议使用代理IP进行请求。 - 交互类接口的最终结果可能会受到TikTok风控系统的影响，大多数情况跟你所使用的账号有关，比如新注册的账号可能无法关注用户或点赞视频，我们无法处理基于账号的风控问题。 - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。 ### 参数: - user_id: 用户id，可以从接口`/api/v1/tiktok/app/v3/handler_user_profile`获取。 - sec_user_id: 用户sec_id，可以从分接口`/api/v1/tiktok/web/get_sec_user_id`获取。 - cookie: 用户Cookie，可以从浏览器中登录自己的TikTok账号，然后复制Cookie信息，提交时请使用URL编码Cookie字符串。 - device_id: 设备id，可选，如果不填写则会自动生成，如果需要自定义设备id，请使用设备信息接口获取设备id。 - iid: 设备安装id，可选，如果不填写则会自动生成，如果需要自定义设备iid，请使用设备信息接口获取设备iid。 - proxy: 代理IP，可选，如果不填写则会使用服务器IP进行请求（不推荐），建议使用代理IP进行请求防止账号异常获被封禁，支持格式如下：     - 代理IP:端口     - 用户名:密码@代理IP:端口 ### 返回: - 关注结果以及评论数据和设备信息，请自行保留设备信息，如请求时使用的`device_id`以及`iid`，以便后续调用接口时使用，频繁更换设备信息可能会导致账号异常或封禁。  # [English] ### Purpose: - Follow a specified user using user cookies, please try to use TikTok accounts in the United States as much as possible, and use proxy IPs in the United States when obtaining cookies. ### Note: - Interactive interfaces all need to use the user's Cookie, so please make sure that your Cookie is valid, otherwise the request will not be made normally. - Interactive interfaces may cause account exceptions or bans, so please use them with caution, and it is recommended to use proxy IPs for requests. - The final result of the interactive interface may be affected by the TikTok risk control system, and in most cases it is related to the account you are using, for example, a newly registered account may not be able to follow users or like videos, and we cannot handle risk control issues based on accounts. - Please do not use interactive interfaces to harass others, or engage in illegal or irregular operations, otherwise we will stop providing services to you, and all responsibilities will be borne by you. ### Parameters: - user_id: User id, which can be obtained from the sub-interface `/api/v1/tiktok/app/v3/handler_user_profile`. - sec_user_id: User sec_id, which can be obtained from the sub-interface `/api/v1/tiktok/web/get_sec_user_id`. - cookie: User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-encoded Cookie string when submitting. - device_id: Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, please use the device information interface to get the device id. - iid: Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device iid, please use the device information interface to get the device iid. - proxy: Proxy IP, optional, if not filled in, the server IP will be used for the request (not recommended), it is recommended to use a proxy IP for the request to prevent account exceptions or bans, support the following formats:     - Proxy IP:Port     - Username:Password@Proxy IP:Port ### Return: - Follow results, comment data and device information, please keep the device information, such as the `device_id` and `iid` used when requesting, for subsequent calls to the interface, frequent replacement of device information may cause account exceptions or bans.  # [示例/Example] ```python # Python Code cookie = urllib.parse.quote(\"Your_Cookie_From_Browser\") payload = {     \"user_id\": \"6881290705605477381\",     \"sec_user_id\": \"MS4wLjABAAAAqB08cUbXaDWqbD6MCga2RbGTuhfO2EsHayBYx08NDrN7IE3jQuRDNNN6YwyfH6_6\",     \"cookie\": cookie,     \"proxy\": \"\", } ```

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
    api_instance = tikhub_sdk_v2.TikTokInteractionAPIApi(api_client)
    follow_request = tikhub_sdk_v2.FollowRequest() # FollowRequest |  (optional)

    try:
        # 关注/Follow
        api_response = api_instance.follow_api_v1_tiktok_interaction_follow_post_0(follow_request=follow_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TikTokInteractionAPIApi->follow_api_v1_tiktok_interaction_follow_post_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **follow_request** | [**FollowRequest**](FollowRequest.md)|  | [optional] 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forward_api_v1_tiktok_interaction_forward_post**
> ResponseModel forward_api_v1_tiktok_interaction_forward_post(forward_request=forward_request)

转发/Forward

# [中文] ### 用途: - 使用用户Cookie转发指定作品，当前请尽可能使用美国地区的TikTok账号，并且在获取Cookie时请使用美国地区的代理IP。 ### 注意: - 交互类接口都需要使用用户的Cookie，因此请确保你的Cookie是有效的，否则将无法正常请求。 - 交互类的接口可能会导致账号异常或封禁，因此请谨慎使用，建议使用代理IP进行请求。 - 交互类接口的最终结果可能会受到TikTok风控系统的影响，大多数情况跟你所使用的账号有关，比如新注册的账号可能无法关注用户或点赞视频，我们无法处理基于账号的风控问题。 - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。 ### 参数: - aweme_id: 视频id，可以从分享链接中获取，例如：https://www.tiktok.com/@username/video/7419966340443819295 - cookie: 用户Cookie，可以从浏览器中登录自己的TikTok账号，然后复制Cookie信息，提交时请使用URL编码Cookie字符串。 - device_id: 设备id，可选，如果不填写则会自动生成，如果需要自定义设备id，请使用设备信息接口获取设备id。 - iid: 设备安装id，可选，如果不填写则会自动生成，如果需要自定义设备iid，请使用设备信息接口获取设备iid。 - proxy: 代理IP，可选，如果不填写则会使用服务器IP进行请求（不推荐），建议使用代理IP进行请求防止账号异常获被封禁，支持格式如下：     - 代理IP:端口     - 用户名:密码@代理IP:端口 ### 返回: - 关注结果以及评论数据和设备信息，请自行保留设备信息，如请求时使用的`device_id`以及`iid`，以便后续调用接口时使用，频繁更换设备信息可能会导致账号异常或封禁。  # [English] ### Purpose: - Forward a specified post using user cookies, please try to use TikTok accounts in the United States as much as possible, and use proxy IPs in the United States when obtaining cookies. ### Note: - Interactive interfaces all need to use the user's Cookie, so please make sure that your Cookie is valid, otherwise the request will not be made normally. - Interactive interfaces may cause account exceptions or bans, so please use them with caution, and it is recommended to use proxy IPs for requests. - The final result of the interactive interface may be affected by the TikTok risk control system, and in most cases it is related to the account you are using, for example, a newly registered account may not be able to follow users or like videos, and we cannot handle risk control issues based on accounts. - Please do not use interactive interfaces to harass others, or engage in illegal or irregular operations, otherwise we will stop providing services to you, and all responsibilities will be borne by you. ### Parameters: - aweme_id: Video id, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/7419966340443819295 - sec_user_id: User sec_id, which can be obtained from the sub-interface `/api/v1/tiktok/web/get_sec_user_id`. - cookie: User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-encoded Cookie string when submitting. - device_id: Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, please use the device information interface to get the device id. - iid: Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device iid, please use the device information interface to get the device iid. - proxy: Proxy IP, optional, if not filled in, the server IP will be used for the request (not recommended), it is recommended to use a proxy IP for the request to prevent account exceptions or bans, support the following formats:     - Proxy IP:Port     - Username:Password@Proxy IP:Port ### Return: - Follow results, comment data and device information, please keep the device information, such as the `device_id` and `iid` used when requesting, for subsequent calls to the interface, frequent replacement of device information may cause account exceptions or bans.  # [示例/Example] ```python # Python Code cookie = urllib.parse.quote(\"Your_Cookie_From_Browser\") payload = {     \"user_id\": \"6881290705605477381\",     \"sec_user_id\": \"MS4wLjABAAAAqB08cUbXaDWqbD6MCga2RbGTuhfO2EsHayBYx08NDrN7IE3jQuRDNNN6YwyfH6_6\",     \"cookie\": cookie,     \"proxy\": \"\", } ```

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
    api_instance = tikhub_sdk_v2.TikTokInteractionAPIApi(api_client)
    forward_request = tikhub_sdk_v2.ForwardRequest() # ForwardRequest |  (optional)

    try:
        # 转发/Forward
        api_response = api_instance.forward_api_v1_tiktok_interaction_forward_post(forward_request=forward_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TikTokInteractionAPIApi->forward_api_v1_tiktok_interaction_forward_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forward_request** | [**ForwardRequest**](ForwardRequest.md)|  | [optional] 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forward_api_v1_tiktok_interaction_forward_post_0**
> ResponseModel forward_api_v1_tiktok_interaction_forward_post_0(forward_request=forward_request)

转发/Forward

# [中文] ### 用途: - 使用用户Cookie转发指定作品，当前请尽可能使用美国地区的TikTok账号，并且在获取Cookie时请使用美国地区的代理IP。 ### 注意: - 交互类接口都需要使用用户的Cookie，因此请确保你的Cookie是有效的，否则将无法正常请求。 - 交互类的接口可能会导致账号异常或封禁，因此请谨慎使用，建议使用代理IP进行请求。 - 交互类接口的最终结果可能会受到TikTok风控系统的影响，大多数情况跟你所使用的账号有关，比如新注册的账号可能无法关注用户或点赞视频，我们无法处理基于账号的风控问题。 - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。 ### 参数: - aweme_id: 视频id，可以从分享链接中获取，例如：https://www.tiktok.com/@username/video/7419966340443819295 - cookie: 用户Cookie，可以从浏览器中登录自己的TikTok账号，然后复制Cookie信息，提交时请使用URL编码Cookie字符串。 - device_id: 设备id，可选，如果不填写则会自动生成，如果需要自定义设备id，请使用设备信息接口获取设备id。 - iid: 设备安装id，可选，如果不填写则会自动生成，如果需要自定义设备iid，请使用设备信息接口获取设备iid。 - proxy: 代理IP，可选，如果不填写则会使用服务器IP进行请求（不推荐），建议使用代理IP进行请求防止账号异常获被封禁，支持格式如下：     - 代理IP:端口     - 用户名:密码@代理IP:端口 ### 返回: - 关注结果以及评论数据和设备信息，请自行保留设备信息，如请求时使用的`device_id`以及`iid`，以便后续调用接口时使用，频繁更换设备信息可能会导致账号异常或封禁。  # [English] ### Purpose: - Forward a specified post using user cookies, please try to use TikTok accounts in the United States as much as possible, and use proxy IPs in the United States when obtaining cookies. ### Note: - Interactive interfaces all need to use the user's Cookie, so please make sure that your Cookie is valid, otherwise the request will not be made normally. - Interactive interfaces may cause account exceptions or bans, so please use them with caution, and it is recommended to use proxy IPs for requests. - The final result of the interactive interface may be affected by the TikTok risk control system, and in most cases it is related to the account you are using, for example, a newly registered account may not be able to follow users or like videos, and we cannot handle risk control issues based on accounts. - Please do not use interactive interfaces to harass others, or engage in illegal or irregular operations, otherwise we will stop providing services to you, and all responsibilities will be borne by you. ### Parameters: - aweme_id: Video id, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/7419966340443819295 - sec_user_id: User sec_id, which can be obtained from the sub-interface `/api/v1/tiktok/web/get_sec_user_id`. - cookie: User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-encoded Cookie string when submitting. - device_id: Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, please use the device information interface to get the device id. - iid: Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device iid, please use the device information interface to get the device iid. - proxy: Proxy IP, optional, if not filled in, the server IP will be used for the request (not recommended), it is recommended to use a proxy IP for the request to prevent account exceptions or bans, support the following formats:     - Proxy IP:Port     - Username:Password@Proxy IP:Port ### Return: - Follow results, comment data and device information, please keep the device information, such as the `device_id` and `iid` used when requesting, for subsequent calls to the interface, frequent replacement of device information may cause account exceptions or bans.  # [示例/Example] ```python # Python Code cookie = urllib.parse.quote(\"Your_Cookie_From_Browser\") payload = {     \"user_id\": \"6881290705605477381\",     \"sec_user_id\": \"MS4wLjABAAAAqB08cUbXaDWqbD6MCga2RbGTuhfO2EsHayBYx08NDrN7IE3jQuRDNNN6YwyfH6_6\",     \"cookie\": cookie,     \"proxy\": \"\", } ```

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
    api_instance = tikhub_sdk_v2.TikTokInteractionAPIApi(api_client)
    forward_request = tikhub_sdk_v2.ForwardRequest() # ForwardRequest |  (optional)

    try:
        # 转发/Forward
        api_response = api_instance.forward_api_v1_tiktok_interaction_forward_post_0(forward_request=forward_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TikTokInteractionAPIApi->forward_api_v1_tiktok_interaction_forward_post_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forward_request** | [**ForwardRequest**](ForwardRequest.md)|  | [optional] 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **like_api_v1_tiktok_interaction_like_post**
> ResponseModel like_api_v1_tiktok_interaction_like_post(like_request=like_request)

点赞/Like

# [中文] ### 用途: - 使用用户Cookie点赞指定视频，当前请尽可能使用美国地区的TikTok账号，并且在获取Cookie时请使用美国地区的代理IP。 ### 注意: - 交互类接口都需要使用用户的Cookie，因此请确保你的Cookie是有效的，否则将无法正常请求。 - 交互类的接口可能会导致账号异常或封禁，因此请谨慎使用，建议使用代理IP进行请求。 - 交互类接口的最终结果可能会受到TikTok风控系统的影响，大多数情况跟你所使用的账号有关，比如新注册的账号可能无法关注用户或点赞视频，我们无法处理基于账号的风控问题。 - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。 ### 参数: - aweme_id: 视频id，可以从分享链接中获取，例如：https://www.tiktok.com/@username/video/7419966340443819295 - cookie: 用户Cookie，可以从浏览器中登录自己的TikTok账号，然后复制Cookie信息，提交时请使用URL编码Cookie字符串。 - device_id: 设备id，可选，如果不填写则会自动生成，如果需要自定义设备id，请使用设备信息接口获取设备id。 - iid: 设备安装id，可选，如果不填写则会自动生成，如果需要自定义设备iid，请使用设备信息接口获取设备iid。 - proxy: 代理IP，可选，如果不填写则会使用服务器IP进行请求（不推荐），建议使用代理IP进行请求防止账号异常获被封禁，支持格式如下：     - 代理IP:端口     - 用户名:密码@代理IP:端口 ### 返回: - 点赞结果以及评论数据和设备信息，请自行保留设备信息，如请求时使用的`device_id`以及`iid`，以便后续调用接口时使用，频繁更换设备信息可能会导致账号异常或封禁。  # [English] ### Purpose: - Like a specified video using user cookies, please try to use TikTok accounts in the United States as much as possible, and use proxy IPs in the United States when obtaining cookies. ### Note: - Interactive interfaces all need to use the user's Cookie, so please make sure that your Cookie is valid, otherwise the request will not be made normally. - Interactive interfaces may cause account exceptions or bans, so please use them with caution, and it is recommended to use proxy IPs for requests. - The final result of the interactive interface may be affected by the TikTok risk control system, and in most cases it is related to the account you are using, for example, a newly registered account may not be able to follow users or like videos, and we cannot handle risk control issues based on accounts. - Please do not use interactive interfaces to harass others, or engage in illegal or irregular operations, otherwise we will stop providing services to you, and all responsibilities will be borne by you. ### Parameters: - aweme_id: Video id, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/7419966340443819295 - cookie: User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-encoded Cookie string when submitting. - device_id: Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, please use the device information interface to get the device id. - iid: Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device iid, please use the device information interface to get the device iid. - proxy: Proxy IP, optional, if not filled in, the server IP will be used for the request (not recommended), it is recommended to use a proxy IP for the request to prevent account exceptions or bans, support the following formats:     - Proxy IP:Port     - Username:Password@Proxy IP:Port ### Return: - Like results, comment data and device information, please keep the device information, such as the `device_id` and `iid` used when requesting, for subsequent calls to the interface, frequent replacement of device information may cause account exceptions or bans.  # [示例/Example] ```python # Python Code cookie = urllib.parse.quote(\"Your_Cookie_From_Browser\") payload = {     \"aweme_id\": \"7419966340443819295\",     \"cookie\": cookie,     \"proxy\": \"\", } ```

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
    api_instance = tikhub_sdk_v2.TikTokInteractionAPIApi(api_client)
    like_request = tikhub_sdk_v2.LikeRequest() # LikeRequest |  (optional)

    try:
        # 点赞/Like
        api_response = api_instance.like_api_v1_tiktok_interaction_like_post(like_request=like_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TikTokInteractionAPIApi->like_api_v1_tiktok_interaction_like_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **like_request** | [**LikeRequest**](LikeRequest.md)|  | [optional] 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **like_api_v1_tiktok_interaction_like_post_0**
> ResponseModel like_api_v1_tiktok_interaction_like_post_0(like_request=like_request)

点赞/Like

# [中文] ### 用途: - 使用用户Cookie点赞指定视频，当前请尽可能使用美国地区的TikTok账号，并且在获取Cookie时请使用美国地区的代理IP。 ### 注意: - 交互类接口都需要使用用户的Cookie，因此请确保你的Cookie是有效的，否则将无法正常请求。 - 交互类的接口可能会导致账号异常或封禁，因此请谨慎使用，建议使用代理IP进行请求。 - 交互类接口的最终结果可能会受到TikTok风控系统的影响，大多数情况跟你所使用的账号有关，比如新注册的账号可能无法关注用户或点赞视频，我们无法处理基于账号的风控问题。 - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。 ### 参数: - aweme_id: 视频id，可以从分享链接中获取，例如：https://www.tiktok.com/@username/video/7419966340443819295 - cookie: 用户Cookie，可以从浏览器中登录自己的TikTok账号，然后复制Cookie信息，提交时请使用URL编码Cookie字符串。 - device_id: 设备id，可选，如果不填写则会自动生成，如果需要自定义设备id，请使用设备信息接口获取设备id。 - iid: 设备安装id，可选，如果不填写则会自动生成，如果需要自定义设备iid，请使用设备信息接口获取设备iid。 - proxy: 代理IP，可选，如果不填写则会使用服务器IP进行请求（不推荐），建议使用代理IP进行请求防止账号异常获被封禁，支持格式如下：     - 代理IP:端口     - 用户名:密码@代理IP:端口 ### 返回: - 点赞结果以及评论数据和设备信息，请自行保留设备信息，如请求时使用的`device_id`以及`iid`，以便后续调用接口时使用，频繁更换设备信息可能会导致账号异常或封禁。  # [English] ### Purpose: - Like a specified video using user cookies, please try to use TikTok accounts in the United States as much as possible, and use proxy IPs in the United States when obtaining cookies. ### Note: - Interactive interfaces all need to use the user's Cookie, so please make sure that your Cookie is valid, otherwise the request will not be made normally. - Interactive interfaces may cause account exceptions or bans, so please use them with caution, and it is recommended to use proxy IPs for requests. - The final result of the interactive interface may be affected by the TikTok risk control system, and in most cases it is related to the account you are using, for example, a newly registered account may not be able to follow users or like videos, and we cannot handle risk control issues based on accounts. - Please do not use interactive interfaces to harass others, or engage in illegal or irregular operations, otherwise we will stop providing services to you, and all responsibilities will be borne by you. ### Parameters: - aweme_id: Video id, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/7419966340443819295 - cookie: User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-encoded Cookie string when submitting. - device_id: Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, please use the device information interface to get the device id. - iid: Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device iid, please use the device information interface to get the device iid. - proxy: Proxy IP, optional, if not filled in, the server IP will be used for the request (not recommended), it is recommended to use a proxy IP for the request to prevent account exceptions or bans, support the following formats:     - Proxy IP:Port     - Username:Password@Proxy IP:Port ### Return: - Like results, comment data and device information, please keep the device information, such as the `device_id` and `iid` used when requesting, for subsequent calls to the interface, frequent replacement of device information may cause account exceptions or bans.  # [示例/Example] ```python # Python Code cookie = urllib.parse.quote(\"Your_Cookie_From_Browser\") payload = {     \"aweme_id\": \"7419966340443819295\",     \"cookie\": cookie,     \"proxy\": \"\", } ```

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
    api_instance = tikhub_sdk_v2.TikTokInteractionAPIApi(api_client)
    like_request = tikhub_sdk_v2.LikeRequest() # LikeRequest |  (optional)

    try:
        # 点赞/Like
        api_response = api_instance.like_api_v1_tiktok_interaction_like_post_0(like_request=like_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TikTokInteractionAPIApi->like_api_v1_tiktok_interaction_like_post_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **like_request** | [**LikeRequest**](LikeRequest.md)|  | [optional] 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_comment_api_v1_tiktok_interaction_post_comment_post**
> ResponseModel post_comment_api_v1_tiktok_interaction_post_comment_post(post_comment_request=post_comment_request)

发送评论/Post comment

# [中文] ### 用途: - 使用用户Cookie发送评论到指定视频，当前请尽可能使用美国地区的TikTok账号，并且在获取Cookie时请使用美国地区的代理IP。 ### 注意: - 交互类接口都需要使用用户的Cookie，因此请确保你的Cookie是有效的，否则将无法正常请求。 - 交互类的接口可能会导致账号异常或封禁，因此请谨慎使用，建议使用代理IP进行请求。 - 交互类接口的最终结果可能会受到TikTok风控系统的影响，大多数情况跟你所使用的账号有关，比如新注册的账号可能无法关注用户或点赞视频，我们无法处理基于账号的风控问题。 - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。 ### 参数: - aweme_id: 视频id，可以从分享链接中获取，例如：https://www.tiktok.com/@username/video/7419966340443819295 - text: 评论内容，TikTok评论内容需要符合规范，不要带有违规的关键词，否则即使请求成功也会被系统判定为垃圾评论从而不被展示，提交时请使用URL编码评论字符串。 - cookie: 用户Cookie，可以从浏览器中登录自己的TikTok账号，然后复制Cookie信息，提交时请使用URL编码Cookie字符串。 - device_id: 设备id，可选，如果不填写则会自动生成，如果需要自定义设备id，请使用设备信息接口获取设备id。 - iid: 设备安装id，可选，如果不填写则会自动生成，如果需要自定义设备iid，请使用设备信息接口获取设备iid。 - proxy: 代理IP，可选，如果不填写则会使用服务器IP进行请求（不推荐），建议使用代理IP进行请求防止账号异常获被封禁，支持格式如下：     - 代理IP:端口     - 用户名:密码@代理IP:端口 ### 返回: - 发送评论结果以及评论数据和设备信息，请自行保留设备信息，如请求时使用的`device_id`以及`iid`，以便后续调用接口时使用，频繁更换设备信息可能会导致账号异常或封禁。  # [English] ### Purpose: - Post comments to the specified video using user cookies, please try to use TikTok accounts in the United States as much as possible, and use proxy IPs in the United States when obtaining cookies. ### Note: - Interactive interfaces all need to use the user's Cookie, so please make sure that your Cookie is valid, otherwise the request will not be made normally. - Interactive interfaces may cause account exceptions or bans, so please use them with caution, and it is recommended to use proxy IPs for requests. - The final result of the interactive interface may be affected by the TikTok risk control system, and in most cases it is related to the account you are using, for example, a newly registered account may not be able to follow users or like videos, and we cannot handle risk control issues based on accounts. - Please do not use interactive interfaces to harass others, or engage in illegal or irregular operations, otherwise we will stop providing services to you, and all responsibilities will be borne by you. ### Parameters: - aweme_id: Video id, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/7419966340443819295 - text: Comment content, TikTok comment content needs to comply with the specifications, do not contain illegal keywords, otherwise, even if the request is successful, it will be judged as spam comments by the system and will not be displayed, please use URL-encoded comment string when submitting. - cookie: User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-encoded Cookie string when submitting. - device_id: Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, please use the device information interface to get the device id. - iid: Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device iid, please use the device information interface to get the device iid. - proxy: Proxy IP, optional, if not filled in, the server IP will be used for the request (not recommended), it is recommended to use a proxy IP for the request to prevent account exceptions or bans, support the following formats:     - Proxy IP:Port     - Username:Password@Proxy IP:Port ### Return: - Post comment results, comment data and device information, please keep the device information, such as the `device_id` and `iid` used when requesting, for subsequent calls to the interface, frequent replacement of device information may cause account exceptions or bans.  # [示例/Example] ```python # Python Code text = urllib.parse.quote(\"Hello, TikTok!\") cookie = urllib.parse.quote(\"Your_Cookie_From_Browser\") payload = {     \"aweme_id\": \"7419966340443819295\",     \"text\": text,     \"cookie\": cookie,     \"proxy\": \"\", } ```

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
    api_instance = tikhub_sdk_v2.TikTokInteractionAPIApi(api_client)
    post_comment_request = tikhub_sdk_v2.PostCommentRequest() # PostCommentRequest |  (optional)

    try:
        # 发送评论/Post comment
        api_response = api_instance.post_comment_api_v1_tiktok_interaction_post_comment_post(post_comment_request=post_comment_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TikTokInteractionAPIApi->post_comment_api_v1_tiktok_interaction_post_comment_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_comment_request** | [**PostCommentRequest**](PostCommentRequest.md)|  | [optional] 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_comment_api_v1_tiktok_interaction_post_comment_post_0**
> ResponseModel post_comment_api_v1_tiktok_interaction_post_comment_post_0(post_comment_request=post_comment_request)

发送评论/Post comment

# [中文] ### 用途: - 使用用户Cookie发送评论到指定视频，当前请尽可能使用美国地区的TikTok账号，并且在获取Cookie时请使用美国地区的代理IP。 ### 注意: - 交互类接口都需要使用用户的Cookie，因此请确保你的Cookie是有效的，否则将无法正常请求。 - 交互类的接口可能会导致账号异常或封禁，因此请谨慎使用，建议使用代理IP进行请求。 - 交互类接口的最终结果可能会受到TikTok风控系统的影响，大多数情况跟你所使用的账号有关，比如新注册的账号可能无法关注用户或点赞视频，我们无法处理基于账号的风控问题。 - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。 ### 参数: - aweme_id: 视频id，可以从分享链接中获取，例如：https://www.tiktok.com/@username/video/7419966340443819295 - text: 评论内容，TikTok评论内容需要符合规范，不要带有违规的关键词，否则即使请求成功也会被系统判定为垃圾评论从而不被展示，提交时请使用URL编码评论字符串。 - cookie: 用户Cookie，可以从浏览器中登录自己的TikTok账号，然后复制Cookie信息，提交时请使用URL编码Cookie字符串。 - device_id: 设备id，可选，如果不填写则会自动生成，如果需要自定义设备id，请使用设备信息接口获取设备id。 - iid: 设备安装id，可选，如果不填写则会自动生成，如果需要自定义设备iid，请使用设备信息接口获取设备iid。 - proxy: 代理IP，可选，如果不填写则会使用服务器IP进行请求（不推荐），建议使用代理IP进行请求防止账号异常获被封禁，支持格式如下：     - 代理IP:端口     - 用户名:密码@代理IP:端口 ### 返回: - 发送评论结果以及评论数据和设备信息，请自行保留设备信息，如请求时使用的`device_id`以及`iid`，以便后续调用接口时使用，频繁更换设备信息可能会导致账号异常或封禁。  # [English] ### Purpose: - Post comments to the specified video using user cookies, please try to use TikTok accounts in the United States as much as possible, and use proxy IPs in the United States when obtaining cookies. ### Note: - Interactive interfaces all need to use the user's Cookie, so please make sure that your Cookie is valid, otherwise the request will not be made normally. - Interactive interfaces may cause account exceptions or bans, so please use them with caution, and it is recommended to use proxy IPs for requests. - The final result of the interactive interface may be affected by the TikTok risk control system, and in most cases it is related to the account you are using, for example, a newly registered account may not be able to follow users or like videos, and we cannot handle risk control issues based on accounts. - Please do not use interactive interfaces to harass others, or engage in illegal or irregular operations, otherwise we will stop providing services to you, and all responsibilities will be borne by you. ### Parameters: - aweme_id: Video id, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/7419966340443819295 - text: Comment content, TikTok comment content needs to comply with the specifications, do not contain illegal keywords, otherwise, even if the request is successful, it will be judged as spam comments by the system and will not be displayed, please use URL-encoded comment string when submitting. - cookie: User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-encoded Cookie string when submitting. - device_id: Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, please use the device information interface to get the device id. - iid: Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device iid, please use the device information interface to get the device iid. - proxy: Proxy IP, optional, if not filled in, the server IP will be used for the request (not recommended), it is recommended to use a proxy IP for the request to prevent account exceptions or bans, support the following formats:     - Proxy IP:Port     - Username:Password@Proxy IP:Port ### Return: - Post comment results, comment data and device information, please keep the device information, such as the `device_id` and `iid` used when requesting, for subsequent calls to the interface, frequent replacement of device information may cause account exceptions or bans.  # [示例/Example] ```python # Python Code text = urllib.parse.quote(\"Hello, TikTok!\") cookie = urllib.parse.quote(\"Your_Cookie_From_Browser\") payload = {     \"aweme_id\": \"7419966340443819295\",     \"text\": text,     \"cookie\": cookie,     \"proxy\": \"\", } ```

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
    api_instance = tikhub_sdk_v2.TikTokInteractionAPIApi(api_client)
    post_comment_request = tikhub_sdk_v2.PostCommentRequest() # PostCommentRequest |  (optional)

    try:
        # 发送评论/Post comment
        api_response = api_instance.post_comment_api_v1_tiktok_interaction_post_comment_post_0(post_comment_request=post_comment_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TikTokInteractionAPIApi->post_comment_api_v1_tiktok_interaction_post_comment_post_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_comment_request** | [**PostCommentRequest**](PostCommentRequest.md)|  | [optional] 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reply_comment_api_v1_tiktok_interaction_reply_comment_post**
> ResponseModel reply_comment_api_v1_tiktok_interaction_reply_comment_post(reply_comment_request=reply_comment_request)

回复评论/Reply to comment

# [中文] ### 用途: - 使用用户Cookie回复指定视频的一个评论，当前请尽可能使用美国地区的TikTok账号，并且在获取Cookie时请使用美国地区的代理IP。 ### 注意: - 交互类接口都需要使用用户的Cookie，因此请确保你的Cookie是有效的，否则将无法正常请求。 - 交互类的接口可能会导致账号异常或封禁，因此请谨慎使用，建议使用代理IP进行请求。 - 交互类接口的最终结果可能会受到TikTok风控系统的影响，大多数情况跟你所使用的账号有关，比如新注册的账号可能无法关注用户或点赞视频，我们无法处理基于账号的风控问题。 - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。 ### 参数: - aweme_id: 视频id，可以从分享链接中获取，例如：https://www.tiktok.com/@username/video/7419966340443819295 - reply_id: 要回复的目标评论ID，可以从指定视频的评论数据接口中获取，通常关键字为`cid`或`comment_id`或`reply_id`。 - text: 评论内容，TikTok评论内容需要符合规范，不要带有违规的关键词，否则即使请求成功也会被系统判定为垃圾评论从而不被展示，提交时请使用URL编码评论字符串。 - cookie: 用户Cookie，可以从浏览器中登录自己的TikTok账号，然后复制Cookie信息，提交时请使用URL编码Cookie字符串。 - device_id: 设备id，可选，如果不填写则会自动生成，如果需要自定义设备id，请使用设备信息接口获取设备id。 - iid: 设备安装id，可选，如果不填写则会自动生成，如果需要自定义设备iid，请使用设备信息接口获取设备iid。 - proxy: 代理IP，可选，如果不填写则会使用服务器IP进行请求（不推荐），建议使用代理IP进行请求防止账号异常获被封禁，支持格式如下：     - 代理IP:端口     - 用户名:密码@代理IP:端口 ### 返回: - 回复评论结果以及评论数据和设备信息，请自行保留设备信息，如请求时使用的`device_id`以及`iid`，以便后续调用接口时使用，频繁更换设备信息可能会导致账号异常或封禁。  # [English] ### Purpose: - Reply to a comment on a specified video using user cookies, please try to use TikTok accounts in the United States as much as possible, and use proxy IPs in the United States when obtaining cookies. ### Note: - Interactive interfaces all need to use the user's Cookie, so please make sure that your Cookie is valid, otherwise the request will not be made normally. - Interactive interfaces may cause account exceptions or bans, so please use them with caution, and it is recommended to use proxy IPs for requests. - The final result of the interactive interface may be affected by the TikTok risk control system, and in most cases it is related to the account you are using, for example, a newly registered account may not be able to follow users or like videos, and we cannot handle risk control issues based on accounts. - Please do not use interactive interfaces to harass others, or engage in illegal or irregular operations, otherwise we will stop providing services to you, and all responsibilities will be borne by you. ### Parameters: - aweme_id: Video id, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/7419966340443819295 - reply_id: The target comment ID to reply to, which can be obtained from the comment data interface of the specified video, usually the keyword is `cid` or `comment_id` or `reply_id`. - text: Comment content, TikTok comment content needs to comply with the specifications, do not contain illegal keywords, otherwise, even if the request is successful, it will be judged as spam comments by the system and will not be displayed, please use URL-encoded comment string when submitting. - cookie: User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-encoded Cookie string when submitting. - device_id: Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, please use the device information interface to get the device id. - iid: Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device iid, please use the device information interface to get the device iid. - proxy: Proxy IP, optional, if not filled in, the server IP will be used for the request (not recommended), it is recommended to use a proxy IP for the request to prevent account exceptions or bans, support the following formats:     - Proxy IP:Port     - Username:Password@Proxy IP:Port ### Return: - Reply comment results, comment data and device information, please keep the device information, such as the `device_id` and `iid` used when requesting, for subsequent calls to the interface, frequent replacement of device information may cause account exceptions or bans.  # [示例/Example] ```python # Python Code text = urllib.parse.quote(\"Hello, TikTok!\") cookie = urllib.parse.quote(\"Your_Cookie_From_Browser\") payload = {     \"aweme_id\": \"7419966340443819295\",     \"reply_id\": \"7420673787547419435\",     \"text\": text,     \"cookie\": cookie,     \"proxy\": \"\", } ```

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
    api_instance = tikhub_sdk_v2.TikTokInteractionAPIApi(api_client)
    reply_comment_request = tikhub_sdk_v2.ReplyCommentRequest() # ReplyCommentRequest |  (optional)

    try:
        # 回复评论/Reply to comment
        api_response = api_instance.reply_comment_api_v1_tiktok_interaction_reply_comment_post(reply_comment_request=reply_comment_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TikTokInteractionAPIApi->reply_comment_api_v1_tiktok_interaction_reply_comment_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reply_comment_request** | [**ReplyCommentRequest**](ReplyCommentRequest.md)|  | [optional] 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reply_comment_api_v1_tiktok_interaction_reply_comment_post_0**
> ResponseModel reply_comment_api_v1_tiktok_interaction_reply_comment_post_0(reply_comment_request=reply_comment_request)

回复评论/Reply to comment

# [中文] ### 用途: - 使用用户Cookie回复指定视频的一个评论，当前请尽可能使用美国地区的TikTok账号，并且在获取Cookie时请使用美国地区的代理IP。 ### 注意: - 交互类接口都需要使用用户的Cookie，因此请确保你的Cookie是有效的，否则将无法正常请求。 - 交互类的接口可能会导致账号异常或封禁，因此请谨慎使用，建议使用代理IP进行请求。 - 交互类接口的最终结果可能会受到TikTok风控系统的影响，大多数情况跟你所使用的账号有关，比如新注册的账号可能无法关注用户或点赞视频，我们无法处理基于账号的风控问题。 - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。 ### 参数: - aweme_id: 视频id，可以从分享链接中获取，例如：https://www.tiktok.com/@username/video/7419966340443819295 - reply_id: 要回复的目标评论ID，可以从指定视频的评论数据接口中获取，通常关键字为`cid`或`comment_id`或`reply_id`。 - text: 评论内容，TikTok评论内容需要符合规范，不要带有违规的关键词，否则即使请求成功也会被系统判定为垃圾评论从而不被展示，提交时请使用URL编码评论字符串。 - cookie: 用户Cookie，可以从浏览器中登录自己的TikTok账号，然后复制Cookie信息，提交时请使用URL编码Cookie字符串。 - device_id: 设备id，可选，如果不填写则会自动生成，如果需要自定义设备id，请使用设备信息接口获取设备id。 - iid: 设备安装id，可选，如果不填写则会自动生成，如果需要自定义设备iid，请使用设备信息接口获取设备iid。 - proxy: 代理IP，可选，如果不填写则会使用服务器IP进行请求（不推荐），建议使用代理IP进行请求防止账号异常获被封禁，支持格式如下：     - 代理IP:端口     - 用户名:密码@代理IP:端口 ### 返回: - 回复评论结果以及评论数据和设备信息，请自行保留设备信息，如请求时使用的`device_id`以及`iid`，以便后续调用接口时使用，频繁更换设备信息可能会导致账号异常或封禁。  # [English] ### Purpose: - Reply to a comment on a specified video using user cookies, please try to use TikTok accounts in the United States as much as possible, and use proxy IPs in the United States when obtaining cookies. ### Note: - Interactive interfaces all need to use the user's Cookie, so please make sure that your Cookie is valid, otherwise the request will not be made normally. - Interactive interfaces may cause account exceptions or bans, so please use them with caution, and it is recommended to use proxy IPs for requests. - The final result of the interactive interface may be affected by the TikTok risk control system, and in most cases it is related to the account you are using, for example, a newly registered account may not be able to follow users or like videos, and we cannot handle risk control issues based on accounts. - Please do not use interactive interfaces to harass others, or engage in illegal or irregular operations, otherwise we will stop providing services to you, and all responsibilities will be borne by you. ### Parameters: - aweme_id: Video id, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/7419966340443819295 - reply_id: The target comment ID to reply to, which can be obtained from the comment data interface of the specified video, usually the keyword is `cid` or `comment_id` or `reply_id`. - text: Comment content, TikTok comment content needs to comply with the specifications, do not contain illegal keywords, otherwise, even if the request is successful, it will be judged as spam comments by the system and will not be displayed, please use URL-encoded comment string when submitting. - cookie: User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-encoded Cookie string when submitting. - device_id: Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, please use the device information interface to get the device id. - iid: Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device iid, please use the device information interface to get the device iid. - proxy: Proxy IP, optional, if not filled in, the server IP will be used for the request (not recommended), it is recommended to use a proxy IP for the request to prevent account exceptions or bans, support the following formats:     - Proxy IP:Port     - Username:Password@Proxy IP:Port ### Return: - Reply comment results, comment data and device information, please keep the device information, such as the `device_id` and `iid` used when requesting, for subsequent calls to the interface, frequent replacement of device information may cause account exceptions or bans.  # [示例/Example] ```python # Python Code text = urllib.parse.quote(\"Hello, TikTok!\") cookie = urllib.parse.quote(\"Your_Cookie_From_Browser\") payload = {     \"aweme_id\": \"7419966340443819295\",     \"reply_id\": \"7420673787547419435\",     \"text\": text,     \"cookie\": cookie,     \"proxy\": \"\", } ```

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
    api_instance = tikhub_sdk_v2.TikTokInteractionAPIApi(api_client)
    reply_comment_request = tikhub_sdk_v2.ReplyCommentRequest() # ReplyCommentRequest |  (optional)

    try:
        # 回复评论/Reply to comment
        api_response = api_instance.reply_comment_api_v1_tiktok_interaction_reply_comment_post_0(reply_comment_request=reply_comment_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TikTokInteractionAPIApi->reply_comment_api_v1_tiktok_interaction_reply_comment_post_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reply_comment_request** | [**ReplyCommentRequest**](ReplyCommentRequest.md)|  | [optional] 

### Return type

[**ResponseModel**](ResponseModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

