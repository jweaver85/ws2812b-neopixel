import time
import board
import neopixel
import random
from collections import deque

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D21
sleepyTime = 0.01
bright = .5
num_pixels = 60
ORDER = neopixel.RGB
RED = (0,255,0)
OFF = (0,0,0)
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=bright, auto_write=False, pixel_order=ORDER)

while True:
  pixels.fill(OFF)
  index1 = 0
  index2 = num_pixels - 1
  for i in range(num_pixels):
    pixels.fill(OFF)
    pixels[index1%num_pixels] = RED
    pixels[index2%num_pixels] = RED
    index1 = index1 + 1
    index2 = index2 - 1
    pixels.show()
    time.sleep(sleepyTime)
