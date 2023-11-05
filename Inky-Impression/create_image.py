#!/usr/bin/env python3

import datetime
import random
import os
import sys
import csv

import psutil
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler

model_id = "stabilityai/stable-diffusion-2"
scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, low_cpu_mem_usage=True)
pipe = pipe.to("cpu")

words = ["Super Cat", "Space Cat", "cat", "python", "SF", "robot", "apple", "star", "tree", "tank", "window",
         "sea", "Pikachu", "Dinosaur", "banana"]
types = ["Pixer", "Vincent Van Gogh", "Emile Galle", "gothic", "Katsuhika Hokusai", "Pablo Picasso", "Doraemon",
         "Ink Wash Painting", "anime", "Pixel Art", "Edo Period", "Stick Figure"]

save_dir = "/var/raspi_create_pict/"
image_dir = os.path.join(save_dir, "image")
csv_file = os.path.join(save_dir, "log.csv")


def create_image(_view_script_pid):
    start_time = datetime.datetime.now()
    main_word = random.choice(words)
    main_type = random.choice(types)
    steps = random.randint(28, 50)
    prompt = f"{main_word}. not a photo. not use frame. use color only black, white, red, green, blue, yellow, " \
             f"orange. {main_type}"
    image = pipe(prompt, num_inference_steps=steps, height=448, width=640).images[0]
    end_date = datetime.datetime.now()
    create_date = end_date.strftime("%Y%m%d_%H%M%S")
    file_name = f"{create_date}-{main_word.replace(' ', '')}_{main_type.replace(' ', '')}.png"
    image.save(os.path.join(image_dir, file_name))
    with open(csv_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([start_time, end_date, main_word, main_type, steps])

    # プロセスのPIDを指定
    target_pid = _view_script_pid  # 送信先のプロセスPIDを指定

    # SIGUSR1シグナルを送信
    #try:
    #    os.kill(target_pid, signal.SIGUSR1)
    #    # print("SIGUSR1 signal sent to process with PID:", target_pid)
    #except OSError as e:
    #    print("Error sending SIGUSR1 signal:", e)


if __name__ == "__main__":
    view_script_pid = int(sys.argv[1])
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    while True:
        create_image(view_script_pid)
