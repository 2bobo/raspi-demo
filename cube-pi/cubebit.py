# Python module for 4tronix Cube:Bit which is basically a port of the Makecode package
# Layered over the Adafruit neopixel library
# Install that following the instructions here: https://learn.adafruit.com/neopixels-on-raspberry-pi/software
# Cube:Bit available from shop.4tronix.co.uk

from rpi_ws281x import *

# Global settings
side = 5
side2 = side * side
side3 = side2 * side
cube = None
brightness = 40

def create (lside=3, lbrightness=40):
        global side, side2, side3, cube
        if (cube == None):
                side = lside
                side2 = side * side
                side3 = side2 * side
                brightness = lbrightness
                cube = Adafruit_NeoPixel(side3, 18, 800000, 5, False, brightness)
                cube.begin()

def cleanup():
        clear()
        show()

def map(x, y, z):
        q=0;
        if (x<side and y<side and z<side and x>=0 and y>=0 and z>=0):
            if ((z%2) == 0):
                if ((y%2) == 0):
                    q = y * side + x
                else:
                    q = y * side + side - 1 - x
            else:
                if ((side%2) == 0):
                    y = side - y - 1
                if ((x%2) == 0):
                    q = side * (side - x) - 1 - y
                else:
                    q = (side - 1 - x) * side + y
            return z*side2 + q
        return cubeSide3;    # return non-existent pixel for out of bounds
        

def setColor(color):
        for i in range(side3):
                setPixel(i, color)

def setPixel(ID, color):
        if (ID <= side3):
                cube.setPixelColor(ID, color)

def show():
        cube.show()

def clear():
        for i in range(side3):
                setPixel(i, 0)

def rainbow():
        i = 0
        for z in range(side):
                for y in range(side):
                        for x in range(side):
                                setPixel(map(x,y,z), wheel(i * 256 / side3))
                                i += 1

def fromRGB(red, green, blue):
        return ((int(red)<<16) + (int(green)<<8) + blue)

def toRGB(color):
        return (((color & 0xff0000) >> 16), ((color & 0x00ff00) >> 8), (color & 0x0000ff))

def wheel(pos):
	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return fromRGB(255 - pos * 3, pos * 3, 0) # Red -> Green
	elif pos < 170:
		pos -= 85
		return fromRGB(0, 255 - pos * 3, pos * 3) # Green -> Blue
	else:
		pos -= 170
		return fromRGB(pos * 3, 0, 255 - pos * 3) # Blue -> Red

def setPlane(plane, axis, color):
        if (axis == 0):
                for y in range(side):
                        for z in range(side):
                                setPixel(map(plane, y, z), color)
        elif (axis == 1):
                for x in range(side):
                        for z in range(side):
                                setPixel(map(x, plane, z), color)
        else:
                for x in range(side):
                        for y in range(side):
                                setPixel(map(x, y, plane), color)


                

