import requests

from .config import Config
from .exceptions import (
    OfficialNezuAuthError,
    OfficialNezuBadRequestError,
    OfficialNezuServerError,
)


class OfficialNezuAuth:
    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def get_auth_url(self, state, response_mode="form_post"):
        """認証URLを生成する"""
        params = {
            "response_type": "code",
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "scope": "notify",
            "state": state,
            "response_mode": response_mode,
        }
        return f"{Config.AUTH_URL}?{'&'.join(f'{k}={v}' for k, v in params.items())}"

    def get_access_token(self, code):
        """アクセストークンを取得する"""
        data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": self.redirect_uri,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        try:
            response = requests.post(
                Config.TOKEN_URL, data=data, timeout=Config.DEFAULT_TIMEOUT
            )
            response.raise_for_status()
            return response.json()["access_token"]
        except requests.HTTPError as e:
            if e.response.status_code == 400:
                raise OfficialNezuBadRequestError(
                    "不正なリクエストです。パラメータを確認してください。"
                ) from e
            elif e.response.status_code >= 500:
                raise OfficialNezuServerError(
                    f"LINEサーバーでエラーが発生しました。ステータスコード: {e.response.status_code}"
                ) from e
            else:
                raise OfficialNezuAuthError(
                    f"アクセストークンの取得に失敗しました: {e}"
                ) from e
        except requests.RequestException as e:
            raise OfficialNezuAuthError(
                f"アクセストークンの取得に失敗しました: {e}"
            ) from e
