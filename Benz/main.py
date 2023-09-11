#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (InfraredSensor, UltrasonicSensor)
from pybricks.parameters import Stop, Direction, Button
from pybricks.tools import wait, StopWatch, DataLog
import time
#from pybricks.media.ev3dev import SoundFile, ImageFile

from modules.motors import *
from modules.colors import *
from modules.detect import *
from modules.places import *
from modules.claw import *

#----------------------------------------------------------------------------------------------------------------------------------
#+close_claw(750)
#drugstore()
#Teste dos lugares

#school()
#turn_right(90)
#turn_left(90)

# enter()

#school()
#print(stack.lista)


#----------------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------#
#regular o giro
motors.turn(300)
while not blackRight() or not blackLeft():
  motors.turn(1)
motors.stop()
print(motor_left.angle(), motor_right.angle())

#----------------------------------------------------------------------#

#---------------------------------------------------------------------#


#-------------------------------------------------------------------------------------------------------
#calibrando cores 
#while True:
 # calibration(sensor_color_right)
  #calibration(sensor_color_left)
  #wait(3000)
#------------------------------------------------------------------------------------------------------
#calibration_auto(sensor_color_right, yell_i_black_left)

'''i = 0
while i < 5:
  turn_left(90)
  print("Virei")
  stop()
  wait(1000)
  i+=1
  
  '''

