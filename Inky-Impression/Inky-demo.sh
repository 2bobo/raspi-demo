#!/bin/bash

/usr/bin/python3 /usr/local/sbin/raspi-demo/Inky-Impression/view_images.py &
/usr/bin/sleep 30
view_pid=$(/usr/bin/pgrep -f view_images.py)

/usr/bin/python3 /usr/local/sbin/raspi-demo/Inky-Impression/create_image.py $view_pid &
