import time
import board
import neopixel
import random
from collections import deque

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D21
sleepyTime = 0.05
STEP = 64 
bright = .1
num_pixels = 60 
ORDER = neopixel.RGB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=bright, auto_write=False, pixel_order=ORDER)
DEQUE = deque([],num_pixels)

RED = (0,255,0)
WHITE = (255,255,255)
BLUE = (0,0,255)


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
  if len(DEQUE) >= num_pixels:
    i = 0
    for e in DEQUE:
      pixels[i] = e
      i = i+1
    pixels.show()
    time.sleep(sleepyTime)

def walk(c1, c2, stepSize):
  if (c1 == c2) & (c1 != WHITE):
   render(c1)
  while (c1 != c2):
    c1= (translate(c1[0],c2[0],stepSize),translate(c1[1],c2[1],stepSize),translate(c1[2],c2[2],stepSize))
    #print(c1)
    render(c1)


while True:
  walk(RED,WHITE,STEP)
  walk(WHITE,BLUE,STEP)
  walk(BLUE,BLUE,STEP)
  walk(BLUE,WHITE,STEP)
  walk(WHITE,RED,STEP)
  walk(RED,RED,STEP)
  #print('!!!!!!!finished walk!!!!!!!!!!')
