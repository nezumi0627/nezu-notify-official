import random
import string
import urllib.parse


def generate_state(length=32):
    """ランダムな状態文字列を生成する"""
    return "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(length)
    )


def url_encode(text):
    """URLエンコードを行う"""
    return urllib.parse.quote(text)


def parse_redirect_response(url):
    """リダイレクトURLからパラメータを解析する"""
    parsed = urllib.parse.urlparse(url)
    params = urllib.parse.parse_qs(parsed.query)
    return {k: v[0] for k, v in params.items()}
