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
mbox.send('hello!')
mbox.wait()
print(mbox.read())


# from modules.motors import *
# from modules.colors import *
# from modules.detect import *
# from modules.places import *
# from modules.claw import *
# import time

#Declaração de variáveis globais e objetos

#----------------------------------------------------------------------------------------------------------------------------------

#Programa principal (minúsuclo pq é o programa principal lmfao)
#close_claw()
#motors.turn(180)
#print("rodei")
# while True:

#    circle_right()
#recognize_fisrt()
# reposition("Blue")
#turn_90_left()
#move_forward_cm(60)
#i = 0
#while i < 10:
#print(motors.distance_control.pid())
#while True:
 #  print(saw_blue())
   #calibrate()
   #i+=1
     #calibration(sensor_color_left)
     #calibration(sensor_color_right)
#    # teste_cor()
 #  print(saw_brown())
    #time.sleep(1)


#while True:
 # print("diretinha", seeRight())
  #print("lula",  seeLeft())
  #time.sleep(1)