#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (InfraredSensor, UltrasonicSensor)
from pybricks.parameters import Stop, Direction, Button
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.messaging import BluetoothMailboxServer, TextMailbox

#from pybricks.media.ev3dev import SoundFile, ImageFile

from modules.motors import *
from modules.colors import *
from modules.detect import *
from modules.places import *
from modules.claw import *


'''server = BluetoothMailboxServer()
eve3box = TextMailbox('greeting', server)

print('waiting for connection...')
server.wait_for_connection()
print('connected!')

eve3box.wait()
print(ev3mbox.read())
eve3box.send('hello to you!')
'''

open_claw()
#open_claw_s(200)
#recognize_fisrt()

'''
while not saw_blue():
  move_forward(160)
stop()
'''


# turn_left(360)
# turn_left(360)
# turn_left(360)
    

#move_backward_cm(5)
#open_claw()
#close_claw()

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