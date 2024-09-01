import requests

from .config import Config
from .exceptions import (
    OfficialNezuBadRequestError,
    OfficialNezuInvalidTokenError,
    OfficialNezuNotifyError,
    OfficialNezuRateLimitError,
    OfficialNezuServerError,
)


class OfficialNezuNotify:
    def __init__(self, access_token):
        self.access_token = access_token
        self.headers = {"Authorization": f"Bearer {self.access_token}"}

    def send_message(
        self,
        message,
        image_url=None,
        sticker_package_id=None,
        sticker_id=None,
        notification_disabled=False,
    ):
        """メッセージを送信する"""
        data = {"message": message}

        if image_url:
            data["imageThumbnail"] = image_url
            data["imageFullsize"] = image_url

        if sticker_package_id and sticker_id:
            data["stickerPackageId"] = sticker_package_id
            data["stickerId"] = sticker_id

        if notification_disabled:
            data["notificationDisabled"] = "true"

        try:
            response = requests.post(
                Config.NOTIFY_URL,
                headers=self.headers,
                data=data,
                timeout=Config.DEFAULT_TIMEOUT,
            )
            response.raise_for_status()
            return self._parse_rate_limit(response)
        except requests.HTTPError as e:
            self._handle_http_error(e)
        except requests.RequestException as e:
            raise OfficialNezuNotifyError(f"メッセージの送信に失敗しました: {e}") from e

    def get_status(self):
        """通知の状態を取得する"""
        try:
            response = requests.get(
                Config.STATUS_URL,
                headers=self.headers,
                timeout=Config.DEFAULT_TIMEOUT,
            )
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as e:
            self._handle_http_error(e)
        except requests.RequestException as e:
            raise OfficialNezuNotifyError(f"状態の取得に失敗しました: {e}") from e

    def revoke(self):
        """通知設定を解除する"""
        try:
            response = requests.post(
                Config.REVOKE_URL,
                headers=self.headers,
                timeout=Config.DEFAULT_TIMEOUT,
            )
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as e:
            self._handle_http_error(e)
        except requests.RequestException as e:
            raise OfficialNezuNotifyError(f"通知設定の解除に失敗しました: {e}") from e

    def _handle_http_error(self, e):
        """HTTPエラーを適切な例外に変換する"""
        if e.response.status_code == 400:
            raise OfficialNezuBadRequestError(
                "不正なリクエストです。パラメータを確認してください。"
            ) from e
        elif e.response.status_code == 401:
            raise OfficialNezuInvalidTokenError("アクセストークンが無効です。") from e
        elif e.response.status_code == 429:
            raise OfficialNezuRateLimitError(
                "APIの呼び出し回数制限に達しました。"
            ) from e
        elif e.response.status_code >= 500:
            raise OfficialNezuServerError(
                f"LINEサーバーでエラーが発生しました。ステータスコード: {e.response.status_code}"
            ) from e
        else:
            raise OfficialNezuNotifyError(f"予期せぬエラーが発生しました: {e}") from e

    def _parse_rate_limit(self, response):
        """レスポンスヘッダーからレート制限情報を解析する"""
        result = response.json()
        result.update(
            {
                "x_ratelimit_limit": int(response.headers.get("X-RateLimit-Limit", 0)),
                "x_ratelimit_remaining": int(
                    response.headers.get("X-RateLimit-Remaining", 0)
                ),
                "x_ratelimit_imagelimit": int(
                    response.headers.get("X-RateLimit-ImageLimit", 0)
                ),
                "x_ratelimit_imageremaining": int(
                    response.headers.get("X-RateLimit-ImageRemaining", 0)
                ),
                "x_ratelimit_reset": int(response.headers.get("X-RateLimit-Reset", 0)),
            }
        )
        return result
