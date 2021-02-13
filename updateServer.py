#!/usr/bin/env python
import os

FILE_NAME = "/tmp/MyOwnServer"
LOG_FILE = "/var/log/effesUpdate.log"
datetime = ""
endline  = " \n"
os.system( "git clone https://github.com/Ythe5th/MyOwnServer " + FILE_NAME )
FILE_NAME += "/updateServer.py"

f = open( LOG_FILE , "w" )
f.write( "STARTING UPDATE IN DATETIME : " + dateTime + endline )
f.close()
f = open( LOG_FILE , "a" )
if exists( FILE_NAME ):
	r = open( FILE_NAME , "r" )
	cmds = r.read().split( "\n" )
	r.close()
	for i in range( len( cmds ) ):
		if cmds[i] != "":
			f.append( "COMMAND N." + str( i ) + endline )
			f.append(  FILE_NAME + " 2>> " + LOG_FILE + endline )
			os.system( FILE_NAME + " 2>> " + LOG_FILE + endline )
f.close()
