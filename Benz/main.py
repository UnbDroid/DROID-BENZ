#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (InfraredSensor, UltrasonicSensor)
from pybricks.parameters import Stop, Direction, Button
from pybricks.tools import wait, StopWatch, DataLog
#from pybricks.media.ev3dev import SoundFile, ImageFile

#!/usr/bin/env pybricks-micropython


# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

# The server must be started before the client!

from pybricks.messaging import BluetoothMailboxClient, TextMailbox

# This is the name of the remote EV3 or PC we are connecting to.
SERVER = 'ev3dev'

client = BluetoothMailboxClient()
mbox = TextMailbox('greeting', client)

print('establishing connection...')
client.connect(SERVER)
print('connected!')

# In this program, the client sends the first message and then waits for the
# server to reply.
while True:
  mbox.wait()
  if mbox.read() == "True":
    mbox.send(check())