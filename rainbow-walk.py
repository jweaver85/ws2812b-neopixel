import time
import board
import neopixel
import random
from collections import deque

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D21
sleepyTime = 0.01
STEP = 27 
bright = .1
num_pixels = 60 
ORDER = neopixel.RGB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=bright, auto_write=False, pixel_order=ORDER)
DEQUE = deque([],num_pixels)

COLOR01 = (255,0,0)
COLOR02 = (255,85,0)
COLOR03 = (255,230,0)
COLOR04 = (0,255,0)
COLOR05 = (0,255,68)
COLOR06 = (0,255,208)
COLOR07 = (0,110,255)
COLOR08 = (0,0,255)
COLOR09 = (157,0,255)
COLOR10 = (255,0,200)


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
  while (c1 != c2):
    c1= (translate(c1[0],c2[0],stepSize),translate(c1[1],c2[1],stepSize),translate(c1[2],c2[2],stepSize))
    #print(c1)
    render(c1)


while True:
  walk(COLOR01,COLOR02,STEP)
  walk(COLOR02,COLOR03,STEP)
  walk(COLOR03,COLOR04,STEP)
  walk(COLOR04,COLOR05,STEP)
  walk(COLOR05,COLOR06,STEP)
  walk(COLOR06,COLOR07,STEP)
  walk(COLOR07,COLOR08,STEP)
  walk(COLOR08,COLOR09,STEP)
  walk(COLOR09,COLOR10,STEP)
  walk(COLOR10,COLOR01,STEP)
  #print('!!!!!!!finished walk!!!!!!!!!!')
