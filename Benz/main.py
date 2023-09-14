#!/usr/bin/env pybricks-micropython
from pybricks.nxtdevices import ColorSensor as ColorNxt
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (InfraredSensor, UltrasonicSensor)
from pybricks.parameters import Stop, Direction, Button
from pybricks.tools import wait, StopWatch, DataLog
import time
from modules.colors import *
#from pybricks.media.ev3dev import SoundFile, ImageFile


#!/usr/bin/env pybricks-micropython


# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

# The server must be started before the client!

from pybricks.messaging import BluetoothMailboxClient, TextMailbox
time.sleep(2)
# This is the name of the remote EV3 or PC we are connecting to.
while True:
  server = BluetoothMailboxServer()
  mbox = TextMailbox('greeting', server)
  # The server must be started before the client!
  print('waiting for connection...')
  server.wait_for_connection()
  connected = True
  print('connected!')
  # In this program, the server waits for the client to send the first message
  # and then sends a reply.
  mbox.wait()
  print(mbox.read())
  mbox.send('hello to you!')
  while connected:
    print(mbox.read())
    if mbox.read() == "True":
      print("checkando")
      txt = check()
      mbox.send(txt)
    elif mbox.read() == "End":
      mbox.close()
      connected = False

# In this program, the client sends the first message and then waits for the
# server to reply.




# green = calibration_auto(sensor_color, green)
# for i in range(100):
#   print(check())
#   time.sleep(1)
# #print(see())
# # while True:
# #   calibration(sensor_color)
# #   wait(1000)

# calibration_auto(sensor_color, brown)
