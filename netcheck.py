#! /usr/bin/env python3

import socket
import time
from dateutil import parser, tz
from datetime import datetime
import time

#configuration
LOG_MODE=2 #1:ERROR, 2:TRACE
CONSOLE_LOG=True
SLEEP_TIMER=0.25
CONNECTION_TRY=1000

#parameters
TIMEZONE="Europe/Zurich"
CHECKUNTIL_TIME="Dec 20, 2021 0:30 AM"
REMOTE_SERVER_DNS = "one.one.one.one"
REMOTE_SERVER_IP = "1.1.1.1"
REMOTE_SERVER_PORT = "80" #HTTP
REMOTE_SERVER_RETRYTIME = 1
FILE_PATH= "/home/admin/Desktop/netcheck.log"

def logging_error(msg):
  if LOG_MODE >= 1:
    mydate=datetime.now(tz=tz.tzlocal())
    FILE.write('[ERROR] '+ mydate.strftime("%Y-%m-%d %H:%M:%S-%f") + ', ' + msg + '\n')
    if CONSOLE_LOG == True:
      print('[ERROR] '+ mydate.strftime("%Y-%m-%d %H:%M:%S-%f") + ', ' + msg + '\n')
    
def logging_trace(msg):
  if LOG_MODE >= 2:
    mydate=datetime.now(tz=tz.tzlocal())
    FILE.write('[TRACE] ' + mydate.strftime("%Y-%m-%d %H:%M:%S-%f") + ', ' + msg + '\n')
    if CONSOLE_LOG == True:
      print('[TRACE] ' + mydate.strftime("%Y-%m-%d %H:%M:%S-%f") + ', ' + msg + '\n')

def is_connected(hostip, port, retryTime):
  try:
    s = socket.create_connection((hostip, port), retryTime)
    s.close()
    logging_trace("socket opened, connection established and socket closed")
  except socket.error as exc:
    logging_error("OSError: {0}".format(exc))
    return False
  return True

def isExitTimeReached(mydatetime):
  PYCON_DATE = parser.parse(mydatetime)
  PYCON_DATE = PYCON_DATE.replace(tzinfo=tz.gettz(TIMEZONE))
  now = datetime.now(tz=tz.tzlocal())
  countdown = PYCON_DATE - now
  if(countdown.total_seconds() <= 0):
    logging_trace("end time reached, exit ...")
    return True
  return False

def checkUntil(endTime, checkIp, checkPort, checkRetryTime):
  logging_trace('check remote ip: ' + checkIp)

  while isExitTimeReached(endTime) == False:
      is_connected(checkIp, checkPort, checkRetryTime)
      time.sleep(SLEEP_TIMER)

#Program entrypoint
FILE = open(FILE_PATH, 'a', buffering=1)
checkUntil(CHECKUNTIL_TIME, REMOTE_SERVER_IP, REMOTE_SERVER_PORT, REMOTE_SERVER_RETRYTIME)
FILE.close()