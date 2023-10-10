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
# from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import BluetoothMailboxClient, TextMailbox

#!/usr/bin/env pybricks-micropython

#####
SERVER = 'ev3dev'
ev3 = EV3Brick()
for i in range(20):
  ev3.speaker.beep(200)

client = BluetoothMailboxClient()
mbox = TextMailbox('greeting', client)

print('establishing connection...')
client.connect(SERVER)
print('connected!')

# In this program, the client sends the first message and then waits for the
# server to reply.
mbox.send('hello!')
mbox.wait()
print(mbox.read())

####
# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

# The server must be started before the client!


# time.sleep(2)
# This is the name of the remote EV3 or PC we are connecting to.
"""while True:
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
      connected = False"""


# In this program, the client sends the first message and then waits for the
# server to reply.
while True:
    print(mbox.read())
    txt = mbox.read()
    if  txt == "True":
      print("checkando")
      txt = check()
      mbox.send(txt)
    elif  txt == "verify":
      txt = verify()
      mbox.send(txt)


"""while True:
  test(green)
  print("#####################################")
  wait(5000)"""

"""rgb = [0,0,0]

calibration_auto(brown)
for i in range(10):
  aux = sensor_sup.rgb()
  print(aux)
  rgb[0] += aux[0]
  rgb[1] += aux[1]
  rgb[2] += aux[2]
  time.sleep(1)
print("rgb", rgb)
print("rgb", rgb/10)"""
# #print(see())
# # while True:
# #   calibration(sensor_color)
# #   wait(1000)

# for i in range(9):
#   print(check())
"""reflect = 0
# calibration_auto(sensor_color, brown)
for i in range(5):
  reflect += sensor_sup.reflection()
  print(reflect)
media = reflect/5
print(media) """


"""while True:
  test(sensor_color, brown)
  wait(1000)
"""