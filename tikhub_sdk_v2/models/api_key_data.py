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


class ApiKeyData(object):
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
        'api_key_name': 'str',
        'api_key_scopes': 'list[str]',
        'created_at': 'datetime',
        'expires_at': 'AnyOfDateTimenull',
        'api_key_status': 'int'
    }

    attribute_map = {
        'api_key_name': 'api_key_name',
        'api_key_scopes': 'api_key_scopes',
        'created_at': 'created_at',
        'expires_at': 'expires_at',
        'api_key_status': 'api_key_status'
    }

    def __init__(self, api_key_name=None, api_key_scopes=None, created_at=None, expires_at=None, api_key_status=None, local_vars_configuration=None):  # noqa: E501
        """ApiKeyData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_key_name = None
        self._api_key_scopes = None
        self._created_at = None
        self._expires_at = None
        self._api_key_status = None
        self.discriminator = None

        self.api_key_name = api_key_name
        self.api_key_scopes = api_key_scopes
        self.created_at = created_at
        self.expires_at = expires_at
        self.api_key_status = api_key_status

    @property
    def api_key_name(self):
        """Gets the api_key_name of this ApiKeyData.  # noqa: E501

        Api Key Name  # noqa: E501

        :return: The api_key_name of this ApiKeyData.  # noqa: E501
        :rtype: str
        """
        return self._api_key_name

    @api_key_name.setter
    def api_key_name(self, api_key_name):
        """Sets the api_key_name of this ApiKeyData.

        Api Key Name  # noqa: E501

        :param api_key_name: The api_key_name of this ApiKeyData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and api_key_name is None:  # noqa: E501
            raise ValueError("Invalid value for `api_key_name`, must not be `None`")  # noqa: E501

        self._api_key_name = api_key_name

    @property
    def api_key_scopes(self):
        """Gets the api_key_scopes of this ApiKeyData.  # noqa: E501

        Api Key Scopes  # noqa: E501

        :return: The api_key_scopes of this ApiKeyData.  # noqa: E501
        :rtype: list[str]
        """
        return self._api_key_scopes

    @api_key_scopes.setter
    def api_key_scopes(self, api_key_scopes):
        """Sets the api_key_scopes of this ApiKeyData.

        Api Key Scopes  # noqa: E501

        :param api_key_scopes: The api_key_scopes of this ApiKeyData.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and api_key_scopes is None:  # noqa: E501
            raise ValueError("Invalid value for `api_key_scopes`, must not be `None`")  # noqa: E501

        self._api_key_scopes = api_key_scopes

    @property
    def created_at(self):
        """Gets the created_at of this ApiKeyData.  # noqa: E501

        Created At  # noqa: E501

        :return: The created_at of this ApiKeyData.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ApiKeyData.

        Created At  # noqa: E501

        :param created_at: The created_at of this ApiKeyData.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def expires_at(self):
        """Gets the expires_at of this ApiKeyData.  # noqa: E501

        Expires At  # noqa: E501

        :return: The expires_at of this ApiKeyData.  # noqa: E501
        :rtype: AnyOfDateTimenull
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this ApiKeyData.

        Expires At  # noqa: E501

        :param expires_at: The expires_at of this ApiKeyData.  # noqa: E501
        :type: AnyOfDateTimenull
        """
        if self.local_vars_configuration.client_side_validation and expires_at is None:  # noqa: E501
            raise ValueError("Invalid value for `expires_at`, must not be `None`")  # noqa: E501

        self._expires_at = expires_at

    @property
    def api_key_status(self):
        """Gets the api_key_status of this ApiKeyData.  # noqa: E501

        Api Key Status  # noqa: E501

        :return: The api_key_status of this ApiKeyData.  # noqa: E501
        :rtype: int
        """
        return self._api_key_status

    @api_key_status.setter
    def api_key_status(self, api_key_status):
        """Sets the api_key_status of this ApiKeyData.

        Api Key Status  # noqa: E501

        :param api_key_status: The api_key_status of this ApiKeyData.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and api_key_status is None:  # noqa: E501
            raise ValueError("Invalid value for `api_key_status`, must not be `None`")  # noqa: E501

        self._api_key_status = api_key_status

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
        if not isinstance(other, ApiKeyData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiKeyData):
            return True

        return self.to_dict() != other.to_dict()
