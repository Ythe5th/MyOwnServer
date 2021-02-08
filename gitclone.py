#!/usr/bin/env python3
import os

LOG_FILE = "/var/log/myownserver.log"
END_CMD = " 2> " + LOG_FILE + " && "

os.system( "git clone" )

cmd = "mv www wwwold" + END_CMD
cmd+= "chown -R www-data:www-data www" + END_CMD
cmd+= "chmod -R 750 www" + END_CMD
os.system( cmd )
