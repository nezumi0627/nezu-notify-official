class OfficialNezuError(Exception):
    """OfficialNezuNotifyの基本例外クラス"""


class OfficialNezuAuthError(OfficialNezuError):
    """認証に失敗した場合に発生する例外"""


class OfficialNezuNotifyError(OfficialNezuError):
    """通知の送信に失敗した場合に発生する例外"""


class OfficialNezuRateLimitError(OfficialNezuError):
    """APIのレート制限に達した場合に発生する例外"""


class OfficialNezuInvalidTokenError(OfficialNezuError):
    """アクセストークンが無効な場合に発生する例外"""


class OfficialNezuBadRequestError(OfficialNezuError):
    """リクエストが不正な場合に発生する例外"""


class OfficialNezuServerError(OfficialNezuError):
    """LINEサーバー側でエラーが発生した場合に発生する例外"""
