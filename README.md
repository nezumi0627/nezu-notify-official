# OfficialNezuNotify

OfficialNezuNotify は、LINE Notify 公式 API を利用した Python 通知管理ライブラリです。

## 特徴

- LINE Notify 公式 API を簡単に利用可能
- 認証、通知送信、ステータス取得、トークン失効などの機能をサポート
- エラーハンドリングとレート制限の管理

## インストール

```
git clone https://github.com/neuzmi0627/OfficialNezuNotify.git
cd OfficialNezuNotify
python setup.py install
```

## 使用例

```python
from OfficialNezuNotify import OfficialNezuAuth, OfficialNezuNotify

# 認証
auth = OfficialNezuAuth("YOUR_CLIENT_ID", "YOUR_CLIENT_SECRET", "YOUR_REDIRECT_URI")
auth_url = auth.get_auth_url("YOUR_STATE")
# ユーザーに auth_url にアクセスしてもらい、認証コードを取得

# アクセストークンの取得
access_token = auth.get_access_token("AUTHORIZATION_CODE")

# 通知の送信
notify = OfficialNezuNotify(access_token)
result = notify.send_message("Hello, LINE Notify!")
print(result)
```

詳細な使用方法は `example/example.py` を参照してください。

## ライセンス

MIT License

## 作者

neuzmi0627 (neuzmi.0627.dev@gmail.com)

## リポジトリ

https://github.com/neuzmi0627/OfficialNezuNotify
