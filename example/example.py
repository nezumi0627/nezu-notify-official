import os

from OfficialNezuNotify import OfficialNezuAuth, OfficialNezuNotify

# 環境変数から認証情報を取得
CLIENT_ID = os.environ.get("LINE_NOTIFY_CLIENT_ID")
CLIENT_SECRET = os.environ.get("LINE_NOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.environ.get("LINE_NOTIFY_REDIRECT_URI")


def main():
    # 認証オブジェクトの作成
    auth = OfficialNezuAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)

    # 認証URLの生成
    state = "random_state_string"
    auth_url = auth.get_auth_url(state)
    print(f"認証URLにアクセスしてください: {auth_url}")

    # ユーザーに認証コードを入力してもらう
    code = input("認証コードを入力してください: ")

    # アクセストークンの取得
    access_token = auth.get_access_token(code)
    print(f"アクセストークン: {access_token}")

    # 通知オブジェクトの作成
    notify = OfficialNezuNotify(access_token)

    # メッセージの送信
    result = notify.send_message("Hello from OfficialNezuNotify!")
    print(f"送信結果: {result}")

    # ステータスの取得
    status = notify.get_status()
    print(f"ステータス: {status}")

    # トークンの失効（注意: 実行するとトークンが無効になります）
    # revoke_result = notify.revoke()
    # print(f"失効結果: {revoke_result}")


if __name__ == "__main__":
    main()
