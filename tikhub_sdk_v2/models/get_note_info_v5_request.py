# coding: utf-8

"""
    TikHub.io - Your Ultimate Social Media Data & API Marketplace

    High-performance asynchronous Douyin(抖音) TikTok Xiaohongshu(小红书) Kuaishou(快手) Weibo(微博) Instagram YouTube(油管) Twitter(X) Captcha Solver(验证码解决器) Temp Mail(临时邮箱) API(接口).  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from tikhub_sdk_v2.configuration import Configuration


class GetNoteInfoV5Request(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'note_id': 'str',
        'xsec_token': 'str',
        'cookie': 'str',
        'proxy': 'str'
    }

    attribute_map = {
        'note_id': 'note_id',
        'xsec_token': 'xsec_token',
        'cookie': 'cookie',
        'proxy': 'proxy'
    }

    def __init__(self, note_id='67855d09000000001703d449', xsec_token='ABfpRSESmZDRbX-EX7lzEztktMngxPVC9kU-dgQmuQoNo=', cookie='', proxy='', local_vars_configuration=None):  # noqa: E501
        """GetNoteInfoV5Request - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._note_id = None
        self._xsec_token = None
        self._cookie = None
        self._proxy = None
        self.discriminator = None

        if note_id is not None:
            self.note_id = note_id
        if xsec_token is not None:
            self.xsec_token = xsec_token
        if cookie is not None:
            self.cookie = cookie
        if proxy is not None:
            self.proxy = proxy

    @property
    def note_id(self):
        """Gets the note_id of this GetNoteInfoV5Request.  # noqa: E501

        Note Id，笔记ID/Note ID  # noqa: E501

        :return: The note_id of this GetNoteInfoV5Request.  # noqa: E501
        :rtype: str
        """
        return self._note_id

    @note_id.setter
    def note_id(self, note_id):
        """Sets the note_id of this GetNoteInfoV5Request.

        Note Id，笔记ID/Note ID  # noqa: E501

        :param note_id: The note_id of this GetNoteInfoV5Request.  # noqa: E501
        :type: str
        """

        self._note_id = note_id

    @property
    def xsec_token(self):
        """Gets the xsec_token of this GetNoteInfoV5Request.  # noqa: E501

        Xsec Token，X-Sec-Token，可以从搜索接口中获取/X-Sec-Token, can be obtained from the search interface  # noqa: E501

        :return: The xsec_token of this GetNoteInfoV5Request.  # noqa: E501
        :rtype: str
        """
        return self._xsec_token

    @xsec_token.setter
    def xsec_token(self, xsec_token):
        """Sets the xsec_token of this GetNoteInfoV5Request.

        Xsec Token，X-Sec-Token，可以从搜索接口中获取/X-Sec-Token, can be obtained from the search interface  # noqa: E501

        :param xsec_token: The xsec_token of this GetNoteInfoV5Request.  # noqa: E501
        :type: str
        """

        self._xsec_token = xsec_token

    @property
    def cookie(self):
        """Gets the cookie of this GetNoteInfoV5Request.  # noqa: E501

        Cookie，用户自行提供的已登录的网页Cookie/User provided logged-in web Cookie  # noqa: E501

        :return: The cookie of this GetNoteInfoV5Request.  # noqa: E501
        :rtype: str
        """
        return self._cookie

    @cookie.setter
    def cookie(self, cookie):
        """Sets the cookie of this GetNoteInfoV5Request.

        Cookie，用户自行提供的已登录的网页Cookie/User provided logged-in web Cookie  # noqa: E501

        :param cookie: The cookie of this GetNoteInfoV5Request.  # noqa: E501
        :type: str
        """

        self._cookie = cookie

    @property
    def proxy(self):
        """Gets the proxy of this GetNoteInfoV5Request.  # noqa: E501

        Proxy，代理，格式：http://用户名:密码@IP:端口/Proxy, format: http://username:password@IP:port  # noqa: E501

        :return: The proxy of this GetNoteInfoV5Request.  # noqa: E501
        :rtype: str
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this GetNoteInfoV5Request.

        Proxy，代理，格式：http://用户名:密码@IP:端口/Proxy, format: http://username:password@IP:port  # noqa: E501

        :param proxy: The proxy of this GetNoteInfoV5Request.  # noqa: E501
        :type: str
        """

        self._proxy = proxy

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetNoteInfoV5Request):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetNoteInfoV5Request):
            return True

        return self.to_dict() != other.to_dict()
