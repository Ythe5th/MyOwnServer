#!/usr/bin/env python
import I2C_LCD_driver
import socket
import fcntl
import struct
import time
import os

LCD = I2C_LCD_driver.lcd()

def get_ip_address( ifname ):
   s = socket
   
def fgc( fileName='/var/www/lcd' ):# file_get_contents
  f = open( fileName , "r" )
  ret = f.read()
  f.close()
  return ret
  
def fpc( str ):# file_put_contents
  f = open( "/var/www/lcd" , "w" )
  f.write( str )
  f.close()
  
def adaptMsg( msg , charNumber=16 ):
   while len( msg ) < 16:
      msg += " "
   return msg
   
while True:
   lcd = fgc().strip( "\n\t " ).split( ";" )
   LCD.lcd_display_string( adaptMsg( lcd[0] ) , 1 )
   if len( lcd ) > 1:
      LCD.lcd_display_string( adaptMsg( lcd[1] ) , 2 )
      if ( len( lcd ) > 2 ) and ( lcd[2] == '1' ):
         if lcd[1] == "00":#Update Effes
            updateFile = "/var/www/updateServer.py"
            if exists( updateFile ):
               os.system( "python " + updateFile )
               fpc( "Aggionamento" )
            else:
               fpc( "Errore:;File Agg. Assente" )
         elif lcd[1] == "10":#lighttpd stop
            os.system( "/etc/init.d/lighttpd stop" )
            fpc( "Server Stopped" )
         elif lcd[1] == "11":#lighttpd start
            os.system( "/etc/init.d/lighttpd start" )
            fpc( "Server Started" )
         elif lcd[1] == "12":#lighttpd restart
            os.system( "/etc/init.d/lighttpd restart" )
            fpc( "Server ReStarted" )
         elif lcd[1] == "13":#lighttpd status
            os.system( "/etc/init.d/lighttpd status" )
            fpc( "Server Status;Ok" )
         else:
            fpc( "Comando Non;Riconosciuto" )
   else:
      LCD.lcd_display_string( adaptMsg( ' ' ) , 2 )
   if lcd[0] == "":
      data = "data"
      ora  = "ora"
      fpc( data + ";" + ora )
   time.sleep( 0.01 )
