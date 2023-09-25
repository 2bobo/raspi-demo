# stack-pi

***更新を断念***

## 概要
[pHAT Stack](https://shop.pimoroni.com/products/phat-stack?variant=658973392906)に6個のPHATを取り付けたもののデモ
搭載HATは以下
- [TOUCH pHAT](https://shop.pimoroni.com/products/touch-phat?variant=39256557066)
- [MICRO DOT pHAT](https://shop.pimoroni.com/products/microdot-phat?variant=25454635591)
- [FOUR LETTER pHAT](https://shop.pimoroni.com/products/four-letter-phat?variant=39256047178)
- [SCROLL pHAT HD](https://shop.pimoroni.com/products/scroll-phat-hd?variant=2380803768330)
- [ENVIRO PHAT](https://github.com/pimoroni/enviro-phat) (販売終了/後継はEnviro for Raspberry Pi)
- [SPEAKER pHAT](https://github.com/pimoroni/speaker-phat) (販売終了)

## セットアップ
1. Raspberry Pi OS(Lite)をセットアップ
2. 必要パッケージインストール  
    ```
    sudo apt install python3-pip git
    ```

3. I2C有効化
    ```
    sudo raspi-config nonint do_i2c 0 
    ```

4. 各ライブラリのインストール
    ```
    sudo pip install touchphat
    sudo pip install microdotphat
    sudo pip install fourletterphat
    sudo pip install scrollphathd
    sudo pip install envirophat
    ```

3. OpenJtalkインストール
    ```
    sudo apt install open-jtalk
    sudo apt install open-jtalk-mecab-naist-jdic
    sudo apt install hts-voice-nitech-jp-atr503-m00
    ```

4. SPEAKER pHATセットアップ
    ```
    
    ```

3. Pythonモジュールインストール  
    ```
    sudo pip3 install touchphat
    ```

4. デモスクリプトコピー  
    ```
    cd /usr/local/sbin
    sudo git clone https://github.com/2bobo/raspi-demo
    ```

5. テスト実行  
    ```
    cd raspi-demo/cube-pi
    sudo python3 cube-demo.py
    ```

6. 自動起動準備  
    ```
    sudo cp -Rp /usr/local/sbin/raspi-demo/cube-pi/cube-pi.service /etc/systemd/system/.
    sudo chown root:root /etc/systemd/system/cube-pi.service
    sudo chmod 644 /etc/systemd/system/cube-pi.service
    ```

7. 自動起動設定  
    ```
    sudo systemctl daemon-reload
    sudo systemctl enable --now cube-pi.service
    ```
