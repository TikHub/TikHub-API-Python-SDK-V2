# coding: utf-8

"""
    TikHub.io - Your Ultimate Social Media Data & API Marketplace

    High-performance asynchronous Douyin(抖音) TikTok Xiaohongshu(小红书) Kuaishou(快手) Weibo(微博) Instagram YouTube(油管) Twitter(X) Captcha Solver(验证码解决器) Temp Mail(临时邮箱) API(接口).  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import tikhub_sdk_v2
from tikhub_sdk_v2.api.douyin_app_v3_api_api import DouyinAppV3APIApi  # noqa: E501
from tikhub_sdk_v2.rest import ApiException


class TestDouyinAppV3APIApi(unittest.TestCase):
    """DouyinAppV3APIApi unit test stubs"""

    def setUp(self):
        self.api = tikhub_sdk_v2.api.douyin_app_v3_api_api.DouyinAppV3APIApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_video_play_count_api_v1_douyin_app_v3_add_video_play_count_get(self):
        """Test case for add_video_play_count_api_v1_douyin_app_v3_add_video_play_count_get

        根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID  # noqa: E501
        """
        pass

    def test_add_video_play_count_api_v1_douyin_app_v3_add_video_play_count_get_0(self):
        """Test case for add_video_play_count_api_v1_douyin_app_v3_add_video_play_count_get_0

        根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID  # noqa: E501
        """
        pass

    def test_fetch_general_search_result_api_v1_douyin_app_v3_fetch_general_search_result_get(self):
        """Test case for fetch_general_search_result_api_v1_douyin_app_v3_fetch_general_search_result_get

        获取指定关键词的综合搜索结果（弃用，替代接口：/api/v1/douyin/web/fetch_general_search_result）/Get comprehensive search results of specified keywords (deprecated, alternative interface: /api/v1/douyin/web/fetch_general_search_result)  # noqa: E501
        """
        pass

    def test_fetch_general_search_result_api_v1_douyin_app_v3_fetch_general_search_result_get_0(self):
        """Test case for fetch_general_search_result_api_v1_douyin_app_v3_fetch_general_search_result_get_0

        获取指定关键词的综合搜索结果（弃用，替代接口：/api/v1/douyin/web/fetch_general_search_result）/Get comprehensive search results of specified keywords (deprecated, alternative interface: /api/v1/douyin/web/fetch_general_search_result)  # noqa: E501
        """
        pass

    def test_fetch_hashtag_detail_api_v1_douyin_app_v3_fetch_hashtag_detail_get(self):
        """Test case for fetch_hashtag_detail_api_v1_douyin_app_v3_fetch_hashtag_detail_get

        获取指定话题的详情数据/Get details of specified hashtag  # noqa: E501
        """
        pass

    def test_fetch_hashtag_detail_api_v1_douyin_app_v3_fetch_hashtag_detail_get_0(self):
        """Test case for fetch_hashtag_detail_api_v1_douyin_app_v3_fetch_hashtag_detail_get_0

        获取指定话题的详情数据/Get details of specified hashtag  # noqa: E501
        """
        pass

    def test_fetch_hashtag_search_result_api_v1_douyin_app_v3_fetch_hashtag_search_result_get(self):
        """Test case for fetch_hashtag_search_result_api_v1_douyin_app_v3_fetch_hashtag_search_result_get

        获取指定关键词的话题搜索结果（弃用，替代接口：/api/v1/douyin/web/fetch_hashtag_search_result）/Get hashtag search results of specified keywords (deprecated, alternative interface: /api/v1/douyin/web/fetch_hashtag_search_result)  # noqa: E501
        """
        pass

    def test_fetch_hashtag_search_result_api_v1_douyin_app_v3_fetch_hashtag_search_result_get_0(self):
        """Test case for fetch_hashtag_search_result_api_v1_douyin_app_v3_fetch_hashtag_search_result_get_0

        获取指定关键词的话题搜索结果（弃用，替代接口：/api/v1/douyin/web/fetch_hashtag_search_result）/Get hashtag search results of specified keywords (deprecated, alternative interface: /api/v1/douyin/web/fetch_hashtag_search_result)  # noqa: E501
        """
        pass

    def test_fetch_hashtag_video_list_api_v1_douyin_app_v3_fetch_hashtag_video_list_get(self):
        """Test case for fetch_hashtag_video_list_api_v1_douyin_app_v3_fetch_hashtag_video_list_get

        获取指定话题的作品数据/Get video list of specified hashtag  # noqa: E501
        """
        pass

    def test_fetch_hashtag_video_list_api_v1_douyin_app_v3_fetch_hashtag_video_list_get_0(self):
        """Test case for fetch_hashtag_video_list_api_v1_douyin_app_v3_fetch_hashtag_video_list_get_0

        获取指定话题的作品数据/Get video list of specified hashtag  # noqa: E501
        """
        pass

    def test_fetch_hot_brand_search_api_v1_douyin_app_v3_fetch_brand_hot_search_list_detail_get(self):
        """Test case for fetch_hot_brand_search_api_v1_douyin_app_v3_fetch_brand_hot_search_list_detail_get

        获取抖音品牌热榜具体分类数据/Get Douyin brand hot search list detail data  # noqa: E501
        """
        pass

    def test_fetch_hot_brand_search_api_v1_douyin_app_v3_fetch_brand_hot_search_list_detail_get_0(self):
        """Test case for fetch_hot_brand_search_api_v1_douyin_app_v3_fetch_brand_hot_search_list_detail_get_0

        获取抖音品牌热榜具体分类数据/Get Douyin brand hot search list detail data  # noqa: E501
        """
        pass

    def test_fetch_hot_brand_search_category_api_v1_douyin_app_v3_fetch_brand_hot_search_list_get(self):
        """Test case for fetch_hot_brand_search_category_api_v1_douyin_app_v3_fetch_brand_hot_search_list_get

        获取抖音品牌热榜分类数据/Get Douyin brand hot search list data  # noqa: E501
        """
        pass

    def test_fetch_hot_brand_search_category_api_v1_douyin_app_v3_fetch_brand_hot_search_list_get_0(self):
        """Test case for fetch_hot_brand_search_category_api_v1_douyin_app_v3_fetch_brand_hot_search_list_get_0

        获取抖音品牌热榜分类数据/Get Douyin brand hot search list data  # noqa: E501
        """
        pass

    def test_fetch_hot_search_list_api_v1_douyin_app_v3_fetch_hot_search_list_get(self):
        """Test case for fetch_hot_search_list_api_v1_douyin_app_v3_fetch_hot_search_list_get

        获取抖音热搜榜数据/Get Douyin hot search list data  # noqa: E501
        """
        pass

    def test_fetch_hot_search_list_api_v1_douyin_app_v3_fetch_hot_search_list_get_0(self):
        """Test case for fetch_hot_search_list_api_v1_douyin_app_v3_fetch_hot_search_list_get_0

        获取抖音热搜榜数据/Get Douyin hot search list data  # noqa: E501
        """
        pass

    def test_fetch_live_hot_search_list_api_v1_douyin_app_v3_fetch_live_hot_search_list_get(self):
        """Test case for fetch_live_hot_search_list_api_v1_douyin_app_v3_fetch_live_hot_search_list_get

        获取抖音直播热搜榜数据/Get Douyin live hot search list data  # noqa: E501
        """
        pass

    def test_fetch_live_hot_search_list_api_v1_douyin_app_v3_fetch_live_hot_search_list_get_0(self):
        """Test case for fetch_live_hot_search_list_api_v1_douyin_app_v3_fetch_live_hot_search_list_get_0

        获取抖音直播热搜榜数据/Get Douyin live hot search list data  # noqa: E501
        """
        pass

    def test_fetch_live_search_result_api_v1_douyin_app_v3_fetch_live_search_result_get(self):
        """Test case for fetch_live_search_result_api_v1_douyin_app_v3_fetch_live_search_result_get

        获取指定关键词的直播搜索结果（弃用，替代接口：/api/v1/douyin/web/fetch_live_search_result）/Get live search results of specified keywords (deprecated, alternative interface: /api/v1/douyin/web/fetch_live_search_result)  # noqa: E501
        """
        pass

    def test_fetch_live_search_result_api_v1_douyin_app_v3_fetch_live_search_result_get_0(self):
        """Test case for fetch_live_search_result_api_v1_douyin_app_v3_fetch_live_search_result_get_0

        获取指定关键词的直播搜索结果（弃用，替代接口：/api/v1/douyin/web/fetch_live_search_result）/Get live search results of specified keywords (deprecated, alternative interface: /api/v1/douyin/web/fetch_live_search_result)  # noqa: E501
        """
        pass

    def test_fetch_multi_video_api_v1_douyin_app_v3_fetch_multi_video_post(self):
        """Test case for fetch_multi_video_api_v1_douyin_app_v3_fetch_multi_video_post

        批量获取视频信息/Batch Get Video Information  # noqa: E501
        """
        pass

    def test_fetch_multi_video_api_v1_douyin_app_v3_fetch_multi_video_post_0(self):
        """Test case for fetch_multi_video_api_v1_douyin_app_v3_fetch_multi_video_post_0

        批量获取视频信息/Batch Get Video Information  # noqa: E501
        """
        pass

    def test_fetch_multi_video_statistics_api_v1_douyin_app_v3_fetch_multi_video_statistics_get(self):
        """Test case for fetch_multi_video_statistics_api_v1_douyin_app_v3_fetch_multi_video_statistics_get

        根据视频ID批量获取作品的统计数据（点赞数、下载数、播放数、分享数）/Get the statistical data of the Post according to the video ID (like count, download count, play count, share count)  # noqa: E501
        """
        pass

    def test_fetch_multi_video_statistics_api_v1_douyin_app_v3_fetch_multi_video_statistics_get_0(self):
        """Test case for fetch_multi_video_statistics_api_v1_douyin_app_v3_fetch_multi_video_statistics_get_0

        根据视频ID批量获取作品的统计数据（点赞数、下载数、播放数、分享数）/Get the statistical data of the Post according to the video ID (like count, download count, play count, share count)  # noqa: E501
        """
        pass

    def test_fetch_music_detail_api_v1_douyin_app_v3_fetch_music_detail_get(self):
        """Test case for fetch_music_detail_api_v1_douyin_app_v3_fetch_music_detail_get

        获取指定音乐的详情数据/Get details of specified music  # noqa: E501
        """
        pass

    def test_fetch_music_detail_api_v1_douyin_app_v3_fetch_music_detail_get_0(self):
        """Test case for fetch_music_detail_api_v1_douyin_app_v3_fetch_music_detail_get_0

        获取指定音乐的详情数据/Get details of specified music  # noqa: E501
        """
        pass

    def test_fetch_music_hot_search_list_api_v1_douyin_app_v3_fetch_music_hot_search_list_get(self):
        """Test case for fetch_music_hot_search_list_api_v1_douyin_app_v3_fetch_music_hot_search_list_get

        获取抖音音乐热榜数据/Get Douyin music hot search list data  # noqa: E501
        """
        pass

    def test_fetch_music_hot_search_list_api_v1_douyin_app_v3_fetch_music_hot_search_list_get_0(self):
        """Test case for fetch_music_hot_search_list_api_v1_douyin_app_v3_fetch_music_hot_search_list_get_0

        获取抖音音乐热榜数据/Get Douyin music hot search list data  # noqa: E501
        """
        pass

    def test_fetch_music_search_result_api_v1_douyin_app_v3_fetch_music_search_result_get(self):
        """Test case for fetch_music_search_result_api_v1_douyin_app_v3_fetch_music_search_result_get

        获取指定关键词的音乐搜索结果（弃用，替代接口：/api/v1/douyin/web/fetch_music_search_result）/Get music search results of specified keywords (deprecated, alternative interface: /api/v1/douyin/web/fetch_music_search_result)  # noqa: E501
        """
        pass

    def test_fetch_music_search_result_api_v1_douyin_app_v3_fetch_music_search_result_get_0(self):
        """Test case for fetch_music_search_result_api_v1_douyin_app_v3_fetch_music_search_result_get_0

        获取指定关键词的音乐搜索结果（弃用，替代接口：/api/v1/douyin/web/fetch_music_search_result）/Get music search results of specified keywords (deprecated, alternative interface: /api/v1/douyin/web/fetch_music_search_result)  # noqa: E501
        """
        pass

    def test_fetch_music_video_list_api_v1_douyin_app_v3_fetch_music_video_list_get(self):
        """Test case for fetch_music_video_list_api_v1_douyin_app_v3_fetch_music_video_list_get

        获取指定音乐的视频列表数据/Get video list of specified music  # noqa: E501
        """
        pass

    def test_fetch_music_video_list_api_v1_douyin_app_v3_fetch_music_video_list_get_0(self):
        """Test case for fetch_music_video_list_api_v1_douyin_app_v3_fetch_music_video_list_get_0

        获取指定音乐的视频列表数据/Get video list of specified music  # noqa: E501
        """
        pass

    def test_fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_get(self):
        """Test case for fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_get

        获取单个作品数据/Get single video data  # noqa: E501
        """
        pass

    def test_fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_get_0(self):
        """Test case for fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_get_0

        获取单个作品数据/Get single video data  # noqa: E501
        """
        pass

    def test_fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_v2_get(self):
        """Test case for fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_v2_get

        获取单个作品数据/Get single video data  # noqa: E501
        """
        pass

    def test_fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_v2_get_0(self):
        """Test case for fetch_one_video_api_v1_douyin_app_v3_fetch_one_video_v2_get_0

        获取单个作品数据/Get single video data  # noqa: E501
        """
        pass

    def test_fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_one_video_by_share_url_get(self):
        """Test case for fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_one_video_by_share_url_get

        根据分享链接获取单个作品数据/Get single video data by sharing link  # noqa: E501
        """
        pass

    def test_fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_one_video_by_share_url_get_0(self):
        """Test case for fetch_one_video_by_share_url_api_v1_douyin_app_v3_fetch_one_video_by_share_url_get_0

        根据分享链接获取单个作品数据/Get single video data by sharing link  # noqa: E501
        """
        pass

    def test_fetch_user_fans_list_api_v1_douyin_app_v3_fetch_user_fans_list_get(self):
        """Test case for fetch_user_fans_list_api_v1_douyin_app_v3_fetch_user_fans_list_get

        获取用户粉丝列表/Get user fans list  # noqa: E501
        """
        pass

    def test_fetch_user_fans_list_api_v1_douyin_app_v3_fetch_user_fans_list_get_0(self):
        """Test case for fetch_user_fans_list_api_v1_douyin_app_v3_fetch_user_fans_list_get_0

        获取用户粉丝列表/Get user fans list  # noqa: E501
        """
        pass

    def test_fetch_user_following_list_api_v1_douyin_app_v3_fetch_user_following_list_get(self):
        """Test case for fetch_user_following_list_api_v1_douyin_app_v3_fetch_user_following_list_get

        获取用户关注列表/Get user following list  # noqa: E501
        """
        pass

    def test_fetch_user_following_list_api_v1_douyin_app_v3_fetch_user_following_list_get_0(self):
        """Test case for fetch_user_following_list_api_v1_douyin_app_v3_fetch_user_following_list_get_0

        获取用户关注列表/Get user following list  # noqa: E501
        """
        pass

    def test_fetch_user_like_videos_api_v1_douyin_app_v3_fetch_user_like_videos_get(self):
        """Test case for fetch_user_like_videos_api_v1_douyin_app_v3_fetch_user_like_videos_get

        获取用户喜欢作品数据/Get user like video data  # noqa: E501
        """
        pass

    def test_fetch_user_like_videos_api_v1_douyin_app_v3_fetch_user_like_videos_get_0(self):
        """Test case for fetch_user_like_videos_api_v1_douyin_app_v3_fetch_user_like_videos_get_0

        获取用户喜欢作品数据/Get user like video data  # noqa: E501
        """
        pass

    def test_fetch_user_post_videos_api_v1_douyin_app_v3_fetch_user_post_videos_get(self):
        """Test case for fetch_user_post_videos_api_v1_douyin_app_v3_fetch_user_post_videos_get

        获取用户主页作品数据/Get user homepage video data  # noqa: E501
        """
        pass

    def test_fetch_user_post_videos_api_v1_douyin_app_v3_fetch_user_post_videos_get_0(self):
        """Test case for fetch_user_post_videos_api_v1_douyin_app_v3_fetch_user_post_videos_get_0

        获取用户主页作品数据/Get user homepage video data  # noqa: E501
        """
        pass

    def test_fetch_user_search_result_api_v1_douyin_app_v3_fetch_user_search_result_get(self):
        """Test case for fetch_user_search_result_api_v1_douyin_app_v3_fetch_user_search_result_get

        获取指定关键词的用户搜索结果（弃用，替代接口：/api/v1/douyin/web/fetch_user_search_result_v2）/Get user search results of specified keywords (deprecated, alternative interface: /api/v1/douyin/web/fetch_user_search_result_v2)  # noqa: E501
        """
        pass

    def test_fetch_user_search_result_api_v1_douyin_app_v3_fetch_user_search_result_get_0(self):
        """Test case for fetch_user_search_result_api_v1_douyin_app_v3_fetch_user_search_result_get_0

        获取指定关键词的用户搜索结果（弃用，替代接口：/api/v1/douyin/web/fetch_user_search_result_v2）/Get user search results of specified keywords (deprecated, alternative interface: /api/v1/douyin/web/fetch_user_search_result_v2)  # noqa: E501
        """
        pass

    def test_fetch_video_comments_api_v1_douyin_app_v3_fetch_video_comments_get(self):
        """Test case for fetch_video_comments_api_v1_douyin_app_v3_fetch_video_comments_get

        获取单个视频评论数据/Get single video comments data  # noqa: E501
        """
        pass

    def test_fetch_video_comments_api_v1_douyin_app_v3_fetch_video_comments_get_0(self):
        """Test case for fetch_video_comments_api_v1_douyin_app_v3_fetch_video_comments_get_0

        获取单个视频评论数据/Get single video comments data  # noqa: E501
        """
        pass

    def test_fetch_video_comments_reply_api_v1_douyin_app_v3_fetch_video_comment_replies_get(self):
        """Test case for fetch_video_comments_reply_api_v1_douyin_app_v3_fetch_video_comment_replies_get

        获取指定视频的评论回复数据/Get comment replies data of specified video  # noqa: E501
        """
        pass

    def test_fetch_video_comments_reply_api_v1_douyin_app_v3_fetch_video_comment_replies_get_0(self):
        """Test case for fetch_video_comments_reply_api_v1_douyin_app_v3_fetch_video_comment_replies_get_0

        获取指定视频的评论回复数据/Get comment replies data of specified video  # noqa: E501
        """
        pass

    def test_fetch_video_mix_detail_api_v1_douyin_app_v3_fetch_video_mix_detail_get(self):
        """Test case for fetch_video_mix_detail_api_v1_douyin_app_v3_fetch_video_mix_detail_get

        获取抖音视频合集详情数据/Get Douyin video mix detail data  # noqa: E501
        """
        pass

    def test_fetch_video_mix_detail_api_v1_douyin_app_v3_fetch_video_mix_detail_get_0(self):
        """Test case for fetch_video_mix_detail_api_v1_douyin_app_v3_fetch_video_mix_detail_get_0

        获取抖音视频合集详情数据/Get Douyin video mix detail data  # noqa: E501
        """
        pass

    def test_fetch_video_mix_post_list_api_v1_douyin_app_v3_fetch_video_mix_post_list_get(self):
        """Test case for fetch_video_mix_post_list_api_v1_douyin_app_v3_fetch_video_mix_post_list_get

        获取抖音视频合集作品列表数据/Get Douyin video mix post list data  # noqa: E501
        """
        pass

    def test_fetch_video_mix_post_list_api_v1_douyin_app_v3_fetch_video_mix_post_list_get_0(self):
        """Test case for fetch_video_mix_post_list_api_v1_douyin_app_v3_fetch_video_mix_post_list_get_0

        获取抖音视频合集作品列表数据/Get Douyin video mix post list data  # noqa: E501
        """
        pass

    def test_fetch_video_search_result_api_v1_douyin_app_v3_fetch_video_search_result_get(self):
        """Test case for fetch_video_search_result_api_v1_douyin_app_v3_fetch_video_search_result_get

        获取指定关键词的视频搜索结果（弃用，替代接口：/api/v1/douyin/web/fetch_video_search_result）/Get video search results of specified keywords (deprecated, alternative interface: /api/v1/douyin/web/fetch_video_search_result)  # noqa: E501
        """
        pass

    def test_fetch_video_search_result_api_v1_douyin_app_v3_fetch_video_search_result_get_0(self):
        """Test case for fetch_video_search_result_api_v1_douyin_app_v3_fetch_video_search_result_get_0

        获取指定关键词的视频搜索结果（弃用，替代接口：/api/v1/douyin/web/fetch_video_search_result）/Get video search results of specified keywords (deprecated, alternative interface: /api/v1/douyin/web/fetch_video_search_result)  # noqa: E501
        """
        pass

    def test_fetch_video_search_result_v2_api_v1_douyin_app_v3_fetch_video_search_result_v2_get(self):
        """Test case for fetch_video_search_result_v2_api_v1_douyin_app_v3_fetch_video_search_result_v2_get

        获取指定关键词的视频搜索结果V2/Get video search results of specified keywords V2  # noqa: E501
        """
        pass

    def test_fetch_video_search_result_v2_api_v1_douyin_app_v3_fetch_video_search_result_v2_get_0(self):
        """Test case for fetch_video_search_result_v2_api_v1_douyin_app_v3_fetch_video_search_result_v2_get_0

        获取指定关键词的视频搜索结果V2/Get video search results of specified keywords V2  # noqa: E501
        """
        pass

    def test_fetch_video_statistics_api_v1_douyin_app_v3_fetch_video_statistics_get(self):
        """Test case for fetch_video_statistics_api_v1_douyin_app_v3_fetch_video_statistics_get

        根据视频ID获取作品的统计数据（点赞数、下载数、播放数、分享数）/Get the statistical data of the Post according to the video ID (like count, download count, play count, share count)  # noqa: E501
        """
        pass

    def test_fetch_video_statistics_api_v1_douyin_app_v3_fetch_video_statistics_get_0(self):
        """Test case for fetch_video_statistics_api_v1_douyin_app_v3_fetch_video_statistics_get_0

        根据视频ID获取作品的统计数据（点赞数、下载数、播放数、分享数）/Get the statistical data of the Post according to the video ID (like count, download count, play count, share count)  # noqa: E501
        """
        pass

    def test_generate_douyin_short_url_api_v1_douyin_app_v3_generate_douyin_short_url_get(self):
        """Test case for generate_douyin_short_url_api_v1_douyin_app_v3_generate_douyin_short_url_get

        生成抖音短链接/Generate Douyin short link  # noqa: E501
        """
        pass

    def test_generate_douyin_short_url_api_v1_douyin_app_v3_generate_douyin_short_url_get_0(self):
        """Test case for generate_douyin_short_url_api_v1_douyin_app_v3_generate_douyin_short_url_get_0

        生成抖音短链接/Generate Douyin short link  # noqa: E501
        """
        pass

    def test_generate_douyin_video_share_qrcode_api_v1_douyin_app_v3_generate_douyin_video_share_qrcode_get(self):
        """Test case for generate_douyin_video_share_qrcode_api_v1_douyin_app_v3_generate_douyin_video_share_qrcode_get

        生成抖音视频分享二维码/Generate Douyin video share QR code  # noqa: E501
        """
        pass

    def test_generate_douyin_video_share_qrcode_api_v1_douyin_app_v3_generate_douyin_video_share_qrcode_get_0(self):
        """Test case for generate_douyin_video_share_qrcode_api_v1_douyin_app_v3_generate_douyin_video_share_qrcode_get_0

        生成抖音视频分享二维码/Generate Douyin video share QR code  # noqa: E501
        """
        pass

    def test_handler_user_profile_api_v1_douyin_app_v3_handler_user_profile_get(self):
        """Test case for handler_user_profile_api_v1_douyin_app_v3_handler_user_profile_get

        获取指定用户的信息/Get information of specified user  # noqa: E501
        """
        pass

    def test_handler_user_profile_api_v1_douyin_app_v3_handler_user_profile_get_0(self):
        """Test case for handler_user_profile_api_v1_douyin_app_v3_handler_user_profile_get_0

        获取指定用户的信息/Get information of specified user  # noqa: E501
        """
        pass

    def test_open_douyin_app_to_keyword_search_api_v1_douyin_app_v3_open_douyin_app_to_keyword_search_get(self):
        """Test case for open_douyin_app_to_keyword_search_api_v1_douyin_app_v3_open_douyin_app_to_keyword_search_get

        生成抖音分享链接，唤起抖音APP，跳转指定关键词搜索结果/Generate Douyin share link, call Douyin APP, and jump to the specified keyword search result  # noqa: E501
        """
        pass

    def test_open_douyin_app_to_keyword_search_api_v1_douyin_app_v3_open_douyin_app_to_keyword_search_get_0(self):
        """Test case for open_douyin_app_to_keyword_search_api_v1_douyin_app_v3_open_douyin_app_to_keyword_search_get_0

        生成抖音分享链接，唤起抖音APP，跳转指定关键词搜索结果/Generate Douyin share link, call Douyin APP, and jump to the specified keyword search result  # noqa: E501
        """
        pass

    def test_open_douyin_app_to_send_private_message_api_v1_douyin_app_v3_open_douyin_app_to_send_private_message_get(self):
        """Test case for open_douyin_app_to_send_private_message_api_v1_douyin_app_v3_open_douyin_app_to_send_private_message_get

        生成抖音分享链接，唤起抖音APP，给指定用户发送私信/Generate Douyin share link, call Douyin APP, and send private messages to specified users  # noqa: E501
        """
        pass

    def test_open_douyin_app_to_send_private_message_api_v1_douyin_app_v3_open_douyin_app_to_send_private_message_get_0(self):
        """Test case for open_douyin_app_to_send_private_message_api_v1_douyin_app_v3_open_douyin_app_to_send_private_message_get_0

        生成抖音分享链接，唤起抖音APP，给指定用户发送私信/Generate Douyin share link, call Douyin APP, and send private messages to specified users  # noqa: E501
        """
        pass

    def test_open_douyin_app_to_user_profile_api_v1_douyin_app_v3_open_douyin_app_to_user_profile_get(self):
        """Test case for open_douyin_app_to_user_profile_api_v1_douyin_app_v3_open_douyin_app_to_user_profile_get

        生成抖音分享链接，唤起抖音APP，跳转指定用户主页/Generate Douyin share link, call Douyin APP, and jump to the specified user profile  # noqa: E501
        """
        pass

    def test_open_douyin_app_to_user_profile_api_v1_douyin_app_v3_open_douyin_app_to_user_profile_get_0(self):
        """Test case for open_douyin_app_to_user_profile_api_v1_douyin_app_v3_open_douyin_app_to_user_profile_get_0

        生成抖音分享链接，唤起抖音APP，跳转指定用户主页/Generate Douyin share link, call Douyin APP, and jump to the specified user profile  # noqa: E501
        """
        pass

    def test_open_douyin_app_to_video_detail_api_v1_douyin_app_v3_open_douyin_app_to_video_detail_get(self):
        """Test case for open_douyin_app_to_video_detail_api_v1_douyin_app_v3_open_douyin_app_to_video_detail_get

        生成抖音分享链接，唤起抖音APP，跳转指定作品详情页/Generate Douyin share link, call Douyin APP, and jump to the specified video details page  # noqa: E501
        """
        pass

    def test_open_douyin_app_to_video_detail_api_v1_douyin_app_v3_open_douyin_app_to_video_detail_get_0(self):
        """Test case for open_douyin_app_to_video_detail_api_v1_douyin_app_v3_open_douyin_app_to_video_detail_get_0

        生成抖音分享链接，唤起抖音APP，跳转指定作品详情页/Generate Douyin share link, call Douyin APP, and jump to the specified video details page  # noqa: E501
        """
        pass

    def test_register_device_api_v1_douyin_app_v3_register_device_get(self):
        """Test case for register_device_api_v1_douyin_app_v3_register_device_get

        抖音APP注册设备/Douyin APP register device  # noqa: E501
        """
        pass

    def test_register_device_api_v1_douyin_app_v3_register_device_get_0(self):
        """Test case for register_device_api_v1_douyin_app_v3_register_device_get_0

        抖音APP注册设备/Douyin APP register device  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
