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
#turn_left(90)
'''close_claw(750)
open_claw()
ev3.speaker.beep(200)'''
open_claw(500)
#wait(700)
recognize_first()
#open_claw()
#close_claw(10)
#while True:
#  move_forward(10*360)
 # print(seeRight())
  #print(seeLeft())3
  #wait(1000)'''
#turn_right_180()
#turn_left(90)
'''while not saw_blue():
    print("andando")
    move_forward(500)
stop()
wait(500)
turn_left(90)'''
'''
    
    if control_signal_right > 300:
        control_signal_right = 300

    if control_signal_left > 300:
        control_signal_left = 300
'''
#check_point()
#close_claw()


#close_claw(750)
#open_claw()
#drugstore()
#Teste dos lugares

#school()
#city_hall()
#library()
#bakery()
#drugstore()
#museum()



#turn_right(90)
#turn_left(90)

# enter()

#school()
#print(stack.lista)


#----------------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------#
#regular o giro
'''motors.turn(300)
while not blackRight() or not blackLeft():
  motors.turn(1)
motors.stop()
print(motor_left.angle(), motor_right.angle())'''

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
#turn_right1(90)
'''i = 0
while i < 5:
  turn_right(90)
  print("Virei")
  stop()
  wait(1000)
  i+=1
  
'''