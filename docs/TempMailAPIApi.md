# tikhub_sdk_v2.TempMailAPIApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_email_by_id_api_v1_temp_mail_v1_get_email_by_id_get**](TempMailAPIApi.md#get_email_by_id_api_v1_temp_mail_v1_get_email_by_id_get) | **GET** /api/v1/temp_mail/v1/get_email_by_id | Get Email By Id
[**get_email_by_id_api_v1_temp_mail_v1_get_email_by_id_get_0**](TempMailAPIApi.md#get_email_by_id_api_v1_temp_mail_v1_get_email_by_id_get_0) | **GET** /api/v1/temp_mail/v1/get_email_by_id | Get Email By Id
[**get_emails_api_v1_temp_mail_v1_get_emails_inbox_get**](TempMailAPIApi.md#get_emails_api_v1_temp_mail_v1_get_emails_inbox_get) | **GET** /api/v1/temp_mail/v1/get_emails_inbox | Get Emails
[**get_emails_api_v1_temp_mail_v1_get_emails_inbox_get_0**](TempMailAPIApi.md#get_emails_api_v1_temp_mail_v1_get_emails_inbox_get_0) | **GET** /api/v1/temp_mail/v1/get_emails_inbox | Get Emails
[**get_temp_email_api_v1_temp_mail_v1_get_temp_email_address_get**](TempMailAPIApi.md#get_temp_email_api_v1_temp_mail_v1_get_temp_email_address_get) | **GET** /api/v1/temp_mail/v1/get_temp_email_address | Get Temp Email
[**get_temp_email_api_v1_temp_mail_v1_get_temp_email_address_get_0**](TempMailAPIApi.md#get_temp_email_api_v1_temp_mail_v1_get_temp_email_address_get_0) | **GET** /api/v1/temp_mail/v1/get_temp_email_address | Get Temp Email


# **get_email_by_id_api_v1_temp_mail_v1_get_email_by_id_get**
> ResponseModel get_email_by_id_api_v1_temp_mail_v1_get_email_by_id_get(token, message_id)

Get Email By Id

# [中文] ### 用途: - 通过邮件ID获取邮件数据 ### 参数: - token: 邮箱Bearer Token - message_id: 邮件ID ### 返回: - 邮件数据  # [English] ### Purpose: - Get email data by email ID ### Parameters: - token: Email Bearer Token - message_id: Email ID ### Returns: - Email data

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
    api_instance = tikhub_sdk_v2.TempMailAPIApi(api_client)
    token = 'token_example' # str | Bearer Token
message_id = 'message_id_example' # str | Message ID

    try:
        # Get Email By Id
        api_response = api_instance.get_email_by_id_api_v1_temp_mail_v1_get_email_by_id_get(token, message_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TempMailAPIApi->get_email_by_id_api_v1_temp_mail_v1_get_email_by_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Bearer Token | 
 **message_id** | **str**| Message ID | 

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

# **get_email_by_id_api_v1_temp_mail_v1_get_email_by_id_get_0**
> ResponseModel get_email_by_id_api_v1_temp_mail_v1_get_email_by_id_get_0(token, message_id)

Get Email By Id

# [中文] ### 用途: - 通过邮件ID获取邮件数据 ### 参数: - token: 邮箱Bearer Token - message_id: 邮件ID ### 返回: - 邮件数据  # [English] ### Purpose: - Get email data by email ID ### Parameters: - token: Email Bearer Token - message_id: Email ID ### Returns: - Email data

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
    api_instance = tikhub_sdk_v2.TempMailAPIApi(api_client)
    token = 'token_example' # str | Bearer Token
message_id = 'message_id_example' # str | Message ID

    try:
        # Get Email By Id
        api_response = api_instance.get_email_by_id_api_v1_temp_mail_v1_get_email_by_id_get_0(token, message_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TempMailAPIApi->get_email_by_id_api_v1_temp_mail_v1_get_email_by_id_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Bearer Token | 
 **message_id** | **str**| Message ID | 

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

# **get_emails_api_v1_temp_mail_v1_get_emails_inbox_get**
> ResponseModel get_emails_api_v1_temp_mail_v1_get_emails_inbox_get(token)

Get Emails

# [中文] ### 用途: - 获取邮件列表 ### 参数: - token: 邮箱Bearer Token ### 返回: - emails: 邮件列表  # [English] ### Purpose: - Get a list of emails ### Parameters: - token: Email Bearer Token ### Returns: - emails: List of emails

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
    api_instance = tikhub_sdk_v2.TempMailAPIApi(api_client)
    token = 'token_example' # str | Bearer Token

    try:
        # Get Emails
        api_response = api_instance.get_emails_api_v1_temp_mail_v1_get_emails_inbox_get(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TempMailAPIApi->get_emails_api_v1_temp_mail_v1_get_emails_inbox_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Bearer Token | 

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

# **get_emails_api_v1_temp_mail_v1_get_emails_inbox_get_0**
> ResponseModel get_emails_api_v1_temp_mail_v1_get_emails_inbox_get_0(token)

Get Emails

# [中文] ### 用途: - 获取邮件列表 ### 参数: - token: 邮箱Bearer Token ### 返回: - emails: 邮件列表  # [English] ### Purpose: - Get a list of emails ### Parameters: - token: Email Bearer Token ### Returns: - emails: List of emails

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
    api_instance = tikhub_sdk_v2.TempMailAPIApi(api_client)
    token = 'token_example' # str | Bearer Token

    try:
        # Get Emails
        api_response = api_instance.get_emails_api_v1_temp_mail_v1_get_emails_inbox_get_0(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TempMailAPIApi->get_emails_api_v1_temp_mail_v1_get_emails_inbox_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Bearer Token | 

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

# **get_temp_email_api_v1_temp_mail_v1_get_temp_email_address_get**
> ResponseModel get_temp_email_api_v1_temp_mail_v1_get_temp_email_address_get()

Get Temp Email

# [中文] ### 用途: - 获取一个临时邮箱地址 - 用于注册或者接收邮件，该邮箱地址不会被删除，也不会被其他人使用。 - 该邮箱无法发送邮件，只能接收邮件。 - 请自行保存邮箱地址、用户名、密码、Bearer Token，我们无法帮助您找回这些关键信息。 ### 参数: - 无 ### 返回: - domain: 邮箱域名 - name: 邮箱用户名 - password: 邮箱密码 - email_address: 邮箱地址 - token: 邮箱Bearer Token  # [English] ### Purpose: - Get a temporary email address - Used for registration or receiving emails, this email address will not be deleted or used by others. - This email cannot send emails, only receive emails. - Please save the email address, username, password, and Bearer Token yourself, we cannot help you retrieve this critical information. ### Parameters: - None ### Returns: - domain: Email domain - name: Email username - password: Email password - email_address: Email address - token: Email Bearer Token

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
    api_instance = tikhub_sdk_v2.TempMailAPIApi(api_client)
    
    try:
        # Get Temp Email
        api_response = api_instance.get_temp_email_api_v1_temp_mail_v1_get_temp_email_address_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TempMailAPIApi->get_temp_email_api_v1_temp_mail_v1_get_temp_email_address_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_temp_email_api_v1_temp_mail_v1_get_temp_email_address_get_0**
> ResponseModel get_temp_email_api_v1_temp_mail_v1_get_temp_email_address_get_0()

Get Temp Email

# [中文] ### 用途: - 获取一个临时邮箱地址 - 用于注册或者接收邮件，该邮箱地址不会被删除，也不会被其他人使用。 - 该邮箱无法发送邮件，只能接收邮件。 - 请自行保存邮箱地址、用户名、密码、Bearer Token，我们无法帮助您找回这些关键信息。 ### 参数: - 无 ### 返回: - domain: 邮箱域名 - name: 邮箱用户名 - password: 邮箱密码 - email_address: 邮箱地址 - token: 邮箱Bearer Token  # [English] ### Purpose: - Get a temporary email address - Used for registration or receiving emails, this email address will not be deleted or used by others. - This email cannot send emails, only receive emails. - Please save the email address, username, password, and Bearer Token yourself, we cannot help you retrieve this critical information. ### Parameters: - None ### Returns: - domain: Email domain - name: Email username - password: Email password - email_address: Email address - token: Email Bearer Token

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
    api_instance = tikhub_sdk_v2.TempMailAPIApi(api_client)
    
    try:
        # Get Temp Email
        api_response = api_instance.get_temp_email_api_v1_temp_mail_v1_get_temp_email_address_get_0()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TempMailAPIApi->get_temp_email_api_v1_temp_mail_v1_get_temp_email_address_get_0: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

