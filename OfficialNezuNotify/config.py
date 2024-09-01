class Config:
    API_BASE_URL = "https://notify-api.line.me"
    AUTH_BASE_URL = "https://notify-bot.line.me"
    AUTH_URL = f"{AUTH_BASE_URL}/oauth/authorize"
    TOKEN_URL = f"{AUTH_BASE_URL}/oauth/token"
    NOTIFY_URL = f"{API_BASE_URL}/api/notify"
    STATUS_URL = f"{API_BASE_URL}/api/status"
    REVOKE_URL = f"{API_BASE_URL}/api/revoke"

    DEFAULT_TIMEOUT = 30
