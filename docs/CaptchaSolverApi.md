# tikhub_sdk_v2.CaptchaSolverApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**amazon_captcha_api_v1_captcha_amazon_captcha_post**](CaptchaSolverApi.md#amazon_captcha_api_v1_captcha_amazon_captcha_post) | **POST** /api/v1/captcha/amazon_captcha | Amazon Captcha Solver/Amazon验证码解决器
[**amazon_captcha_api_v1_captcha_amazon_captcha_post_0**](CaptchaSolverApi.md#amazon_captcha_api_v1_captcha_amazon_captcha_post_0) | **POST** /api/v1/captcha/amazon_captcha | Amazon Captcha Solver/Amazon验证码解决器
[**cloudflare_turnstile_api_v1_captcha_cloudflare_turnstile_post**](CaptchaSolverApi.md#cloudflare_turnstile_api_v1_captcha_cloudflare_turnstile_post) | **POST** /api/v1/captcha/cloudflare_turnstile | Cloudflare Turnstile Solver/Cloudflare Turnstile解决器
[**cloudflare_turnstile_api_v1_captcha_cloudflare_turnstile_post_0**](CaptchaSolverApi.md#cloudflare_turnstile_api_v1_captcha_cloudflare_turnstile_post_0) | **POST** /api/v1/captcha/cloudflare_turnstile | Cloudflare Turnstile Solver/Cloudflare Turnstile解决器
[**hcaptcha_api_v1_captcha_hcaptcha_post**](CaptchaSolverApi.md#hcaptcha_api_v1_captcha_hcaptcha_post) | **POST** /api/v1/captcha/hcaptcha | hCaptcha Solver/hCaptcha解决器
[**hcaptcha_api_v1_captcha_hcaptcha_post_0**](CaptchaSolverApi.md#hcaptcha_api_v1_captcha_hcaptcha_post_0) | **POST** /api/v1/captcha/hcaptcha | hCaptcha Solver/hCaptcha解决器
[**recaptcha_v2_api_v1_captcha_recaptcha_v2_post**](CaptchaSolverApi.md#recaptcha_v2_api_v1_captcha_recaptcha_v2_post) | **POST** /api/v1/captcha/recaptcha_v2 | Recaptcha V2 Solver/Recaptcha V2解决器
[**recaptcha_v2_api_v1_captcha_recaptcha_v2_post_0**](CaptchaSolverApi.md#recaptcha_v2_api_v1_captcha_recaptcha_v2_post_0) | **POST** /api/v1/captcha/recaptcha_v2 | Recaptcha V2 Solver/Recaptcha V2解决器
[**recaptcha_v3_api_v1_captcha_recaptcha_v3_post**](CaptchaSolverApi.md#recaptcha_v3_api_v1_captcha_recaptcha_v3_post) | **POST** /api/v1/captcha/recaptcha_v3 | Recaptcha V3 Solver/Recaptcha V3解决器
[**recaptcha_v3_api_v1_captcha_recaptcha_v3_post_0**](CaptchaSolverApi.md#recaptcha_v3_api_v1_captcha_recaptcha_v3_post_0) | **POST** /api/v1/captcha/recaptcha_v3 | Recaptcha V3 Solver/Recaptcha V3解决器
[**tencent_captcha_api_v1_captcha_tencent_captcha_post**](CaptchaSolverApi.md#tencent_captcha_api_v1_captcha_tencent_captcha_post) | **POST** /api/v1/captcha/tencent_captcha | Tencent Captcha Solver/Tencent验证码解决器
[**tencent_captcha_api_v1_captcha_tencent_captcha_post_0**](CaptchaSolverApi.md#tencent_captcha_api_v1_captcha_tencent_captcha_post_0) | **POST** /api/v1/captcha/tencent_captcha | Tencent Captcha Solver/Tencent验证码解决器


# **amazon_captcha_api_v1_captcha_amazon_captcha_post**
> ResponseModel amazon_captcha_api_v1_captcha_amazon_captcha_post(body_amazon_captcha_api_v1_captcha_amazon_captcha_post=body_amazon_captcha_api_v1_captcha_amazon_captcha_post)

Amazon Captcha Solver/Amazon验证码解决器

# [中文] ### 用途: - Amazon Captcha验证码解决器 ### 参数: - app_id: 在HTML中可以找到网站对应的app_id - url: 需要解决验证码的URL - proxy: 默认为None ### 返回: - 返回验证码解决结果  # [English] ### Purpose: - Amazon Captcha solver ### Parameters: - app_id: The app_id corresponding to the website can be found in the HTML - url: URL that needs to solve the captcha - proxy: Default is None ### Return: - Return the captcha solution result  # [Example/示例] app_id = \"10000000\" url = \"https://www.amazon.com/\" proxy = None

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
    api_instance = tikhub_sdk_v2.CaptchaSolverApi(api_client)
    body_amazon_captcha_api_v1_captcha_amazon_captcha_post = tikhub_sdk_v2.BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost() # BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost |  (optional)

    try:
        # Amazon Captcha Solver/Amazon验证码解决器
        api_response = api_instance.amazon_captcha_api_v1_captcha_amazon_captcha_post(body_amazon_captcha_api_v1_captcha_amazon_captcha_post=body_amazon_captcha_api_v1_captcha_amazon_captcha_post)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CaptchaSolverApi->amazon_captcha_api_v1_captcha_amazon_captcha_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_amazon_captcha_api_v1_captcha_amazon_captcha_post** | [**BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost**](BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost.md)|  | [optional] 

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

# **amazon_captcha_api_v1_captcha_amazon_captcha_post_0**
> ResponseModel amazon_captcha_api_v1_captcha_amazon_captcha_post_0(body_amazon_captcha_api_v1_captcha_amazon_captcha_post=body_amazon_captcha_api_v1_captcha_amazon_captcha_post)

Amazon Captcha Solver/Amazon验证码解决器

# [中文] ### 用途: - Amazon Captcha验证码解决器 ### 参数: - app_id: 在HTML中可以找到网站对应的app_id - url: 需要解决验证码的URL - proxy: 默认为None ### 返回: - 返回验证码解决结果  # [English] ### Purpose: - Amazon Captcha solver ### Parameters: - app_id: The app_id corresponding to the website can be found in the HTML - url: URL that needs to solve the captcha - proxy: Default is None ### Return: - Return the captcha solution result  # [Example/示例] app_id = \"10000000\" url = \"https://www.amazon.com/\" proxy = None

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
    api_instance = tikhub_sdk_v2.CaptchaSolverApi(api_client)
    body_amazon_captcha_api_v1_captcha_amazon_captcha_post = tikhub_sdk_v2.BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost() # BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost |  (optional)

    try:
        # Amazon Captcha Solver/Amazon验证码解决器
        api_response = api_instance.amazon_captcha_api_v1_captcha_amazon_captcha_post_0(body_amazon_captcha_api_v1_captcha_amazon_captcha_post=body_amazon_captcha_api_v1_captcha_amazon_captcha_post)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CaptchaSolverApi->amazon_captcha_api_v1_captcha_amazon_captcha_post_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_amazon_captcha_api_v1_captcha_amazon_captcha_post** | [**BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost**](BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost.md)|  | [optional] 

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

# **cloudflare_turnstile_api_v1_captcha_cloudflare_turnstile_post**
> ResponseModel cloudflare_turnstile_api_v1_captcha_cloudflare_turnstile_post(body_cloudflare_turnstile_api_v1_captcha_cloudflare_turnstile_post=body_cloudflare_turnstile_api_v1_captcha_cloudflare_turnstile_post)

Cloudflare Turnstile Solver/Cloudflare Turnstile解决器

# [中文] ### 用途: - Cloudflare Turnstile验证码解决器 ### 参数: - sitekey: 在HTML中可以找到网站对应的sitekey - url: 需要解决验证码的URL - proxy: 默认为None ### 返回: - 返回验证码解决结果  # [English] ### Purpose: - Cloudflare Turnstile captcha solver ### Parameters: - sitekey: The sitekey corresponding to the website can be found in the HTML - url: URL that needs to solve the captcha - action: Default is None - data: Default is None - proxy: Default is None ### Return: - Return the captcha solution result  # [Example/示例] sitekey = \"1x00000000000000000000AA\" url = \"https://demo.turnstile.workers.dev\" proxy = None

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
    api_instance = tikhub_sdk_v2.CaptchaSolverApi(api_client)
    body_cloudflare_turnstile_api_v1_captcha_cloudflare_turnstile_post = tikhub_sdk_v2.BodyCloudflareTurnstileApiV1CaptchaCloudflareTurnstilePost() # BodyCloudflareTurnstileApiV1CaptchaCloudflareTurnstilePost |  (optional)

    try:
        # Cloudflare Turnstile Solver/Cloudflare Turnstile解决器
        api_response = api_instance.cloudflare_turnstile_api_v1_captcha_cloudflare_turnstile_post(body_cloudflare_turnstile_api_v1_captcha_cloudflare_turnstile_post=body_cloudflare_turnstile_api_v1_captcha_cloudflare_turnstile_post)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CaptchaSolverApi->cloudflare_turnstile_api_v1_captcha_cloudflare_turnstile_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_cloudflare_turnstile_api_v1_captcha_cloudflare_turnstile_post** | [**BodyCloudflareTurnstileApiV1CaptchaCloudflareTurnstilePost**](BodyCloudflareTurnstileApiV1CaptchaCloudflareTurnstilePost.md)|  | [optional] 

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

# **cloudflare_turnstile_api_v1_captcha_cloudflare_turnstile_post_0**
> ResponseModel cloudflare_turnstile_api_v1_captcha_cloudflare_turnstile_post_0(body_cloudflare_turnstile_api_v1_captcha_cloudflare_turnstile_post=body_cloudflare_turnstile_api_v1_captcha_cloudflare_turnstile_post)

Cloudflare Turnstile Solver/Cloudflare Turnstile解决器

# [中文] ### 用途: - Cloudflare Turnstile验证码解决器 ### 参数: - sitekey: 在HTML中可以找到网站对应的sitekey - url: 需要解决验证码的URL - proxy: 默认为None ### 返回: - 返回验证码解决结果  # [English] ### Purpose: - Cloudflare Turnstile captcha solver ### Parameters: - sitekey: The sitekey corresponding to the website can be found in the HTML - url: URL that needs to solve the captcha - action: Default is None - data: Default is None - proxy: Default is None ### Return: - Return the captcha solution result  # [Example/示例] sitekey = \"1x00000000000000000000AA\" url = \"https://demo.turnstile.workers.dev\" proxy = None

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
    api_instance = tikhub_sdk_v2.CaptchaSolverApi(api_client)
    body_cloudflare_turnstile_api_v1_captcha_cloudflare_turnstile_post = tikhub_sdk_v2.BodyCloudflareTurnstileApiV1CaptchaCloudflareTurnstilePost() # BodyCloudflareTurnstileApiV1CaptchaCloudflareTurnstilePost |  (optional)

    try:
        # Cloudflare Turnstile Solver/Cloudflare Turnstile解决器
        api_response = api_instance.cloudflare_turnstile_api_v1_captcha_cloudflare_turnstile_post_0(body_cloudflare_turnstile_api_v1_captcha_cloudflare_turnstile_post=body_cloudflare_turnstile_api_v1_captcha_cloudflare_turnstile_post)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CaptchaSolverApi->cloudflare_turnstile_api_v1_captcha_cloudflare_turnstile_post_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_cloudflare_turnstile_api_v1_captcha_cloudflare_turnstile_post** | [**BodyCloudflareTurnstileApiV1CaptchaCloudflareTurnstilePost**](BodyCloudflareTurnstileApiV1CaptchaCloudflareTurnstilePost.md)|  | [optional] 

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

# **hcaptcha_api_v1_captcha_hcaptcha_post**
> ResponseModel hcaptcha_api_v1_captcha_hcaptcha_post(body_hcaptcha_api_v1_captcha_hcaptcha_post=body_hcaptcha_api_v1_captcha_hcaptcha_post)

hCaptcha Solver/hCaptcha解决器

# [中文] ### 用途: - hCaptcha验证码解决器 ### 参数: - sitekey: 在HTML中可以找到网站对应的sitekey - url: 需要解决验证码的URL - proxy: 默认为None ### 返回: - 返回验证码解决结果  # [English] ### Purpose: - hCaptcha captcha solver ### Parameters: - sitekey: The sitekey corresponding to the website can be found in the HTML - url: URL that needs to solve the captcha - proxy: Default is None ### Return: - Return the captcha solution result  # [Example/示例] sitekey = \"10000000-ffff-ffff-ffff-000000000001\" url = \"https://www.hcaptcha.com/\" proxy = None

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
    api_instance = tikhub_sdk_v2.CaptchaSolverApi(api_client)
    body_hcaptcha_api_v1_captcha_hcaptcha_post = tikhub_sdk_v2.BodyHcaptchaApiV1CaptchaHcaptchaPost() # BodyHcaptchaApiV1CaptchaHcaptchaPost |  (optional)

    try:
        # hCaptcha Solver/hCaptcha解决器
        api_response = api_instance.hcaptcha_api_v1_captcha_hcaptcha_post(body_hcaptcha_api_v1_captcha_hcaptcha_post=body_hcaptcha_api_v1_captcha_hcaptcha_post)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CaptchaSolverApi->hcaptcha_api_v1_captcha_hcaptcha_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_hcaptcha_api_v1_captcha_hcaptcha_post** | [**BodyHcaptchaApiV1CaptchaHcaptchaPost**](BodyHcaptchaApiV1CaptchaHcaptchaPost.md)|  | [optional] 

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

# **hcaptcha_api_v1_captcha_hcaptcha_post_0**
> ResponseModel hcaptcha_api_v1_captcha_hcaptcha_post_0(body_hcaptcha_api_v1_captcha_hcaptcha_post=body_hcaptcha_api_v1_captcha_hcaptcha_post)

hCaptcha Solver/hCaptcha解决器

# [中文] ### 用途: - hCaptcha验证码解决器 ### 参数: - sitekey: 在HTML中可以找到网站对应的sitekey - url: 需要解决验证码的URL - proxy: 默认为None ### 返回: - 返回验证码解决结果  # [English] ### Purpose: - hCaptcha captcha solver ### Parameters: - sitekey: The sitekey corresponding to the website can be found in the HTML - url: URL that needs to solve the captcha - proxy: Default is None ### Return: - Return the captcha solution result  # [Example/示例] sitekey = \"10000000-ffff-ffff-ffff-000000000001\" url = \"https://www.hcaptcha.com/\" proxy = None

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
    api_instance = tikhub_sdk_v2.CaptchaSolverApi(api_client)
    body_hcaptcha_api_v1_captcha_hcaptcha_post = tikhub_sdk_v2.BodyHcaptchaApiV1CaptchaHcaptchaPost() # BodyHcaptchaApiV1CaptchaHcaptchaPost |  (optional)

    try:
        # hCaptcha Solver/hCaptcha解决器
        api_response = api_instance.hcaptcha_api_v1_captcha_hcaptcha_post_0(body_hcaptcha_api_v1_captcha_hcaptcha_post=body_hcaptcha_api_v1_captcha_hcaptcha_post)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CaptchaSolverApi->hcaptcha_api_v1_captcha_hcaptcha_post_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_hcaptcha_api_v1_captcha_hcaptcha_post** | [**BodyHcaptchaApiV1CaptchaHcaptchaPost**](BodyHcaptchaApiV1CaptchaHcaptchaPost.md)|  | [optional] 

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

# **recaptcha_v2_api_v1_captcha_recaptcha_v2_post**
> ResponseModel recaptcha_v2_api_v1_captcha_recaptcha_v2_post(body_recaptcha_v2_api_v1_captcha_recaptcha_v2_post=body_recaptcha_v2_api_v1_captcha_recaptcha_v2_post)

Recaptcha V2 Solver/Recaptcha V2解决器

# [中文] ### 用途: - Recaptcha V2验证码解决器 ### 参数: - sitekey: 在HTML中可以找到网站对应的sitekey - url: 需要解决验证码的URL - proxy: 默认为None ### 返回: - 返回验证码解决结果  # [English] ### Purpose: - Recaptcha V2 captcha solver ### Parameters: - sitekey: The sitekey corresponding to the website can be found in the HTML - url: URL that needs to solve the captcha - proxy: Default is None ### Return: - Return the captcha solution result  # [Example/示例] sitekey = \"6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-\" url = \"https://www.google.com/recaptcha/api2/demo\" proxy = None

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
    api_instance = tikhub_sdk_v2.CaptchaSolverApi(api_client)
    body_recaptcha_v2_api_v1_captcha_recaptcha_v2_post = tikhub_sdk_v2.BodyRecaptchaV2ApiV1CaptchaRecaptchaV2Post() # BodyRecaptchaV2ApiV1CaptchaRecaptchaV2Post |  (optional)

    try:
        # Recaptcha V2 Solver/Recaptcha V2解决器
        api_response = api_instance.recaptcha_v2_api_v1_captcha_recaptcha_v2_post(body_recaptcha_v2_api_v1_captcha_recaptcha_v2_post=body_recaptcha_v2_api_v1_captcha_recaptcha_v2_post)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CaptchaSolverApi->recaptcha_v2_api_v1_captcha_recaptcha_v2_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_recaptcha_v2_api_v1_captcha_recaptcha_v2_post** | [**BodyRecaptchaV2ApiV1CaptchaRecaptchaV2Post**](BodyRecaptchaV2ApiV1CaptchaRecaptchaV2Post.md)|  | [optional] 

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

# **recaptcha_v2_api_v1_captcha_recaptcha_v2_post_0**
> ResponseModel recaptcha_v2_api_v1_captcha_recaptcha_v2_post_0(body_recaptcha_v2_api_v1_captcha_recaptcha_v2_post=body_recaptcha_v2_api_v1_captcha_recaptcha_v2_post)

Recaptcha V2 Solver/Recaptcha V2解决器

# [中文] ### 用途: - Recaptcha V2验证码解决器 ### 参数: - sitekey: 在HTML中可以找到网站对应的sitekey - url: 需要解决验证码的URL - proxy: 默认为None ### 返回: - 返回验证码解决结果  # [English] ### Purpose: - Recaptcha V2 captcha solver ### Parameters: - sitekey: The sitekey corresponding to the website can be found in the HTML - url: URL that needs to solve the captcha - proxy: Default is None ### Return: - Return the captcha solution result  # [Example/示例] sitekey = \"6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-\" url = \"https://www.google.com/recaptcha/api2/demo\" proxy = None

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
    api_instance = tikhub_sdk_v2.CaptchaSolverApi(api_client)
    body_recaptcha_v2_api_v1_captcha_recaptcha_v2_post = tikhub_sdk_v2.BodyRecaptchaV2ApiV1CaptchaRecaptchaV2Post() # BodyRecaptchaV2ApiV1CaptchaRecaptchaV2Post |  (optional)

    try:
        # Recaptcha V2 Solver/Recaptcha V2解决器
        api_response = api_instance.recaptcha_v2_api_v1_captcha_recaptcha_v2_post_0(body_recaptcha_v2_api_v1_captcha_recaptcha_v2_post=body_recaptcha_v2_api_v1_captcha_recaptcha_v2_post)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CaptchaSolverApi->recaptcha_v2_api_v1_captcha_recaptcha_v2_post_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_recaptcha_v2_api_v1_captcha_recaptcha_v2_post** | [**BodyRecaptchaV2ApiV1CaptchaRecaptchaV2Post**](BodyRecaptchaV2ApiV1CaptchaRecaptchaV2Post.md)|  | [optional] 

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

# **recaptcha_v3_api_v1_captcha_recaptcha_v3_post**
> ResponseModel recaptcha_v3_api_v1_captcha_recaptcha_v3_post(body_recaptcha_v3_api_v1_captcha_recaptcha_v3_post=body_recaptcha_v3_api_v1_captcha_recaptcha_v3_post)

Recaptcha V3 Solver/Recaptcha V3解决器

# [中文] ### 用途: - Recaptcha V3验证码解决器 ### 参数: - sitekey: 在HTML中可以找到网站对应的sitekey - url: 需要解决验证码的URL - proxy: 默认为None ### 返回: - 返回验证码解决结果  # [English] ### Purpose: - Recaptcha V3 captcha solver ### Parameters: - sitekey: The sitekey corresponding to the website can be found in the HTML - url: URL that needs to solve the captcha - proxy: Default is None ### Return: - Return the captcha solution result  # [Example/示例] sitekey = \"6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-\" url = \"https://www.google.com/recaptcha/api2/demo\" proxy = None

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
    api_instance = tikhub_sdk_v2.CaptchaSolverApi(api_client)
    body_recaptcha_v3_api_v1_captcha_recaptcha_v3_post = tikhub_sdk_v2.BodyRecaptchaV3ApiV1CaptchaRecaptchaV3Post() # BodyRecaptchaV3ApiV1CaptchaRecaptchaV3Post |  (optional)

    try:
        # Recaptcha V3 Solver/Recaptcha V3解决器
        api_response = api_instance.recaptcha_v3_api_v1_captcha_recaptcha_v3_post(body_recaptcha_v3_api_v1_captcha_recaptcha_v3_post=body_recaptcha_v3_api_v1_captcha_recaptcha_v3_post)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CaptchaSolverApi->recaptcha_v3_api_v1_captcha_recaptcha_v3_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_recaptcha_v3_api_v1_captcha_recaptcha_v3_post** | [**BodyRecaptchaV3ApiV1CaptchaRecaptchaV3Post**](BodyRecaptchaV3ApiV1CaptchaRecaptchaV3Post.md)|  | [optional] 

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

# **recaptcha_v3_api_v1_captcha_recaptcha_v3_post_0**
> ResponseModel recaptcha_v3_api_v1_captcha_recaptcha_v3_post_0(body_recaptcha_v3_api_v1_captcha_recaptcha_v3_post=body_recaptcha_v3_api_v1_captcha_recaptcha_v3_post)

Recaptcha V3 Solver/Recaptcha V3解决器

# [中文] ### 用途: - Recaptcha V3验证码解决器 ### 参数: - sitekey: 在HTML中可以找到网站对应的sitekey - url: 需要解决验证码的URL - proxy: 默认为None ### 返回: - 返回验证码解决结果  # [English] ### Purpose: - Recaptcha V3 captcha solver ### Parameters: - sitekey: The sitekey corresponding to the website can be found in the HTML - url: URL that needs to solve the captcha - proxy: Default is None ### Return: - Return the captcha solution result  # [Example/示例] sitekey = \"6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-\" url = \"https://www.google.com/recaptcha/api2/demo\" proxy = None

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
    api_instance = tikhub_sdk_v2.CaptchaSolverApi(api_client)
    body_recaptcha_v3_api_v1_captcha_recaptcha_v3_post = tikhub_sdk_v2.BodyRecaptchaV3ApiV1CaptchaRecaptchaV3Post() # BodyRecaptchaV3ApiV1CaptchaRecaptchaV3Post |  (optional)

    try:
        # Recaptcha V3 Solver/Recaptcha V3解决器
        api_response = api_instance.recaptcha_v3_api_v1_captcha_recaptcha_v3_post_0(body_recaptcha_v3_api_v1_captcha_recaptcha_v3_post=body_recaptcha_v3_api_v1_captcha_recaptcha_v3_post)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CaptchaSolverApi->recaptcha_v3_api_v1_captcha_recaptcha_v3_post_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_recaptcha_v3_api_v1_captcha_recaptcha_v3_post** | [**BodyRecaptchaV3ApiV1CaptchaRecaptchaV3Post**](BodyRecaptchaV3ApiV1CaptchaRecaptchaV3Post.md)|  | [optional] 

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

# **tencent_captcha_api_v1_captcha_tencent_captcha_post**
> ResponseModel tencent_captcha_api_v1_captcha_tencent_captcha_post(body_tencent_captcha_api_v1_captcha_tencent_captcha_post=body_tencent_captcha_api_v1_captcha_tencent_captcha_post)

Tencent Captcha Solver/Tencent验证码解决器

# [中文] ### 用途: - Tencent Captcha验证码解决器 ### 参数: - app_id: 在HTML中可以找到网站对应的app_id - url: 需要解决验证码的URL - proxy: 默认为None ### 返回: - 返回验证码解决结果  # [English] ### Purpose: - Tencent Captcha solver ### Parameters: - app_id: The app_id corresponding to the website can be found in the HTML - url: URL that needs to solve the captcha - proxy: Default is None ### Return: - Return the captcha solution result  # [Example/示例] app_id = \"10000000\" url = \"https://www.tencent.com/\" proxy = None

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
    api_instance = tikhub_sdk_v2.CaptchaSolverApi(api_client)
    body_tencent_captcha_api_v1_captcha_tencent_captcha_post = tikhub_sdk_v2.BodyTencentCaptchaApiV1CaptchaTencentCaptchaPost() # BodyTencentCaptchaApiV1CaptchaTencentCaptchaPost |  (optional)

    try:
        # Tencent Captcha Solver/Tencent验证码解决器
        api_response = api_instance.tencent_captcha_api_v1_captcha_tencent_captcha_post(body_tencent_captcha_api_v1_captcha_tencent_captcha_post=body_tencent_captcha_api_v1_captcha_tencent_captcha_post)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CaptchaSolverApi->tencent_captcha_api_v1_captcha_tencent_captcha_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_tencent_captcha_api_v1_captcha_tencent_captcha_post** | [**BodyTencentCaptchaApiV1CaptchaTencentCaptchaPost**](BodyTencentCaptchaApiV1CaptchaTencentCaptchaPost.md)|  | [optional] 

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

# **tencent_captcha_api_v1_captcha_tencent_captcha_post_0**
> ResponseModel tencent_captcha_api_v1_captcha_tencent_captcha_post_0(body_tencent_captcha_api_v1_captcha_tencent_captcha_post=body_tencent_captcha_api_v1_captcha_tencent_captcha_post)

Tencent Captcha Solver/Tencent验证码解决器

# [中文] ### 用途: - Tencent Captcha验证码解决器 ### 参数: - app_id: 在HTML中可以找到网站对应的app_id - url: 需要解决验证码的URL - proxy: 默认为None ### 返回: - 返回验证码解决结果  # [English] ### Purpose: - Tencent Captcha solver ### Parameters: - app_id: The app_id corresponding to the website can be found in the HTML - url: URL that needs to solve the captcha - proxy: Default is None ### Return: - Return the captcha solution result  # [Example/示例] app_id = \"10000000\" url = \"https://www.tencent.com/\" proxy = None

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
    api_instance = tikhub_sdk_v2.CaptchaSolverApi(api_client)
    body_tencent_captcha_api_v1_captcha_tencent_captcha_post = tikhub_sdk_v2.BodyTencentCaptchaApiV1CaptchaTencentCaptchaPost() # BodyTencentCaptchaApiV1CaptchaTencentCaptchaPost |  (optional)

    try:
        # Tencent Captcha Solver/Tencent验证码解决器
        api_response = api_instance.tencent_captcha_api_v1_captcha_tencent_captcha_post_0(body_tencent_captcha_api_v1_captcha_tencent_captcha_post=body_tencent_captcha_api_v1_captcha_tencent_captcha_post)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CaptchaSolverApi->tencent_captcha_api_v1_captcha_tencent_captcha_post_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_tencent_captcha_api_v1_captcha_tencent_captcha_post** | [**BodyTencentCaptchaApiV1CaptchaTencentCaptchaPost**](BodyTencentCaptchaApiV1CaptchaTencentCaptchaPost.md)|  | [optional] 

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

