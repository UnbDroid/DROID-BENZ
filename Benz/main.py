#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (InfraredSensor, UltrasonicSensor)
from pybricks.parameters import Stop, Direction, Button
from pybricks.tools import wait, StopWatch, DataLog

#from pybricks.media.ev3dev import SoundFile, ImageFile

from modules.motors import *
from modules.colors import *
from modules.detect import *
from modules.places import *
from modules.claw import *

#turn_right(90)
#recognize_first2()
#move_forward(200)

#while True:
 # move_forward_pid(360*10)
#Abrir e fechar a garra

#close_claw(100)
#open_claw(750)
#turn_right(90)
#recognize_first2()


#Declaração de variáveis globais e objetos

#----------------------------------------------------------------------------------------------------------------------------------

#Programa principal (minúsuclo pq é o programa principal lmfao)

#school()
#
# 
#turn_left(90)
#move_forward_cm(90)

# reposition("Blue")
#turn_90_left()
#command_stack()
#move_forward_cm(30)
#turn_left(90)
#move_forward_cm(30)
#turn_left(90)
#stack.reverse()

#----------------------------------------------------------------------#
#regular o giro

motors.turn(330)
while not blackRight() or not blackLeft():
   motors.turn(1)
motors.stop()
print(motor_left.angle(), motor_right.angle())

#----------------------------------------------------------------------#

'''

motors.turn(90)

wait(500)
print(motor_left.angle())
print(motor_right.angle())
print("a")
turn_left(90)


'''
#turn_right(90)
#wait(2000)
'''
i = 0
while i < 2:
  turn_right(90)
#  motors.turn(360)
  stop()
  wait(500)
  i+=1
stop()
#reposition_wall()
'''
'''
#---------------------------------------------------------------------#


#-------------------------------------------------------------------------------------------------------
#calibrando cores 
#while True:
 # calibration(sensor_color_right)
  #calibration(sensor_color_left)
  #wait(3000)
#------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------#
#teste do time


tempo = StopWatch()
print(tempo.time())
print(tempo.reset())
time.sleep(2)
print(tempo.time())

'''
#---------------------------------------------------------------------#


# museum2()
# move_forward_cm(12)
# turn_left(90)
# move_forward_cm(150)
#print(stack.lista)
#stack.reverse()
#print(stack.lista)