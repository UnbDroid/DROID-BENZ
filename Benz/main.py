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
#Funções iniciais
### recognize_first() arrumar a logica.!!!
recognize()
#recognize_first() ## Função inicial até o azul
#open_claw()
#while True:
'''  test(sensor_color_left, white_left)
  wait(2000)'''

# find_passenger() scanneamento
#check_point() vai pro check point( VERMELHO )
#decision(tube) Vai entregar o tubo

#----------------------------------------------------------------------------------------------------------------------------------
#Teste para andar em cm

'''motor_left.run_angle(280, -360,  wait=False)
motor_right.run_angle(280, -360~,  wait=True)
print("Esquerdo", (motor_left.angle()))
print("Direito", (motor_right.angle()))
'''


#----------------------------------------------------------------------------------------------------------------------------------
#Teste dos lugares

#school()
#city_hall()
#library()
#bakery()
#drugstore()
#museum()
#park()


#----------------------------------------------------------------------------------------------------------------------------------
#Teste básicos

#reposition_wall()
#reposition("Red")
#open_claw()
#close_claw(700)

#turn_right(90)
#turn_left(90)
#move_forward_cm(60)
#move_backward_cm(60)


'''while not saw_black():
  move_forward(500)

stop()'''

#----------------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------#
#regular o giro
#boa sorte :D
#stop()
#regular()
#802

'''regulagem = [0,0]
for i in range(4):
  aux = regular()
  regulagem[0]+=aux[0]/(i+1)
  regulagem[1] += aux[1]/(i+1)
  print(aux)
  wait(4000)
regulagem[0] = regulagem[0]/4
regulagem[1] = regulagem[1]/4
print("real oficial ",regulagem)'''
#----------------------------------------------------------------------#

#---------------------------------------------------------------------#


#-------------------------------------------------------------------------------------------------------
#calibrando cores 
"""array = [[57,7,0],[78,27,25]]
while True:
  print("R")
  calibration_auto(sensor_color_right, array)
  print("L")
  calibration_auto(sensor_color_left, array)
  wait(3000)"""
#------------------------------------------------------------------------------------------------------
#treinar kp e ki
'''i = 0
while i <= 0 :
  #turn_left(90)
  turn_right(90)
  print("Virei")
  stop()
  wait(10000)
  i+=1
  '''
#------------------------------------------------------------------------------------------------------

#teste para andar
'''stop_motors()
move_backward_cm(60)
stop_motors()'''
'''print(motor_left.angle())
print(motor_right.angle())
move_forward_cm(15)
print("###############")
print(motor_left.angle())
print(motor_right.angle())
print("###############")
stop_motors()
print(motor_left.angle())
print(motor_right.angle())
'''

#teste de reposicionar
# stop()
# while not saw_black():
#   move_forward(330)
# stop()
#move_backward_cm(0.5)
# reposition("Black")
# '''
#reposition("Blue")
# while True:
#   test(sensor_color_left,blue_i_white_left)
#   wait(2000)

'''while True:
  obstacle("frente")
  print(ultra_sensor.distance())
  wait(5000)'''

# while True:
#   move_backward(800)
# calibration_auto(sensor_color_right, white_right)
# [16, 39, 65]

#enter()