#!/usr/bin/env python3
#mkdir keypad-rpi && cd keypad-rpi

import time
import RPi.GPIO as GPIO
from keypad import keypad

GPIO.setwarnings(False)

def fpc( str ):# file_put_contents
  f = open( "/var/www/lcd" , "w" )
  f.write( str )
  f.close()

if __name__ == '__main__':
  # Initialize
  kp = keypad(columnCount = 3)
  # waiting for a keypress
  digit = None
  while digit == None:
    digit = kp.getKey()
  # Print result
  print( digit )
  if digit == "*":
    if keypressed:
      fpc( "1" )
    keypressed = 1 - keypressed
  time.sleep(0.5)
'''
###### 4 Digit wait ######
seq = []
for i in range(4):
digit = None
while digit == None:
digit = kp.getKey()
seq.append(digit)
time.sleep(0.4)

# Check digit code
print(seq)
    if seq == [1, 2, 3, '#']:
        print( "Code accepted" )
    '''
