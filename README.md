# chrome driverをインストール
- https://chromedriver.chromium.org/downloads
※　自分のクロームのバージョンと同じverをインストールすること
- 適当なパスに配置し、その絶対パスをexecutable_pathに貼り付ける。




# ログイン状態を保持する

- chrome で新しいユーザーを追加する。
- そのユーザーでアプリにログイン
- アドレスバーにchrome://version/を入力
  - プロフィール パスをコピー
  - ソース内chrome profile pathに貼り付け（/Default以前の部分）