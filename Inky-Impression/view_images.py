#!/usr/bin/env python3

import sys
import signal
import os
import random
import csv
import datetime

from PIL import Image
import RPi.GPIO as GPIO
from inky.auto import auto

inky = auto(ask_user=True, verbose=True)
saturation = 0.5

# Gpio pins for each button (from top to bottom)
BUTTONS = [5, 6, 16, 24]

# These correspond to buttons A, B, C and D respectively
LABELS = ['A', 'B', 'C', 'D']

image_dir = "/var/raspi_create_pict/image"


def view_image(image_file):

    image = Image.open(image_file)
    resizedimage = image.resize(inky.resolution)

    inky.set_image(resizedimage, saturation=saturation)
    inky.show()


def get_latest_file(directory):
    # ディレクトリ内のすべてのエントリ（ファイルとサブディレクトリ）を取得
    entries = os.listdir(directory)

    # ディレクトリ内のファイルのみをフルパスで取得し、最新のファイルを見つける
    files = [os.path.join(directory, entry) for entry in entries if os.path.isfile(os.path.join(directory, entry))]

    if not files:
        return None  # ディレクトリ内にファイルが存在しない場合はNoneを返す

    # 更新日時の降順にファイルをソートし、最新のファイルを取得
    latest_file = max(files, key=os.path.getmtime)

    return latest_file


def get_random_file(directory):
    # ディレクトリ内のすべてのエントリ（ファイルとサブディレクトリ）を取得
    entries = os.listdir(directory)

    # ディレクトリ内のファイルのみをフルパスで取得
    files = [os.path.join(directory, entry) for entry in entries if os.path.isfile(os.path.join(directory, entry))]

    if not files:
        return None  # ディレクトリ内にファイルが存在しない場合はNoneを返す

    # ファイルリストからランダムに1つを選択
    random_file = random.choice(files)

    return random_file


def handle_button(pin):
    label = LABELS[BUTTONS.index(pin)]
    if label == "A":
        _image_file_path = get_latest_file(image_dir)
        view_image(_image_file_path)
    elif label == "B":
        _image_file_path = get_random_file(image_dir)
        view_image(_image_file_path)
    elif label == "C":
        bookmark_csv = "/var/raspi_create_pict/bookmark.csv"
        log_time = datetime.datetime.now()
        log_str_date = log_time.strftime("%Y%m%d_%H%M%S")

        with open(bookmark_csv, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([log_str_date, _image_file_path])
    elif label == "D":
        _image_file_path = "/usr/local/sbin/raspi-demo/Inky-Impression/sample.png"
        view_image(_image_file_path)


def custom_signal_handler(sig, frame):
    _image_file_path = get_latest_file(image_dir)
    view_image(_image_file_path)


if __name__ == "__main__":
    image_file_path = "/usr/local/sbin/raspi-demo/Inky-Impression/sample.png"
    view_image(image_file_path)
    print("""buttons.py - Detect which button has been pressed

    This example should demonstrate how to:
     1. set up RPi.GPIO to read buttons,
     2. determine which button has been pressed

    Press Ctrl+C to exit!

    """)

    # Set up RPi.GPIO with the "BCM" numbering scheme
    GPIO.setmode(GPIO.BCM)

    # Buttons connect to ground when pressed, so we should set them up
    # with a "PULL UP", which weakly pulls the input signal to 3.3V.
    GPIO.setup(BUTTONS, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # Loop through out buttons and attach the "handle_button" function to each
    # We're watching the "FALLING" edge (transition from 3.3V to Ground) and
    # picking a generous bouncetime of 250ms to smooth out button presses.
    for pin in BUTTONS:
        GPIO.add_event_detect(pin, GPIO.FALLING, handle_button, bouncetime=250)

    # SIGUSR1シグナルに対してカスタムハンドラを設定
    signal.signal(signal.SIGUSR1, custom_signal_handler)

    print("Waiting for SIGUSR1 signal. You can send it using 'kill -SIGUSR1 <pid>'")

    # アイドル中にプロセスを保つ
    while True:
        try:
            signal.pause()  # シグナルを待機
        except KeyboardInterrupt:
            print("Exiting...")
            break
