# stack-pi
## 概要
pirate audio
https://shop.pimoroni.com/collections/pirate-audio

## 日本語対応
- pidiをいじれでばできそうだが、設定値にfontが無いので結構な修正が必要そう

## セットアップ
[公式手順](https://learn.pimoroni.com/article/getting-started-with-pirate-audio)

1. Raspberry Pi OS(Lite)をセットアップ
2. 必要パッケージインストール  
    ```
    sudo apt install git
    ```

3. リポジトリのclone
    ```
    git clone https://github.com/pimoroni/pirate-audio
    ```
4. インストール
    ```
    cd pirate-audio/mopidy
    sudo ./install.sh
    ```

5. 再起動
   ```
   sudo shutdown -r now
   ```

6. ブラウザで`http://<IPアドレス>:6680`にアクセス

## 設定とか
- 設定ファイルは`/etc/mopidy/mopidy.conf`
- [pidi]の項目に`idle_timeout = 0`を追記すると画面が消えなくなる
- デフォルト設定では`/home/pi/Music`に音楽ファイルを配置すれば再生可能
- spotifyの設定はよくわからん…
- 初回の再生開始はブラウザから実行する必要あり
