import cubebit as cb
import time
import random

side = 5

side2 = side*side
cb.create(side)
rain = cb.fromRGB(255,0,255)
white = cb.fromRGB(255,255,255)
cloud = [None]*side2

try:
    while True:
        cb.clear()
        cb.setPlane(side-1, 2, rain)
        cb.show()
        time.sleep(1)
        cb.setColor(white)
        cb.show()
        time.sleep(0.05)
        cb.clear()
        cb.setPlane(side-1,2,rain)
        cb.show()
        for i in range(side2):
            cloud[i] = 0
        for k in range(side2):
            x = random.randint(0,side-1)
            y = random.randint(0,side-1)
            while (cloud[x+y*side] != 0):
                x = random.randint(0,side-1)
                y = random.randint(0,side-1)
            cloud[x + y*side] = 1
            for i in range(side-1):
                cb.setPixel(cb.map(x,y,side-1-i), 0)
                cb.setPixel(cb.map(x,y,side-2-i), rain)
                cb.show()
                time.sleep(0.2)
        time.sleep(1)
        for y in range(side-1):
            for x in range(side):
                cb.setPixel(cb.map(x, side-y-1, 0), 0)
                cb.setPixel(cb.map(x, 0, y+1), rain)
            cb.show()
            time.sleep(0.2)
        for y in range(side-1):
            for x in range(side):
                cb.setPixel(cb.map(x, 0, y), 0)
                cb.setPixel(cb.map(x, y+1, side-1), rain)
            cb.show()
            time.sleep(0.2)
        time.sleep(1)
except Exception as ex:
    print ex
    print
finally:
    cb.cleanup()
    
