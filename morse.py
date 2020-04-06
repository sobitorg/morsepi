#!/usr/bin/python

import time
from sense_hat import SenseHat

sense = SenseHat()

duration = 0.5 # length of the dot duration in seconds

on = (255, 255, 255) # on state colour
off = (0, 0, 0) # off state colour
red = (255, 0, 0)

def dot():
   sense.clear(on)
   time.sleep(duration)
   sense.clear(off)
   time.sleep(duration)

def dash():
   sense.clear(on)
   time.sleep(duration * 4)
   sense.clear(off)
   time.sleep(duration)

def space():
   sense.clear(red)
   time.sleep(duration * 3)
   sense.clear(off)
   
code = {
   'A': '.-',     'B': '-...',   'C': '-.-.', 
   'D': '-..',    'E': '.',      'F': '..-.',
   'G': '--.',    'H': '....',   'I': '..',
   'J': '.---',   'K': '-.-',    'L': '.-..',
   'M': '--',     'N': '-.',     'O': '---',
   'P': '.--.',   'Q': '--.-',   'R': '.-.',
   'S': '...',    'T': '-',      'U': '..-',
   'V': '...-',   'W': '.--',    'X': '-..-',
   'Y': '-.--',   'Z': '--..',
   '0': '-----',  '1': '.----',  '2': '..---',
   '3': '...--',  '4': '....-',  '5': '.....',
   '6': '-....',  '7': '--...',  '8': '---..',
   '9': '----.'
}
   
#msg = raw_input('Message: ')

msg = " o p e r a t i o n   a n v i l "
for char in msg:
   if char.upper() in code:
      output = code[char.upper()]
      for char in output:
         if char == '.':
            dot()
         elif char == '-':
            dash()
   elif char == ' ':
      space()
