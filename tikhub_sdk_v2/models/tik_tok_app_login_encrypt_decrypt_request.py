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


class TikTokAppLoginEncryptDecryptRequest(object):
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
        'username': 'str',
        'password': 'str',
        'mode': 'ModeEnum'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'mode': 'mode'
    }

    def __init__(self, username='example_username', password='example_password', mode=None, local_vars_configuration=None):  # noqa: E501
        """TikTokAppLoginEncryptDecryptRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._username = None
        self._password = None
        self._mode = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if mode is not None:
            self.mode = mode

    @property
    def username(self):
        """Gets the username of this TikTokAppLoginEncryptDecryptRequest.  # noqa: E501

        Username，Plaintext or encrypted username  # noqa: E501

        :return: The username of this TikTokAppLoginEncryptDecryptRequest.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this TikTokAppLoginEncryptDecryptRequest.

        Username，Plaintext or encrypted username  # noqa: E501

        :param username: The username of this TikTokAppLoginEncryptDecryptRequest.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this TikTokAppLoginEncryptDecryptRequest.  # noqa: E501

        Password，Plaintext or encrypted password  # noqa: E501

        :return: The password of this TikTokAppLoginEncryptDecryptRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this TikTokAppLoginEncryptDecryptRequest.

        Password，Plaintext or encrypted password  # noqa: E501

        :param password: The password of this TikTokAppLoginEncryptDecryptRequest.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def mode(self):
        """Gets the mode of this TikTokAppLoginEncryptDecryptRequest.  # noqa: E501

        Encrypt or decrypt the input string  # noqa: E501

        :return: The mode of this TikTokAppLoginEncryptDecryptRequest.  # noqa: E501
        :rtype: ModeEnum
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this TikTokAppLoginEncryptDecryptRequest.

        Encrypt or decrypt the input string  # noqa: E501

        :param mode: The mode of this TikTokAppLoginEncryptDecryptRequest.  # noqa: E501
        :type: ModeEnum
        """

        self._mode = mode

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
        if not isinstance(other, TikTokAppLoginEncryptDecryptRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TikTokAppLoginEncryptDecryptRequest):
            return True

        return self.to_dict() != other.to_dict()
