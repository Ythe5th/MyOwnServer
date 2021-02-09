#!/usr/bin/env python3
import os

LOG_FILE = "/var/log/myownserver.log"
END_CMD = " 2> " + LOG_FILE + " && "
CMD_FILE = "/var/www/commands"
F = open( CMD_FILE , "r" )
cmds = F.read().split( "\n" )
F.close()
cmd = ""
os.system( "git clone" )

for c in range( len( cmds ) ):
  cmd += cmds[c] + END_CMD
cmd = cmd[:-4]
f = open( "/tmp/gitcmd" , "w" )
f.write( cmd )
f.close()
os.system( cmd )
'''
cmd = "mv www wwwold" + END_CMD
cmd+= "chown -R www-data:www-data www" + END_CMD
cmd+= "chmod -R 750 www" + END_CMD
'''

