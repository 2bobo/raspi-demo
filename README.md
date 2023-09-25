# raspi-demo
RaspberryPi展示用の雑多なコード

## cube-pi
- 4tronixのCUBE:BITのデモ
- 3*3*3のLEDマトリクス表示

## stack-pi

## pirate

## OTG設定メモ
1. `/boot/config.txt`編集
   末尾に以下を追記
    ```
    dtoverlay=dwc2
    ```
2. `/boot/cmdline.txt`編集
   - 編集前(一度起動後の状態)
     ```
     console=serial0,115200 console=tty1 root=PARTUUID=67caab89-02 rootfstype=ext4 fsck.repair=yes rootwait
     ```
   - 編集後
     ```
     console=serial0,115200 console=tty1 root=PARTUUID=b1214a26-02 rootfstype=ext4 fsck.repair=yes rootwait modules-load=dwc2,g_ether
     ```

