import time
import board
import neopixel
import random
from collections import deque

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D21
sleepyTime = 0.05
bright = .1
num_pixels = 60
ORDER = neopixel.RGB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=bright, auto_write=False, pixel_order=ORDER)
RED = (0,255,0)
BLUE = (0,0,255)
OFF = (0,0,0)

def flicker(color1, color2,interval,n):
    for i in range(n):
        pixels.fill(color1)
        pixels.show()
        time.sleep(interval)
        pixels.fill(color2)
        pixels.show()
        time.sleep(interval)


while True:
  pixels.fill(BLUE)
  pixels.show()
  time.sleep(.5)
  flicker(RED,OFF,.25,5)

  flicker(RED,BLUE,.25,5)

  pixels.fill(RED)
  pixels.show()
  time.sleep(.5)
  flicker(BLUE,OFF,.25,5)

  flicker(RED,BLUE,.25,5)
