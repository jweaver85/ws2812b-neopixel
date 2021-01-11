import time
import board
import neopixel
import random
from collections import deque

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D21
sleepyTime = 0.05
STEP = 10 
bright = .1
num_pixels = 60
ORDER = neopixel.RGB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=bright, auto_write=False, pixel_order=ORDER)
DEQUE = deque([],num_pixels)

def rand():
  return int(255 * random.random())

def translate(start,end,stepSize):
  if start == end:
    return end
  elif start > end:
    if start-stepSize <= end:
      return end
    else:
      return start-stepSize
  else:
    if start+stepSize >= end:
      return end
    else:
      return start+stepSize

def render(c):
  DEQUE.append(c)
  if len(DEQUE) >= 60:
    i = 0
    for e in DEQUE:
      pixels[i] = e
      i = i+1
    pixels.show()
    time.sleep(sleepyTime)

def walk(c1, c2, stepSize):
  while (c1 != c2):
    c1= (translate(c1[0],c2[0],stepSize),translate(c1[1],c2[1],stepSize),translate(c1[2],c2[2],stepSize))
    #print(c1)
    render(c1)


start = (rand(), rand(), rand())
while True:
  end = (rand(), rand(), rand())
  walk(start,end,STEP)
  start = end
  #print('!!!!!!!finished walk!!!!!!!!!!')
