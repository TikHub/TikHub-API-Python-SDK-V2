# ReplyCommentRequest

ReplyCommentRequest
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aweme_id** | **str** | AKA Video ID，Video ID, which can be obtained from the sharing link, for example: https://www.tiktok.com/@username/video/7419966340443819295 | [optional] [default to '7419966340443819295']
**reply_id** | **str** | Reply Comment ID AKA CID，Comment ID, which can be obtained from the comment data of the specified video. | [optional] [default to '7420673787547419435']
**text** | **str** | Comment Content，Comment content, TikTok comment content needs to comply with the specifications, do not contain illegal keywords, otherwise, even if the request is successful, it will be judged as spam comments by the system and will not be displayed. | [optional] [default to 'Hello, TikTok!']
**cookie** | **str** | User Cookie，User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie information, please use URL-encoded Cookie string when submitting. | [optional] [default to 'Your_Cookie_From_Browser']
**device_id** | **str** | Device ID，Device id, optional, if not filled in, it will be automatically generated, if you need to customize the device id, please use the device information interface to get the device id. | [optional] [default to '']
**iid** | **str** | Device Install ID，Device install id, optional, if not filled in, it will be automatically generated, if you need to customize the device iid, please use the device information interface to get the device iid. | [optional] [default to '']
**proxy** | **str** | Proxy IP，Proxy IP, optional, if not filled in, it will be automatically generated, if you need to customize the proxy IP, please use the proxy IP interface to get the proxy IP. | [optional] [default to '']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


