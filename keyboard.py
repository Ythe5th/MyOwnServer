#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

L1 = 5
L2 = 6
L3 = 13
L4 = 19

C1 = 12
C2 = 16
C3 = 20
C4 = 21

GPIO.setwarnings( False )
GPIO.setmode( GPIO.BCM )

GPIO.setup( L1 , GPIO.OUT )
GPIO.setup( L2 , GPIO.OUT )
GPIO.setup( L3 , GPIO.OUT )
GPIO.setup( L4 , GPIO.OUT )

GPIO.setup( C1 , GPIO.IN , pull_up_down=GPIO.PUD_DOWN )
GPIO.setup( C2 , GPIO.IN , pull_up_down=GPIO.PUD_DOWN )
GPIO.setup( C3 , GPIO.IN , pull_up_down=GPIO.PUD_DOWN )
GPIO.setup( C4 , GPIO.IN , pull_up_down=GPIO.PUD_DOWN )

def readLine( line , characters , ret="" ):
    GPIO.output( line , GPIO.HIGH )
    if( GPIO.input( C1 ) == 1 ):
        ret = characters[0]
    if( GPIO.input( C2 ) == 1 ):
        ret = characters[1]
    if( GPIO.input( C3 ) == 1 ):
        ret = characters[2]
    if( GPIO.input( C4 ) == 1 ):
        ret = characters[3]
    GPIO.output( line , GPIO.LOW )
	return ret

def readlines( ret="" ):
	ret = readLine( L1, ["1","2","3","A"] )
	if ret != "":
		return ret
	ret = readLine( L2, ["4","5","6","B"] )
	if ret != "":
		return ret
	ret = readLine( L3, ["7","8","9","C"] )
	if ret != "":
		return ret
	ret = readLine( L4, ["*","0","#","D"] )
	return ret

try:
    while True:
        ch = readlines()
        if ch != "":
			print ch
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nApplication stopped!")
