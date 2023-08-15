#!/usr/bin/env pybricks-micropython
from pybricks.nxtdevices import ColorSensor as ColorNxt
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (InfraredSensor, UltrasonicSensor)
from pybricks.parameters import Stop, Direction, Button
from pybricks.tools import wait, StopWatch, DataLog
import time
#from pybricks.media.ev3dev import SoundFile, ImageFile


#!/usr/bin/env pybricks-micropython


# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

# The server must be started before the client!

from pybricks.messaging import BluetoothMailboxClient, TextMailbox
time.sleep(2)
# This is the name of the remote EV3 or PC we are connecting to.
SERVER = 'ev3dev'
print("tentando ;)")
client = BluetoothMailboxClient()
mbox = TextMailbox('greeting', client)

print('establishing connection...')
client.connect(SERVER)
print('connected!')
mbox.send("Hello")


# In this program, the client sends the first message and then waits for the
# server to reply.
from modules.colors import *
while True:
  print(mbox.read())
  if mbox.read() == "True":
    print("checkando")
    txt = check()
    mbox.send(txt)

#print(see())
# while True:
#   print(check())
#   wait(1000)
