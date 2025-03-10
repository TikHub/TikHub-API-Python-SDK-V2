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


class BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost(object):
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
        'app_id': 'str',
        'url': 'str',
        'proxy': 'object'
    }

    attribute_map = {
        'app_id': 'app_id',
        'url': 'url',
        'proxy': 'proxy'
    }

    def __init__(self, app_id=None, url=None, proxy=None, local_vars_configuration=None):  # noqa: E501
        """BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._app_id = None
        self._url = None
        self._proxy = None
        self.discriminator = None

        self.app_id = app_id
        self.url = url
        if proxy is not None:
            self.proxy = proxy

    @property
    def app_id(self):
        """Gets the app_id of this BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost.  # noqa: E501

        App Id，App ID  # noqa: E501

        :return: The app_id of this BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost.

        App Id，App ID  # noqa: E501

        :param app_id: The app_id of this BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and app_id is None:  # noqa: E501
            raise ValueError("Invalid value for `app_id`, must not be `None`")  # noqa: E501

        self._app_id = app_id

    @property
    def url(self):
        """Gets the url of this BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost.  # noqa: E501

        Url，URL  # noqa: E501

        :return: The url of this BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost.

        Url，URL  # noqa: E501

        :param url: The url of this BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def proxy(self):
        """Gets the proxy of this BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost.  # noqa: E501

        Proxy，Proxy  # noqa: E501

        :return: The proxy of this BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost.  # noqa: E501
        :rtype: object
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost.

        Proxy，Proxy  # noqa: E501

        :param proxy: The proxy of this BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost.  # noqa: E501
        :type: object
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
        if not isinstance(other, BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost):
            return True

        return self.to_dict() != other.to_dict()
