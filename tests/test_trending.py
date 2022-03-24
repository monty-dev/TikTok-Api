from TikTokApi import TikTokApi
import os


def test_trending_videos():
    with TikTokApi(custom_verify_fp=os.environ.get("verifyFp", None)) as api:
        count = sum(1 for _ in api.trending.videos(count=100))
        assert count >= 100
