# set up
- ①chrome driverをインストール
  - https://chromedriver.chromium.org/downloads

    ※　自分のクロームのバージョンと同じverをインストールすること
- ブラウザアドレスバーにchrome://version/を入力
- ②プロフィール パスの/Default以前の部分をコピー
- プロジェクト直下に.envファイルを作成
  - TARGET_PAGEに対象アプリのホームを指定
  - DRIVER_PATHに①でダウンロードしたchrome driverの絶対パスを指定
  - PROFILE_PATHに②でコピーしたプロフィールパスをペースト
  
  ※.envファイルフォーマット
  ```
  TARGET_PAGE = "アプリのホームURL"
  DRIVER_PATH = "chrome driverの絶対パス"
  PROFILE_PATH = "プロフィールパス"
  ```
# ツール起動と停止方法
- 以下のコマンドを実行して必要モジュールをインストールする。

  `make setup`
- プロジェクトディレクトリで以下のコマンドを実行して起動

  `make run`
- クリック数が上限に達したら自動的に終了されます。
- 途中停止する場合はctrl + cでツールを終了。ブラウザは勝手に閉じます。

# 注意
- 初回はログインが必要です。
  - ログイン状態はプロフィールパスに保存されるので二回目以降はログインの必要なし
- chromeを終了している状態から起動してください。
  - 既に開いているとエラーが出て起動できません。