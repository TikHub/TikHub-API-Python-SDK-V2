# coding: utf-8

"""
    TikHub.io - Your Ultimate Social Media Data & API Marketplace

    High-performance asynchronous Douyin(抖音) TikTok Xiaohongshu(小红书) Kuaishou(快手) Weibo(微博) Instagram YouTube(油管) Twitter(X) Captcha Solver(验证码解决器) Temp Mail(临时邮箱) API(接口).  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tikhub_sdk_v2.api_client import ApiClient
from tikhub_sdk_v2.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ToutiaoWebAPIApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_article_info_api_v1_toutiao_web_get_article_info_get(self, aweme_id, **kwargs):  # noqa: E501
        """获取指定文章的信息/Get information of specified article  # noqa: E501

        # [中文] ### 用途: - 获取指定文章的信息 ### 参数: - aweme_id: 作品ID，可以从链接中获取     - 例如: https://www.toutiao.com/article/7450114952884503059/ ### 返回: - 作品信息  # [English] ### Purpose: - Get information of specified post ### Parameters: - item_id: Post ID, can be obtained from the link     - For example: https://www.toutiao.com/article/7450114952884503059/ ### Return: - Post information  # [示例/Example] aweme_id = \"7450114952884503059\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_article_info_api_v1_toutiao_web_get_article_info_get(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str aweme_id: 作品ID/Post ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_article_info_api_v1_toutiao_web_get_article_info_get_with_http_info(aweme_id, **kwargs)  # noqa: E501

    def get_article_info_api_v1_toutiao_web_get_article_info_get_with_http_info(self, aweme_id, **kwargs):  # noqa: E501
        """获取指定文章的信息/Get information of specified article  # noqa: E501

        # [中文] ### 用途: - 获取指定文章的信息 ### 参数: - aweme_id: 作品ID，可以从链接中获取     - 例如: https://www.toutiao.com/article/7450114952884503059/ ### 返回: - 作品信息  # [English] ### Purpose: - Get information of specified post ### Parameters: - item_id: Post ID, can be obtained from the link     - For example: https://www.toutiao.com/article/7450114952884503059/ ### Return: - Post information  # [示例/Example] aweme_id = \"7450114952884503059\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_article_info_api_v1_toutiao_web_get_article_info_get_with_http_info(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str aweme_id: 作品ID/Post ID (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ResponseModel, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'aweme_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_article_info_api_v1_toutiao_web_get_article_info_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'aweme_id' is set
        if self.api_client.client_side_validation and ('aweme_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['aweme_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `aweme_id` when calling `get_article_info_api_v1_toutiao_web_get_article_info_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'aweme_id' in local_var_params and local_var_params['aweme_id'] is not None:  # noqa: E501
            query_params.append(('aweme_id', local_var_params['aweme_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/toutiao/web/get_article_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_article_info_api_v1_toutiao_web_get_article_info_get_0(self, aweme_id, **kwargs):  # noqa: E501
        """获取指定文章的信息/Get information of specified article  # noqa: E501

        # [中文] ### 用途: - 获取指定文章的信息 ### 参数: - aweme_id: 作品ID，可以从链接中获取     - 例如: https://www.toutiao.com/article/7450114952884503059/ ### 返回: - 作品信息  # [English] ### Purpose: - Get information of specified post ### Parameters: - item_id: Post ID, can be obtained from the link     - For example: https://www.toutiao.com/article/7450114952884503059/ ### Return: - Post information  # [示例/Example] aweme_id = \"7450114952884503059\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_article_info_api_v1_toutiao_web_get_article_info_get_0(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str aweme_id: 作品ID/Post ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_article_info_api_v1_toutiao_web_get_article_info_get_0_with_http_info(aweme_id, **kwargs)  # noqa: E501

    def get_article_info_api_v1_toutiao_web_get_article_info_get_0_with_http_info(self, aweme_id, **kwargs):  # noqa: E501
        """获取指定文章的信息/Get information of specified article  # noqa: E501

        # [中文] ### 用途: - 获取指定文章的信息 ### 参数: - aweme_id: 作品ID，可以从链接中获取     - 例如: https://www.toutiao.com/article/7450114952884503059/ ### 返回: - 作品信息  # [English] ### Purpose: - Get information of specified post ### Parameters: - item_id: Post ID, can be obtained from the link     - For example: https://www.toutiao.com/article/7450114952884503059/ ### Return: - Post information  # [示例/Example] aweme_id = \"7450114952884503059\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_article_info_api_v1_toutiao_web_get_article_info_get_0_with_http_info(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str aweme_id: 作品ID/Post ID (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ResponseModel, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'aweme_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_article_info_api_v1_toutiao_web_get_article_info_get_0" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'aweme_id' is set
        if self.api_client.client_side_validation and ('aweme_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['aweme_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `aweme_id` when calling `get_article_info_api_v1_toutiao_web_get_article_info_get_0`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'aweme_id' in local_var_params and local_var_params['aweme_id'] is not None:  # noqa: E501
            query_params.append(('aweme_id', local_var_params['aweme_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/toutiao/web/get_article_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_video_info_api_v1_toutiao_web_get_video_info_get(self, aweme_id, **kwargs):  # noqa: E501
        """获取指定视频的信息/Get information of specified video  # noqa: E501

        # [中文] ### 用途: - 获取指定视频的信息 ### 参数: - aweme_id: 作品ID，可以从链接中获取     - 例如: https://www.toutiao.com/video/7431543350882206242/ ### 返回: - 作品信息  # [English] ### Purpose: - Get information of specified video ### Parameters: - item_id: Post ID, can be obtained from the link     - For example: https://www.toutiao.com/video/7431543350882206242/ ### Return: - Post information  # [示例/Example] aweme_id = \"7431543350882206242\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_video_info_api_v1_toutiao_web_get_video_info_get(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str aweme_id: 作品ID/Post ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_video_info_api_v1_toutiao_web_get_video_info_get_with_http_info(aweme_id, **kwargs)  # noqa: E501

    def get_video_info_api_v1_toutiao_web_get_video_info_get_with_http_info(self, aweme_id, **kwargs):  # noqa: E501
        """获取指定视频的信息/Get information of specified video  # noqa: E501

        # [中文] ### 用途: - 获取指定视频的信息 ### 参数: - aweme_id: 作品ID，可以从链接中获取     - 例如: https://www.toutiao.com/video/7431543350882206242/ ### 返回: - 作品信息  # [English] ### Purpose: - Get information of specified video ### Parameters: - item_id: Post ID, can be obtained from the link     - For example: https://www.toutiao.com/video/7431543350882206242/ ### Return: - Post information  # [示例/Example] aweme_id = \"7431543350882206242\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_video_info_api_v1_toutiao_web_get_video_info_get_with_http_info(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str aweme_id: 作品ID/Post ID (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ResponseModel, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'aweme_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_video_info_api_v1_toutiao_web_get_video_info_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'aweme_id' is set
        if self.api_client.client_side_validation and ('aweme_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['aweme_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `aweme_id` when calling `get_video_info_api_v1_toutiao_web_get_video_info_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'aweme_id' in local_var_params and local_var_params['aweme_id'] is not None:  # noqa: E501
            query_params.append(('aweme_id', local_var_params['aweme_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/toutiao/web/get_video_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_video_info_api_v1_toutiao_web_get_video_info_get_0(self, aweme_id, **kwargs):  # noqa: E501
        """获取指定视频的信息/Get information of specified video  # noqa: E501

        # [中文] ### 用途: - 获取指定视频的信息 ### 参数: - aweme_id: 作品ID，可以从链接中获取     - 例如: https://www.toutiao.com/video/7431543350882206242/ ### 返回: - 作品信息  # [English] ### Purpose: - Get information of specified video ### Parameters: - item_id: Post ID, can be obtained from the link     - For example: https://www.toutiao.com/video/7431543350882206242/ ### Return: - Post information  # [示例/Example] aweme_id = \"7431543350882206242\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_video_info_api_v1_toutiao_web_get_video_info_get_0(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str aweme_id: 作品ID/Post ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_video_info_api_v1_toutiao_web_get_video_info_get_0_with_http_info(aweme_id, **kwargs)  # noqa: E501

    def get_video_info_api_v1_toutiao_web_get_video_info_get_0_with_http_info(self, aweme_id, **kwargs):  # noqa: E501
        """获取指定视频的信息/Get information of specified video  # noqa: E501

        # [中文] ### 用途: - 获取指定视频的信息 ### 参数: - aweme_id: 作品ID，可以从链接中获取     - 例如: https://www.toutiao.com/video/7431543350882206242/ ### 返回: - 作品信息  # [English] ### Purpose: - Get information of specified video ### Parameters: - item_id: Post ID, can be obtained from the link     - For example: https://www.toutiao.com/video/7431543350882206242/ ### Return: - Post information  # [示例/Example] aweme_id = \"7431543350882206242\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_video_info_api_v1_toutiao_web_get_video_info_get_0_with_http_info(aweme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str aweme_id: 作品ID/Post ID (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ResponseModel, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'aweme_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_video_info_api_v1_toutiao_web_get_video_info_get_0" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'aweme_id' is set
        if self.api_client.client_side_validation and ('aweme_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['aweme_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `aweme_id` when calling `get_video_info_api_v1_toutiao_web_get_video_info_get_0`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'aweme_id' in local_var_params and local_var_params['aweme_id'] is not None:  # noqa: E501
            query_params.append(('aweme_id', local_var_params['aweme_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/toutiao/web/get_video_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
