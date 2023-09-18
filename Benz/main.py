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
#museum()
#open_claw(780)
#open_claw(720)
#turn_right(90)
#array = [1, 2, 3]
#calibration_auto(sensor_color_left, array)
'''close_claw(750)
open_claw()
ev3.speaker.beep(200)'''
#close_claw(750)
#wait(700)
#recognize_first()
#school()
#move_backward_cm(60)
#moving_backward_cm(60)

'''while not saw_blue():
    print("andando")
    move_forward(500)
stop()
wait(500)
turn_left(90)'''
#turn_left(90)
'''
    
    if control_signal_right > 300:
        control_signal_right = 300

    if control_signal_left > 300:
        control_signal_left = 300
'''
#check_point()
#close_claw()
'''Teste para andar em cm
motor_left.run_angle(280, 1872,  wait=False)
motor_right.run_angle(280, 1872,  wait=True)
print("Esquerdo", (motor_left.angle()))
print("Direito", (motor_right.angle()))
'''
#close_claw(750)
#open_claw()
#drugstore()
#Teste dos lugares
#turn_right(360)
school()
#city_hall()
#library()
#bakery()
#drugstore()
#museum()





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
'''array = [[57,7,0],[78,27,25]]
while True:
  print("R")
  calibration_auto(sensor_color_right, array)
  print("L")
  calibration_auto(sensor_color_left, array)
  wait(3000)'''
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

'''
while True:
  print(message())
  wait(1000)'''