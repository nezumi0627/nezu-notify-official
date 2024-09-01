class OfficialNezuError(Exception):
    """OfficialNezuNotifyの基本例外クラス"""


class OfficialNezuAuthError(OfficialNezuError):
    """認証に失敗した場合に発生する例外"""

    def __init__(self, message="認証に失敗しました"):
        self.message = message
        super().__init__(self.message)


class OfficialNezuNotifyError(OfficialNezuError):
    """通知の送信に失敗した場合に発生する例外"""

    def __init__(self, message="通知の送信に失敗しました"):
        self.message = message
        super().__init__(self.message)


class OfficialNezuRateLimitError(OfficialNezuError):
    """APIのレート制限に達した場合に発生する例外"""

    def __init__(self, message="APIのレート制限に達しました"):
        self.message = message
        super().__init__(self.message)


class OfficialNezuInvalidTokenError(OfficialNezuError):
    """アクセストークンが無効な場合に発生する例外"""

    def __init__(self, message="アクセストークンが無効です"):
        self.message = message
        super().__init__(self.message)


class OfficialNezuBadRequestError(OfficialNezuError):
    """リクエストが不正な場合に発生する例外"""

    def __init__(self, message="不正なリクエストです"):
        self.message = message
        super().__init__(self.message)


class OfficialNezuServerError(OfficialNezuError):
    """LINEサーバー側でエラーが発生した場合に発生する例外"""

    def __init__(self, message="LINEサーバーでエラーが発生しました"):
        self.message = message
        super().__init__(self.message)


class OfficialNezuNetworkError(OfficialNezuError):
    """ネットワーク関連のエラーが発生した場合に発生する例外"""

    def __init__(self, message="ネットワークエラーが発生しました"):
        self.message = message
        super().__init__(self.message)


class OfficialNezuTimeoutError(OfficialNezuError):
    """リクエストがタイムアウトした場合に発生する例外"""

    def __init__(self, message="リクエストがタイムアウトしました"):
        self.message = message
        super().__init__(self.message)
