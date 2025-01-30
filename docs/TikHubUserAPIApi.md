# tikhub_sdk_v2.TikHubUserAPIApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_price_api_v1_tikhub_user_calculate_price_get**](TikHubUserAPIApi.md#calculate_price_api_v1_tikhub_user_calculate_price_get) | **GET** /api/v1/tikhub/user/calculate_price | 计算价格/Calculate price
[**calculate_price_api_v1_tikhub_user_calculate_price_get_0**](TikHubUserAPIApi.md#calculate_price_api_v1_tikhub_user_calculate_price_get_0) | **GET** /api/v1/tikhub/user/calculate_price | 计算价格/Calculate price
[**get_all_endpoints_info_api_v1_tikhub_user_get_all_endpoints_info_get**](TikHubUserAPIApi.md#get_all_endpoints_info_api_v1_tikhub_user_get_all_endpoints_info_get) | **GET** /api/v1/tikhub/user/get_all_endpoints_info | 获取所有端点信息/Get all endpoints information
[**get_all_endpoints_info_api_v1_tikhub_user_get_all_endpoints_info_get_0**](TikHubUserAPIApi.md#get_all_endpoints_info_api_v1_tikhub_user_get_all_endpoints_info_get_0) | **GET** /api/v1/tikhub/user/get_all_endpoints_info | 获取所有端点信息/Get all endpoints information
[**get_endpoint_info_api_v1_tikhub_user_get_endpoint_info_get**](TikHubUserAPIApi.md#get_endpoint_info_api_v1_tikhub_user_get_endpoint_info_get) | **GET** /api/v1/tikhub/user/get_endpoint_info | 获取一个端点的信息/Get information of an endpoint
[**get_endpoint_info_api_v1_tikhub_user_get_endpoint_info_get_0**](TikHubUserAPIApi.md#get_endpoint_info_api_v1_tikhub_user_get_endpoint_info_get_0) | **GET** /api/v1/tikhub/user/get_endpoint_info | 获取一个端点的信息/Get information of an endpoint
[**get_tiered_discount_info_api_v1_tikhub_user_get_tiered_discount_info_get**](TikHubUserAPIApi.md#get_tiered_discount_info_api_v1_tikhub_user_get_tiered_discount_info_get) | **GET** /api/v1/tikhub/user/get_tiered_discount_info | 获取阶梯式折扣百分比信息/Get tiered discount percentage information
[**get_tiered_discount_info_api_v1_tikhub_user_get_tiered_discount_info_get_0**](TikHubUserAPIApi.md#get_tiered_discount_info_api_v1_tikhub_user_get_tiered_discount_info_get_0) | **GET** /api/v1/tikhub/user/get_tiered_discount_info | 获取阶梯式折扣百分比信息/Get tiered discount percentage information
[**get_user_daily_usage_api_v1_tikhub_user_get_user_daily_usage_get**](TikHubUserAPIApi.md#get_user_daily_usage_api_v1_tikhub_user_get_user_daily_usage_get) | **GET** /api/v1/tikhub/user/get_user_daily_usage | 获取用户每日使用情况/Get user daily usage
[**get_user_daily_usage_api_v1_tikhub_user_get_user_daily_usage_get_0**](TikHubUserAPIApi.md#get_user_daily_usage_api_v1_tikhub_user_get_user_daily_usage_get_0) | **GET** /api/v1/tikhub/user/get_user_daily_usage | 获取用户每日使用情况/Get user daily usage
[**get_user_info_api_v1_tikhub_user_get_user_info_get**](TikHubUserAPIApi.md#get_user_info_api_v1_tikhub_user_get_user_info_get) | **GET** /api/v1/tikhub/user/get_user_info | 获取TikHub用户信息/Get TikHub user info
[**get_user_info_api_v1_tikhub_user_get_user_info_get_0**](TikHubUserAPIApi.md#get_user_info_api_v1_tikhub_user_get_user_info_get_0) | **GET** /api/v1/tikhub/user/get_user_info | 获取TikHub用户信息/Get TikHub user info


# **calculate_price_api_v1_tikhub_user_calculate_price_get**
> ResponseModel calculate_price_api_v1_tikhub_user_calculate_price_get(endpoint, request_per_day=request_per_day)

计算价格/Calculate price

# [中文] ### 用途: - 根据用户输入的每日请求次数以及端点信息计算最终价格。 ### 参数: - endpoint: 请求的端点，用于查询端点的原始请求单价 - request_per_day: 每日请求次数，用于计算价格，将自动根据阶梯式计费的折扣百分比计算最终价格 ### 计算公式: - 总成本 = ∑ (阶梯内请求次数 * 阶梯折后单价) - 其中，阶梯折后单价 = 基础价格 * (1 - 折扣) ### 详细计算步骤: 1. **初始化总成本**：    总成本=0 2. **遍历每个阶梯**：    * 对于每个阶梯，计算该阶梯内的请求次数。    * 计算该阶梯内的折后单价。    * 计算该阶梯内的总费用，并累加到总成本中。    * 更新剩余的请求次数。 ### 数学表示: > 设有 𝑛 个阶梯，每个阶梯的参数为： * min_rpd𝑖: 第 𝑖 个阶梯的最小请求次数 * max_rpd𝑖: 第 𝑖 个阶梯的最大请求次数 * discount𝑖: 第 𝑖 个阶梯的折扣（百分比形式） * base_price：基础价格 * request_per_day：每日请求次数 > 那么，总成本的计算公式如下： - 总成本 = Σ𝑖=1𝑛（阶梯𝑖中的请求数量 * 阶梯𝑖中的折扣单价） - 其中，阶梯折扣单价 𝑖 = base_price * (1 - 折扣𝑖/100) - 该阶梯中的请求数 𝑖 = min(request_per_day - 累计付费请求数, max_rpd𝑖 - min_rpd𝑖) ### 示例 > 假设有以下定价阶梯： * 第 1 阶梯：0 ≤ rpd < 1000，折扣 0% * 第 2 阶梯：1000 ≤ rpd < 5000，折扣 10% * 第 3 阶梯：5000 ≤ rpd < 10000，折扣 20% * 第 4 阶梯：10000 ≤ rpd < 20000，折扣 30% * 第 5 阶梯：20000 ≤ rpd < 30000，折扣 40% * 第 6 阶梯：30000 ≤ rpd，折扣 50% > 假设基础价格为 0.001 USD，每日请求次数为 12000，则计算过程如下： 1. **第 1 阶梯**（0 ≤ rpd < 1000）：    * 阶梯内请求次数=1000−0=1000    * 阶梯折后单价=0.001×(1−0/100)=0.001    * 总成本=1000×0.001=1 2. **第 2 阶梯**（1000 ≤ rpd < 5000）：    * 阶梯内请求次数=5000−1000=4000    * 阶梯折后单价=0.001×(1−10/100)=0.0009    * 总成本=4000×0.0009=3.6 3. **第 3 阶梯**（5000 ≤ rpd < 10000）：    * 阶梯内请求次数=10000−5000=5000    * 阶梯折后单价=0.001×(1−20/100)=0.0008    * 总成本=5000×0.0008=4 4. **第 4 阶梯**（10000 ≤ rpd < 20000）：    * 阶梯内请求次数=12000−10000=2000    * 阶梯折后单价=0.001×(1−30/100)=0.0007    * 总成本=2000×0.0007=1.4 5. **累加总成本**：    * 总成本=1+3.6+4+1.4=10 ### 返回: - 端点uri - 每日请求次数 - 端点原始请求单价 - 总价格 - 货币单位 - 阶梯式计费的折扣百分比信息  # [English] ### Purpose: - Calculate the final price based on the user's input of the number of daily requests and endpoint information. - Price calculation formula: Price = Number of daily requests * (Original request unit price of the endpoint * (1 - discount percentage of tiered billing)) ### Parameters: - endpoint: Requested endpoint, used to query the original request unit price of the endpoint - request_per_day: Number of daily requests, used to calculate the price, the final price will be calculated automatically based on the discount percentage of the tiered billing ### Calculation formula: - Total cost = ∑ (Number of requests in the tier * Discounted unit price in the tier) - Where, Discounted unit price in the tier = Base price * (1 - Discount) ### Detailed calculation steps: 1. **Initialize the total cost**:      Total cost = 0 2. **Traverse each tier**:         * For each tier, calculate the number of requests in the tier.         * Calculate the discounted unit price in the tier.         * Calculate the total cost in the tier and add it to the total cost.         * Update the remaining number of requests. ### Mathematical representation: Suppose there are 𝑛 tiers, and the parameters of each tier are: * min_rpd𝑖: The minimum number of requests in the 𝑖-th tier * max_rpd𝑖: The maximum number of requests in the 𝑖-th tier * discount𝑖: The discount of the 𝑖-th tier (in percentage form) * base_price: Base price * request_per_day: Number of daily requests > Then, the formula for calculating the total cost is as follows: - Total cost = ∑𝑖=1𝑛(Number of requests in the tier 𝑖 * Discounted unit price in the tier 𝑖) - Where, Discounted unit price in the tier 𝑖 = base_price * (1 - discount𝑖/100) - Number of requests in the tier 𝑖 = min(request_per_day - accumulated number of paid requests, max_rpd𝑖 - min_rpd𝑖) ### Example Suppose there are the following pricing tiers: * Tier 1: 0 ≤ rpd < 1000, discount 0% * Tier 2: 1000 ≤ rpd < 5000, discount 10% * Tier 3: 5000 ≤ rpd < 10000, discount 20% * Tier 4: 10000 ≤ rpd < 20000, discount 30% * Tier 5: 20000 ≤ rpd < 30000, discount 40% * Tier 6: 30000 ≤ rpd, discount 50% > Suppose the base price is 0.001 USD and the number of daily requests is 12000, the calculation process is as follows: 1. **Tier 1** (0 ≤ rpd < 1000):      - Number of requests in the tier 1 = 1000 - 0 = 1000      - Discounted unit price in the tier 1 = 0.001 * (1 - 0/100) = 0.001      - Total cost 1 = 1000 * 0.001 = 1 2. **Tier 2** (1000 ≤ rpd < 5000):     - Number of requests in the tier 2 = 5000 - 1000 = 4000     - Discounted unit price in the tier 2 = 0.001 * (1 - 10/100) = 0.0009     - Total cost 2 = 4000 * 0.0009 = 3.6 3. **Tier 3** (5000 ≤ rpd < 10000):     - Number of requests in the tier 3 = 10000 - 5000 = 5000     - Discounted unit price in the tier 3 = 0.001 * (1 - 20/100) = 0.0008     - Total cost 3 = 5000 * 0.0008 = 4 4. **Tier 4** (10000 ≤ rpd < 20000):     - Number of requests in the tier 4 = 12000 - 10000 = 2000     - Discounted unit price in the tier 4 = 0.001 * (1 - 30/100) = 0.0007     - Total cost 4 = 2000 * 0.0007 = 1.4 5. **Accumulated total cost**:     - Total cost = 1 + 3.6 + 4 + 1.4 = 10 ### Return: - Endpoint uri - Number of daily requests - Original request unit price of the endpoint - Total price - Currency unit - Discount percentage information of tiered billing

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
    api_instance = tikhub_sdk_v2.TikHubUserAPIApi(api_client)
    endpoint = '/api/v1/douyin/app/v1/fetch_one_video' # str | 请求的端点/Requested endpoint
request_per_day = 1 # int | 每日请求次数/Request per day (optional) (default to 1)

    try:
        # 计算价格/Calculate price
        api_response = api_instance.calculate_price_api_v1_tikhub_user_calculate_price_get(endpoint, request_per_day=request_per_day)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TikHubUserAPIApi->calculate_price_api_v1_tikhub_user_calculate_price_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | **str**| 请求的端点/Requested endpoint | 
 **request_per_day** | **int**| 每日请求次数/Request per day | [optional] [default to 1]

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

# **calculate_price_api_v1_tikhub_user_calculate_price_get_0**
> ResponseModel calculate_price_api_v1_tikhub_user_calculate_price_get_0(endpoint, request_per_day=request_per_day)

计算价格/Calculate price

# [中文] ### 用途: - 根据用户输入的每日请求次数以及端点信息计算最终价格。 ### 参数: - endpoint: 请求的端点，用于查询端点的原始请求单价 - request_per_day: 每日请求次数，用于计算价格，将自动根据阶梯式计费的折扣百分比计算最终价格 ### 计算公式: - 总成本 = ∑ (阶梯内请求次数 * 阶梯折后单价) - 其中，阶梯折后单价 = 基础价格 * (1 - 折扣) ### 详细计算步骤: 1. **初始化总成本**：    总成本=0 2. **遍历每个阶梯**：    * 对于每个阶梯，计算该阶梯内的请求次数。    * 计算该阶梯内的折后单价。    * 计算该阶梯内的总费用，并累加到总成本中。    * 更新剩余的请求次数。 ### 数学表示: > 设有 𝑛 个阶梯，每个阶梯的参数为： * min_rpd𝑖: 第 𝑖 个阶梯的最小请求次数 * max_rpd𝑖: 第 𝑖 个阶梯的最大请求次数 * discount𝑖: 第 𝑖 个阶梯的折扣（百分比形式） * base_price：基础价格 * request_per_day：每日请求次数 > 那么，总成本的计算公式如下： - 总成本 = Σ𝑖=1𝑛（阶梯𝑖中的请求数量 * 阶梯𝑖中的折扣单价） - 其中，阶梯折扣单价 𝑖 = base_price * (1 - 折扣𝑖/100) - 该阶梯中的请求数 𝑖 = min(request_per_day - 累计付费请求数, max_rpd𝑖 - min_rpd𝑖) ### 示例 > 假设有以下定价阶梯： * 第 1 阶梯：0 ≤ rpd < 1000，折扣 0% * 第 2 阶梯：1000 ≤ rpd < 5000，折扣 10% * 第 3 阶梯：5000 ≤ rpd < 10000，折扣 20% * 第 4 阶梯：10000 ≤ rpd < 20000，折扣 30% * 第 5 阶梯：20000 ≤ rpd < 30000，折扣 40% * 第 6 阶梯：30000 ≤ rpd，折扣 50% > 假设基础价格为 0.001 USD，每日请求次数为 12000，则计算过程如下： 1. **第 1 阶梯**（0 ≤ rpd < 1000）：    * 阶梯内请求次数=1000−0=1000    * 阶梯折后单价=0.001×(1−0/100)=0.001    * 总成本=1000×0.001=1 2. **第 2 阶梯**（1000 ≤ rpd < 5000）：    * 阶梯内请求次数=5000−1000=4000    * 阶梯折后单价=0.001×(1−10/100)=0.0009    * 总成本=4000×0.0009=3.6 3. **第 3 阶梯**（5000 ≤ rpd < 10000）：    * 阶梯内请求次数=10000−5000=5000    * 阶梯折后单价=0.001×(1−20/100)=0.0008    * 总成本=5000×0.0008=4 4. **第 4 阶梯**（10000 ≤ rpd < 20000）：    * 阶梯内请求次数=12000−10000=2000    * 阶梯折后单价=0.001×(1−30/100)=0.0007    * 总成本=2000×0.0007=1.4 5. **累加总成本**：    * 总成本=1+3.6+4+1.4=10 ### 返回: - 端点uri - 每日请求次数 - 端点原始请求单价 - 总价格 - 货币单位 - 阶梯式计费的折扣百分比信息  # [English] ### Purpose: - Calculate the final price based on the user's input of the number of daily requests and endpoint information. - Price calculation formula: Price = Number of daily requests * (Original request unit price of the endpoint * (1 - discount percentage of tiered billing)) ### Parameters: - endpoint: Requested endpoint, used to query the original request unit price of the endpoint - request_per_day: Number of daily requests, used to calculate the price, the final price will be calculated automatically based on the discount percentage of the tiered billing ### Calculation formula: - Total cost = ∑ (Number of requests in the tier * Discounted unit price in the tier) - Where, Discounted unit price in the tier = Base price * (1 - Discount) ### Detailed calculation steps: 1. **Initialize the total cost**:      Total cost = 0 2. **Traverse each tier**:         * For each tier, calculate the number of requests in the tier.         * Calculate the discounted unit price in the tier.         * Calculate the total cost in the tier and add it to the total cost.         * Update the remaining number of requests. ### Mathematical representation: Suppose there are 𝑛 tiers, and the parameters of each tier are: * min_rpd𝑖: The minimum number of requests in the 𝑖-th tier * max_rpd𝑖: The maximum number of requests in the 𝑖-th tier * discount𝑖: The discount of the 𝑖-th tier (in percentage form) * base_price: Base price * request_per_day: Number of daily requests > Then, the formula for calculating the total cost is as follows: - Total cost = ∑𝑖=1𝑛(Number of requests in the tier 𝑖 * Discounted unit price in the tier 𝑖) - Where, Discounted unit price in the tier 𝑖 = base_price * (1 - discount𝑖/100) - Number of requests in the tier 𝑖 = min(request_per_day - accumulated number of paid requests, max_rpd𝑖 - min_rpd𝑖) ### Example Suppose there are the following pricing tiers: * Tier 1: 0 ≤ rpd < 1000, discount 0% * Tier 2: 1000 ≤ rpd < 5000, discount 10% * Tier 3: 5000 ≤ rpd < 10000, discount 20% * Tier 4: 10000 ≤ rpd < 20000, discount 30% * Tier 5: 20000 ≤ rpd < 30000, discount 40% * Tier 6: 30000 ≤ rpd, discount 50% > Suppose the base price is 0.001 USD and the number of daily requests is 12000, the calculation process is as follows: 1. **Tier 1** (0 ≤ rpd < 1000):      - Number of requests in the tier 1 = 1000 - 0 = 1000      - Discounted unit price in the tier 1 = 0.001 * (1 - 0/100) = 0.001      - Total cost 1 = 1000 * 0.001 = 1 2. **Tier 2** (1000 ≤ rpd < 5000):     - Number of requests in the tier 2 = 5000 - 1000 = 4000     - Discounted unit price in the tier 2 = 0.001 * (1 - 10/100) = 0.0009     - Total cost 2 = 4000 * 0.0009 = 3.6 3. **Tier 3** (5000 ≤ rpd < 10000):     - Number of requests in the tier 3 = 10000 - 5000 = 5000     - Discounted unit price in the tier 3 = 0.001 * (1 - 20/100) = 0.0008     - Total cost 3 = 5000 * 0.0008 = 4 4. **Tier 4** (10000 ≤ rpd < 20000):     - Number of requests in the tier 4 = 12000 - 10000 = 2000     - Discounted unit price in the tier 4 = 0.001 * (1 - 30/100) = 0.0007     - Total cost 4 = 2000 * 0.0007 = 1.4 5. **Accumulated total cost**:     - Total cost = 1 + 3.6 + 4 + 1.4 = 10 ### Return: - Endpoint uri - Number of daily requests - Original request unit price of the endpoint - Total price - Currency unit - Discount percentage information of tiered billing

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
    api_instance = tikhub_sdk_v2.TikHubUserAPIApi(api_client)
    endpoint = '/api/v1/douyin/app/v1/fetch_one_video' # str | 请求的端点/Requested endpoint
request_per_day = 1 # int | 每日请求次数/Request per day (optional) (default to 1)

    try:
        # 计算价格/Calculate price
        api_response = api_instance.calculate_price_api_v1_tikhub_user_calculate_price_get_0(endpoint, request_per_day=request_per_day)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TikHubUserAPIApi->calculate_price_api_v1_tikhub_user_calculate_price_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | **str**| 请求的端点/Requested endpoint | 
 **request_per_day** | **int**| 每日请求次数/Request per day | [optional] [default to 1]

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

# **get_all_endpoints_info_api_v1_tikhub_user_get_all_endpoints_info_get**
> ResponseModel get_all_endpoints_info_api_v1_tikhub_user_get_all_endpoints_info_get()

获取所有端点信息/Get all endpoints information

# [中文] ### 用途: - 获取所有端点信息 ### 返回: - 所有端点信息  # [English] ### Purpose: - Get all endpoints information ### Return: - All endpoints information

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
    api_instance = tikhub_sdk_v2.TikHubUserAPIApi(api_client)
    
    try:
        # 获取所有端点信息/Get all endpoints information
        api_response = api_instance.get_all_endpoints_info_api_v1_tikhub_user_get_all_endpoints_info_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TikHubUserAPIApi->get_all_endpoints_info_api_v1_tikhub_user_get_all_endpoints_info_get: %s\n" % e)
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

# **get_all_endpoints_info_api_v1_tikhub_user_get_all_endpoints_info_get_0**
> ResponseModel get_all_endpoints_info_api_v1_tikhub_user_get_all_endpoints_info_get_0()

获取所有端点信息/Get all endpoints information

# [中文] ### 用途: - 获取所有端点信息 ### 返回: - 所有端点信息  # [English] ### Purpose: - Get all endpoints information ### Return: - All endpoints information

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
    api_instance = tikhub_sdk_v2.TikHubUserAPIApi(api_client)
    
    try:
        # 获取所有端点信息/Get all endpoints information
        api_response = api_instance.get_all_endpoints_info_api_v1_tikhub_user_get_all_endpoints_info_get_0()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TikHubUserAPIApi->get_all_endpoints_info_api_v1_tikhub_user_get_all_endpoints_info_get_0: %s\n" % e)
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

# **get_endpoint_info_api_v1_tikhub_user_get_endpoint_info_get**
> ResponseModel get_endpoint_info_api_v1_tikhub_user_get_endpoint_info_get(endpoint)

获取一个端点的信息/Get information of an endpoint

# [中文] ### 用途: - 获取一个端点的信息 ### 参数: - endpoint: 请求的端点 ### 返回: - 端点信息  # [English] ### Purpose: - Get information of an endpoint ### Parameters: - endpoint: Requested endpoint ### Return: - Endpoint information

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
    api_instance = tikhub_sdk_v2.TikHubUserAPIApi(api_client)
    endpoint = '/api/v1/douyin/app/v1/fetch_one_video' # str | 请求的端点/Requested endpoint

    try:
        # 获取一个端点的信息/Get information of an endpoint
        api_response = api_instance.get_endpoint_info_api_v1_tikhub_user_get_endpoint_info_get(endpoint)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TikHubUserAPIApi->get_endpoint_info_api_v1_tikhub_user_get_endpoint_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | **str**| 请求的端点/Requested endpoint | 

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

# **get_endpoint_info_api_v1_tikhub_user_get_endpoint_info_get_0**
> ResponseModel get_endpoint_info_api_v1_tikhub_user_get_endpoint_info_get_0(endpoint)

获取一个端点的信息/Get information of an endpoint

# [中文] ### 用途: - 获取一个端点的信息 ### 参数: - endpoint: 请求的端点 ### 返回: - 端点信息  # [English] ### Purpose: - Get information of an endpoint ### Parameters: - endpoint: Requested endpoint ### Return: - Endpoint information

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
    api_instance = tikhub_sdk_v2.TikHubUserAPIApi(api_client)
    endpoint = '/api/v1/douyin/app/v1/fetch_one_video' # str | 请求的端点/Requested endpoint

    try:
        # 获取一个端点的信息/Get information of an endpoint
        api_response = api_instance.get_endpoint_info_api_v1_tikhub_user_get_endpoint_info_get_0(endpoint)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TikHubUserAPIApi->get_endpoint_info_api_v1_tikhub_user_get_endpoint_info_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | **str**| 请求的端点/Requested endpoint | 

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

# **get_tiered_discount_info_api_v1_tikhub_user_get_tiered_discount_info_get**
> ResponseModel get_tiered_discount_info_api_v1_tikhub_user_get_tiered_discount_info_get()

获取阶梯式折扣百分比信息/Get tiered discount percentage information

# [中文] ### 用途: - 获取阶梯式折扣百分比信息 ### 返回: - 阶梯式折扣百分比信息  # [English] ### Purpose: - Get tiered discount percentage information ### Return: - Tiered discount percentage information

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
    api_instance = tikhub_sdk_v2.TikHubUserAPIApi(api_client)
    
    try:
        # 获取阶梯式折扣百分比信息/Get tiered discount percentage information
        api_response = api_instance.get_tiered_discount_info_api_v1_tikhub_user_get_tiered_discount_info_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TikHubUserAPIApi->get_tiered_discount_info_api_v1_tikhub_user_get_tiered_discount_info_get: %s\n" % e)
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

# **get_tiered_discount_info_api_v1_tikhub_user_get_tiered_discount_info_get_0**
> ResponseModel get_tiered_discount_info_api_v1_tikhub_user_get_tiered_discount_info_get_0()

获取阶梯式折扣百分比信息/Get tiered discount percentage information

# [中文] ### 用途: - 获取阶梯式折扣百分比信息 ### 返回: - 阶梯式折扣百分比信息  # [English] ### Purpose: - Get tiered discount percentage information ### Return: - Tiered discount percentage information

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
    api_instance = tikhub_sdk_v2.TikHubUserAPIApi(api_client)
    
    try:
        # 获取阶梯式折扣百分比信息/Get tiered discount percentage information
        api_response = api_instance.get_tiered_discount_info_api_v1_tikhub_user_get_tiered_discount_info_get_0()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TikHubUserAPIApi->get_tiered_discount_info_api_v1_tikhub_user_get_tiered_discount_info_get_0: %s\n" % e)
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

# **get_user_daily_usage_api_v1_tikhub_user_get_user_daily_usage_get**
> ResponseModel get_user_daily_usage_api_v1_tikhub_user_get_user_daily_usage_get()

获取用户每日使用情况/Get user daily usage

# [中文] ### 用途: - 请求头中携带API Key请求此端点可以查询当前账户每日使用情况。 ### 参数: - 请求头：{'Authorization': 'Bearer API Key'} ### 返回: - 用户每日使用情况  # [English] ### Purpose: - Request this endpoint with API Key in the header to query the current account daily usage. ### Parameters: - Headers: {'Authorization': 'Bearer API Key'} ### Return: - User daily usage

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
    api_instance = tikhub_sdk_v2.TikHubUserAPIApi(api_client)
    
    try:
        # 获取用户每日使用情况/Get user daily usage
        api_response = api_instance.get_user_daily_usage_api_v1_tikhub_user_get_user_daily_usage_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TikHubUserAPIApi->get_user_daily_usage_api_v1_tikhub_user_get_user_daily_usage_get: %s\n" % e)
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

# **get_user_daily_usage_api_v1_tikhub_user_get_user_daily_usage_get_0**
> ResponseModel get_user_daily_usage_api_v1_tikhub_user_get_user_daily_usage_get_0()

获取用户每日使用情况/Get user daily usage

# [中文] ### 用途: - 请求头中携带API Key请求此端点可以查询当前账户每日使用情况。 ### 参数: - 请求头：{'Authorization': 'Bearer API Key'} ### 返回: - 用户每日使用情况  # [English] ### Purpose: - Request this endpoint with API Key in the header to query the current account daily usage. ### Parameters: - Headers: {'Authorization': 'Bearer API Key'} ### Return: - User daily usage

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
    api_instance = tikhub_sdk_v2.TikHubUserAPIApi(api_client)
    
    try:
        # 获取用户每日使用情况/Get user daily usage
        api_response = api_instance.get_user_daily_usage_api_v1_tikhub_user_get_user_daily_usage_get_0()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TikHubUserAPIApi->get_user_daily_usage_api_v1_tikhub_user_get_user_daily_usage_get_0: %s\n" % e)
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

# **get_user_info_api_v1_tikhub_user_get_user_info_get**
> UserInfoResponseModel get_user_info_api_v1_tikhub_user_get_user_info_get()

获取TikHub用户信息/Get TikHub user info

# [中文] ### 用途: - 请求头中携带API Key请求此端点可以查询当前账户信息。 ### 参数: - 请求头：{'Authorization': 'Bearer API_KEY'} ### 返回: - 用户信息  # [English] ### Purpose: - Request this endpoint with API Key in the header to query the current account information. ### Parameters: - Headers: {'Authorization': 'Bearer API_KEY'} ### Return: - User information  # [示例/Example] ```python response = {       \"code\": 200,       \"router\": \"/api/v1/tikhub/user/get_user_info\",       \"api_key_data\": {         \"api_key_name\": \"Develop Test\",         \"api_key_scopes\": [           \"/api/v1/tikhub/user/\"         ],         \"created_at\": \"2024-05-22T06:07:12.495520\",         \"expires_at\": null,         \"api_key_status\": 1       },       \"user_data\": {         \"email\": \"example@example.com\",         \"balance\": 100,         \"free_credit\": 100,         \"email_verified\": true,         \"account_disabled\": false,         \"is_active\": true       }     } ```

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
    api_instance = tikhub_sdk_v2.TikHubUserAPIApi(api_client)
    
    try:
        # 获取TikHub用户信息/Get TikHub user info
        api_response = api_instance.get_user_info_api_v1_tikhub_user_get_user_info_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TikHubUserAPIApi->get_user_info_api_v1_tikhub_user_get_user_info_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserInfoResponseModel**](UserInfoResponseModel.md)

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

# **get_user_info_api_v1_tikhub_user_get_user_info_get_0**
> UserInfoResponseModel get_user_info_api_v1_tikhub_user_get_user_info_get_0()

获取TikHub用户信息/Get TikHub user info

# [中文] ### 用途: - 请求头中携带API Key请求此端点可以查询当前账户信息。 ### 参数: - 请求头：{'Authorization': 'Bearer API_KEY'} ### 返回: - 用户信息  # [English] ### Purpose: - Request this endpoint with API Key in the header to query the current account information. ### Parameters: - Headers: {'Authorization': 'Bearer API_KEY'} ### Return: - User information  # [示例/Example] ```python response = {       \"code\": 200,       \"router\": \"/api/v1/tikhub/user/get_user_info\",       \"api_key_data\": {         \"api_key_name\": \"Develop Test\",         \"api_key_scopes\": [           \"/api/v1/tikhub/user/\"         ],         \"created_at\": \"2024-05-22T06:07:12.495520\",         \"expires_at\": null,         \"api_key_status\": 1       },       \"user_data\": {         \"email\": \"example@example.com\",         \"balance\": 100,         \"free_credit\": 100,         \"email_verified\": true,         \"account_disabled\": false,         \"is_active\": true       }     } ```

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
    api_instance = tikhub_sdk_v2.TikHubUserAPIApi(api_client)
    
    try:
        # 获取TikHub用户信息/Get TikHub user info
        api_response = api_instance.get_user_info_api_v1_tikhub_user_get_user_info_get_0()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TikHubUserAPIApi->get_user_info_api_v1_tikhub_user_get_user_info_get_0: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserInfoResponseModel**](UserInfoResponseModel.md)

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

