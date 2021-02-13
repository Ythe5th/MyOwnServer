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
  kp = keypad( columnCount = 3 )
  tolcd = ""
  keypressed = 0
  while True:
    digit = None
    while digit == None:
      digit = kp.getKey()
      if digit != None:
        print( digit )
        if keypressed:
          if digit == "#":
            tolcd += ";1"
            keypressed = 0
          elif digit == "*":
            if tolcd[-1] != ";":
              tolcd = tolcd[:-1]
            else:
              tolcd = ""
              keypressed = 0
          else:
            if ";" not in tolcd:
              tolcd += ";"
            tolcd += digit
        else:
          if digit == "#":
            tolcd = "Codice Funzione"
            keypressed = 1
          if digit == "*":
            tolcd = ""
        fpc( tolcd )
    time.sleep( 0.3 )
  '''
  while True:
    digit = None
    while digit == None:
        digit = kp.getKey()
        if digit != None:
            print( digit )
            if keypressed and ( digit != "#" or digit != "*" ):
              if ";" not in tolcd:
                tolcd += ";"
              tolcd += digit
            elif digit == "#":
              tolcd = "Codice Funzione"
              keypressed = 1
            if digit == "*":
              tolcd = ""
    fpc( tolcd )            
    time.sleep( 0.3 )
  '''
