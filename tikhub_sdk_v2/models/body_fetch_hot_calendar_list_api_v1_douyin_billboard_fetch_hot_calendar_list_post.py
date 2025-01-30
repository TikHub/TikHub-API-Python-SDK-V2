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


class BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost(object):
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
        'city_code': 'str',
        'category_code': 'str',
        'end_date': 'int',
        'start_date': 'int'
    }

    attribute_map = {
        'city_code': 'city_code',
        'category_code': 'category_code',
        'end_date': 'end_date',
        'start_date': 'start_date'
    }

    def __init__(self, city_code='', category_code='', end_date=1735488000, start_date=1734902400, local_vars_configuration=None):  # noqa: E501
        """BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._city_code = None
        self._category_code = None
        self._end_date = None
        self._start_date = None
        self.discriminator = None

        if city_code is not None:
            self.city_code = city_code
        if category_code is not None:
            self.category_code = category_code
        if end_date is not None:
            self.end_date = end_date
        if start_date is not None:
            self.start_date = start_date

    @property
    def city_code(self):
        """Gets the city_code of this BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost.  # noqa: E501

        City Code，城市编码，从城市列表获取，空为全部  # noqa: E501

        :return: The city_code of this BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost.  # noqa: E501
        :rtype: str
        """
        return self._city_code

    @city_code.setter
    def city_code(self, city_code):
        """Sets the city_code of this BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost.

        City Code，城市编码，从城市列表获取，空为全部  # noqa: E501

        :param city_code: The city_code of this BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost.  # noqa: E501
        :type: str
        """

        self._city_code = city_code

    @property
    def category_code(self):
        """Gets the category_code of this BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost.  # noqa: E501

        Category Code，热点榜分类编码，从热点榜分类获取，空为全部  # noqa: E501

        :return: The category_code of this BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost.  # noqa: E501
        :rtype: str
        """
        return self._category_code

    @category_code.setter
    def category_code(self, category_code):
        """Sets the category_code of this BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost.

        Category Code，热点榜分类编码，从热点榜分类获取，空为全部  # noqa: E501

        :param category_code: The category_code of this BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost.  # noqa: E501
        :type: str
        """

        self._category_code = category_code

    @property
    def end_date(self):
        """Gets the end_date of this BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost.  # noqa: E501

        End Date，快照结束时间 格式10位时间戳  # noqa: E501

        :return: The end_date of this BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost.  # noqa: E501
        :rtype: int
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost.

        End Date，快照结束时间 格式10位时间戳  # noqa: E501

        :param end_date: The end_date of this BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost.  # noqa: E501
        :type: int
        """

        self._end_date = end_date

    @property
    def start_date(self):
        """Gets the start_date of this BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost.  # noqa: E501

        Start Date，快照开始时间 格式10位时间戳  # noqa: E501

        :return: The start_date of this BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost.  # noqa: E501
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost.

        Start Date，快照开始时间 格式10位时间戳  # noqa: E501

        :param start_date: The start_date of this BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost.  # noqa: E501
        :type: int
        """

        self._start_date = start_date

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
        if not isinstance(other, BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost):
            return True

        return self.to_dict() != other.to_dict()
