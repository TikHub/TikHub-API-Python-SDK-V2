# coding: utf-8

"""
    TikHub.io - Your Ultimate Social Media Data & API Marketplace

    High-performance asynchronous Douyin(抖音) TikTok Xiaohongshu(小红书) Kuaishou(快手) Weibo(微博) Instagram YouTube(油管) Twitter(X) Captcha Solver(验证码解决器) Temp Mail(临时邮箱) API(接口).  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import tikhub_sdk_v2
from tikhub_sdk_v2.models.body_amazon_captcha_api_v1_captcha_amazon_captcha_post import BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost  # noqa: E501
from tikhub_sdk_v2.rest import ApiException

class TestBodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost(unittest.TestCase):
    """BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tikhub_sdk_v2.models.body_amazon_captcha_api_v1_captcha_amazon_captcha_post.BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost()  # noqa: E501
        if include_optional :
            return BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost(
                app_id = '0', 
                url = '0', 
                proxy = tikhub_sdk_v2.models.proxy.Proxy()
            )
        else :
            return BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost(
                app_id = '0',
                url = '0',
        )

    def testBodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost(self):
        """Test BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
