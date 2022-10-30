import cubebit as cb
import time
import random

side = 3

side2 = side*side
cb.create(side)
rain = cb.fromRGB(255,0,255)
white = cb.fromRGB(255,255,255)
red = cb.fromRGB(255, 0, 0)

green = cb.fromRGB(0, 150, 0)
brown = cb.fromRGB(230, 150, 80)

star = cb.fromRGB(255, 255, 0)

colors = 10

cloud = [None]*side2


try:
    while True:
        cb.cleanup()
        cb.setPlane(side-1, 2, green)
        cb.setPlane(side-2, 2, green)
        cb.setPlane(side-3, 2, green)
        cb.setPixel(cb.map(1, 1, 2), star)

        cb.show()

        clr = cb.fromRGB(
            random.randint(0, 255 - 1),
            random.randint(0, 150 - 1),
            random.randint(0, 255 - 1)
        )

        print(clr)
        x = [0] * colors
        y = [0] * colors
        z = [0] * colors
        r = [0] * colors
        g = [0] * colors
        b = [0] * colors

        print(x)

        for i in range(colors):
            print(i)
            x[i] = random.randint(0, side - 1)
            y[i] = random.randint(0, side - 1)
            z[i] = random.randint(0, side - 1)

            r[i] = random.randint(0, 254)
            g[i] = random.randint(0, 150)
            b[i] = random.randint(0, 254)

        print(x)
        print(y)
        print(z)
        print(r)
        print(g)
        print(b)

        for (xx, yy, zz, rr, gg, bb) in zip(x, y, z, r, g, b):
            if xx == 1 and yy == 1 and zz == 2:
                zz = 0

            rn = 0
            gn = 150
            bn = 0

            while (rn != rr) or (gn != gg) or (bn != bb):
                if rn > rr:
                    rn -= 1
                elif rn < rr:
                    rn += 1
                else:
                    rn = rr

                if gn > gg:
                    gn -= 1
                elif gn < gg:
                    gn += 1
                else:
                    gn = gg

                if bn > bb:
                    bn -= 1
                elif bn < bb:
                    bn += 1
                else:
                    bn = bb

                cb.setPixel(
                    cb.map(xx, yy, zz),
                    cb.fromRGB(rn, gn, bn)
                )
                cb.show()
                time.sleep(0.005)
                #print("{rn}:{rr} / {gn}:{gg} / {bn}:{bb}".format(rn=rn, rr=rr, gn=gn, gg=gg, bn=bn, bb=bb))

        time.sleep(3)

        for (xx, yy, zz, rn, gn, bn) in zip(x, y, z, r, g, b):
            if xx == 1 and yy == 1 and zz == 2:
                zz = 0

            rr = 0
            gg = 150
            bb = 0

            while (rn != rr) or (gn != gg) or (bn != bb):
                if rn > rr:
                    rn -= 1
                elif rn < rr:
                    rn += 1
                else:
                    rn = rr

                if gn > gg:
                    gn -= 1
                elif gn < gg:
                    gn += 1
                else:
                    gn = gg

                if bn > bb:
                    bn -= 1
                elif bn < bb:
                    bn += 1
                else:
                    bn = bb

                cb.setPixel(
                    cb.map(xx, yy, zz),
                    cb.fromRGB(rn, gn, bn)
                )
                cb.show()
                time.sleep(0.01)
                #print("{rn}:{rr} / {gn}:{gg} / {bn}:{bb}".format(rn=rn, rr=rr, gn=gn, gg=gg, bn=bn, bb=bb))

        time.sleep(2)

except Exception as ex:
    print(ex)
finally:
    cb.cleanup()
