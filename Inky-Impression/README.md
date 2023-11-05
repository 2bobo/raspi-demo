# Inky Impression
## 概要
7色電子ペーパーHAT  
4インチ、5.7インチ、7.3インチがある  

デモのためにAIで画像を生成し、Inky Impressionで画像を表示する。  
RasPi4 8GBモデル必須。

## 製品情報
- https://shop.pimoroni.com/products/inky-impression-5-7
- https://github.com/pimoroni/inky

## セットアップ
1. Raspberry Pi OSをセットアップ
2. I2CとSPIを有効化
3. 必要パッケージインストール  
    ```
    sudo apt install python3-pip git
    ```

4. Pythonモジュールインストール  
    ```
    pip3 install inky[rpi,example-depends]
    ```

5. デモスクリプトコピー  
    ```
    cd /usr/local/sbin
    sudo git clone https://github.com/2bobo/raspi-demo
    ```

6. テスト実行  
    ```
    cd raspi-demo/cube-pi
    sudo python3 cube-demo.py
    ```

7. 自動起動準備  
    ```
    sudo cp -Rp /usr/local/sbin/raspi-demo/Inky-Impression/create_image.service /etc/systemd/system/.
    sudo chown root:root /etc/systemd/system/create_image.service
    sudo chmod 644 /etc/systemd/system/create_image.service
    ```

8. 自動起動設定  
    ```
    sudo systemctl daemon-reload
    sudo systemctl enable --now create_image.service
    ```
