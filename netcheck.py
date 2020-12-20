#! /usr/bin/env python3

import socket
import time
from dateutil import parser, tz
from datetime import datetime
import time

REMOTE_SERVER = "1.1.1.1"
FILE_PATH= "/home/admin/Desktop/netcheck.log"
FILE = open(FILE_PATH, 'w', buffering=1)
TIMEZONE="Europe/Zurich"

def is_connected(hostip):
  try:
    s = socket.create_connection((hostip, 80), 100)
    s.close()
    return "pass"
  except:
    pass
  return "nopass"

def checkUntil(endTime):
  print('check on remote ip: ' + REMOTE_SERVER + '\n')
  FILE.write('check on remote ip: ' + REMOTE_SERVER + '\n')

  while isExitTimeReached(endTime) == False:
    time.sleep(0.25)
    mydate=datetime.now(tz=tz.tzlocal())
      
    try:
      if is_connected(REMOTE_SERVER) != "pass":
        print('no internet', mydate.strftime("%Y-%m-%d %H:%M:%S-%f") + '\n')
        FILE.write('[ERROR] check ' + mydate.strftime("%Y-%m-%d %H:%M:%S-%f") + '\n')  # python will convert \n to os.linesep
      else:
        print('[OK] check at ' + mydate.strftime("%Y-%m-%d %H:%M:%S-%f") + '\n')
        FILE.write('[OK] check ' + mydate.strftime("%Y-%m-%d %H:%M:%S-%f") + '\n')
    except:
      FILE.close()
      break
  FILE.close()

def isExitTimeReached(mydatetime):
  PYCON_DATE = parser.parse(mydatetime)
  PYCON_DATE = PYCON_DATE.replace(tzinfo=tz.gettz(TIMEZONE))
  now = datetime.now(tz=tz.tzlocal())

  countdown = PYCON_DATE - now
  if(countdown.total_seconds() <= 0):
    print("end time reached, exit ...")
    FILE.write('end time reached, exit...')
    return True
  return False

checkUntil("Dec 20, 2021 0:30 AM")
