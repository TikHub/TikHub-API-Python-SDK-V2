# BodyFetchHotAccountListApiV1DouyinBillboardFetchHotAccountListPost

Body_fetch_hot_account_list_api_v1_douyin_billboard_fetch_hot_account_list_post
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_window** | **str** | Date Window，时间窗口，格式 小时，默认24小时 | [optional] [default to '24']
**page_num** | **str** | Page Num，页码，默认1 | [optional] [default to '1']
**page_size** | **str** | Page Size，每页数量，默认10 | [optional] [default to '10']
**query_tag** | [**object**](.md) | Query Tag，子级垂类标签，空则为全部，多个标签需传入{\&quot;value\&quot;: \&quot;{顶级垂类标签id}\&quot;, \&quot;children\&quot;: [{\&quot;value\&quot;: \&quot;{子级垂类标签id}\&quot;}, {\&quot;value\&quot;: \&quot;{子级垂类标签id}\&quot;}]} | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


