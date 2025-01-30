#! /usr/bin/env python
# -*- coding: utf-8 -*-
# RUN Command Line:
# 1.Build-check dist folder
# python setup.py sdist bdist_wheel
# 2.Upload to PyPi
# twine upload dist/*

"""
TikHub.io - Your Ultimate Social Media Data & API Marketplace
High-performance asynchronous Douyin(抖音) TikTok Xiaohongshu(小红书) Kuaishou(快手) Weibo(微博) Instagram YouTube(油管) Twitter(X) Captcha Solver(验证码解决器) Temp Mail(临时邮箱) API(接口).
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "tikhub_sdk_v2"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="TikHub.io - Your Ultimate Social Media Data &amp; API Marketplace",
    author="TikHub.io",
    author_email="tikhub.io@proton.me",
    url="https://github.com/TikHub/TikHub-API-Python-SDK-V2",
    keywords=["OpenAPI", "OpenAPI-Generator", "TikHub.io - Your Ultimate Social Media Data & API Marketplace"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    High-performance asynchronous Douyin(抖音) TikTok Xiaohongshu(小红书) Kuaishou(快手) Weibo(微博) Instagram YouTube(油管) Twitter(X) Captcha Solver(验证码解决器) Temp Mail(临时邮箱) API(接口).  # noqa: E501
    """
)
