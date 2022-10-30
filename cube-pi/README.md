# cube-pi
## 概要
4tronixのCUBE:BITのデモ
3*3*3のLEDマトリクス表示

## 製品情報
- https://shop.4tronix.co.uk/products/cubebit
- https://github.com/rpi-ws281x/rpi-ws281x-python

## セットアップ
1. Raspberry Pi OS(Lite)をセットアップ
2. 必要パッケージインストール  
    ```
    sudo apt install python3-pip git
    ```

3. Pythonモジュールインストール  
    ```
    sudo pip3 install rpi_ws281x
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
