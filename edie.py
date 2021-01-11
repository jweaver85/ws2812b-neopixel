import time
import board
import neopixel
import random
from collections import deque

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D21
sleepyTime = 0.09
bright = .05
num_pixels = 60
ORDER = neopixel.RGB
RED = (0,255,0)
PURPLE = (0,125,184)
CYAN = (190,51,214)
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=bright, auto_write=False, pixel_order=ORDER)
colors = [PURPLE,RED,CYAN,PURPLE,PURPLE,RED,CYAN,PURPLE,RED,CYAN,PURPLE,RED,CYAN,PURPLE,RED,CYAN,PURPLE,RED,CYAN,PURPLE,
        RED,CYAN,PURPLE,RED,CYAN,PURPLE,RED,CYAN,PURPLE,RED,CYAN,PURPLE,RED,CYAN,PURPLE,RED,CYAN,PURPLE,RED,CYAN,
        PURPLE,RED,CYAN,PURPLE,RED,CYAN,PURPLE,RED,CYAN,PURPLE,RED,CYAN,PURPLE,RED,CYAN,PURPLE,RED,CYAN,PURPLE,RED]
def shiftLeft(arr):
  arr.append(arr.pop(0))
 
def shiftRight(arr):
  arr.insert(0, arr.pop(len(arr)-1))

def arrayShift():
  while True:
    # SHIFT RIGHT
    colors.insert(0, colors.pop(len(colors)-1))
    
    # SHIFT LEFT
    # colors.append(colors.pop(0))
    
    # UPDATE PIXELS
    for i in range(num_pixels):
      pixels[i] = colors[i]
    pixels.show()
    time.sleep(sleepyTime)


def dequeShift():
  dequeColors = deque(colors,num_pixels)
  while True:
    dequeColors.append(dequeColors.popleft())
    i = 0
    for color in dequeColors:
      pixels[i] = color
      i+=1
    pixels.show()
    time.sleep(sleepyTime)

#dequeShift()
arrayShift()

