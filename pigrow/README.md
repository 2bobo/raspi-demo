# pigrow
## 概要
土壌水分量測定きっと

## 製品情報
- https://shop.pimoroni.com/products/grow
- https://learn.pimoroni.com/article/assembling-grow

## セットアップ
1. Raspberry Pi OSをセットアップ
2. インストール  
    ```
    curl -sSL https://get.pimoroni.com/grow | bash
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
