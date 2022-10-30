import cubebit as cb
import time

side = 5

cb.create(side)

try:
    cb.rainbow()
    cb.show()
    time.sleep(50)
    while True:
        for z in range (side):
            for y in range(side):
                for x in range(side):
                    cb.clear()
                    cb.setPixel(cb.map(x,y,z), cb.fromRGB(255,255,0))
                    cb.show()
                    time.sleep(0.2)
except Exception as ex:
    print (ex)
    print
finally:
    cb.cleanup()
    
