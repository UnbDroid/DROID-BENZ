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
#school()
# while True:
#   move_forward(380)
#enter()
#recognize()
# turn_right(90)
# reposition()
#-------------------------------------------------------------------------------------------------------

'''while recognize():
   print("Buscando passageiro")
   find_passenger() #scanneamento
   tubo = check_point() #vai pro check point( VERMELHO )
   print("Opa vou ver")
   decision(tubo) #Vai entregar o tubo  #print("Cor preto")'''
   
''' print("RGB do direito")
  calibration_auto(sensor_color_right, array)
  print("RGB do esquerdo")
  calibration_auto(sensor_color_left, array)
  wait(3000)
'''

#black e yellow right
'''Devolvendo os valores
[[1, 9, 3], [17, 25, 19]]
L
Calibrando as cores
Devolvendo os valores
[[52, 71, 4], [68, 87, 20]]
#black e yellow left
Calibrando as cores
Devolvendo os valores
[[6, 9, 1], [22, 25, 17]]
R
Calibrando as cores
Devolvendo os valores
[[34, 63, 11], [50, 79, 27]]
L'''



#calibrando cores 
"""array = [[57,7,0],[78,27,25]]
while True:
  print("R")
  calibration_auto(sensor_color_right, array)
  print("L")
  calibration_auto(sensor_color_left, array)
  wait(3000)"""
#coloque o valor aqui do azul = Direito: [[0, 10, 34], [16, 26, 50]]       Esquerdo: [[7, 14, 24], [23, 30, 40]]
#coloque o valor aqui do amarelo = Direito: [[31, 58, 8], [47, 74, 24]]       Esquerdo:  [[55, 79, 8], [71, 95, 24]]
#coloque o valor aqui do vermelho = Direito: [[37, 5, 5], [53, 21, 21]]      Esquerdo: [[62, 8, 5], [78, 24, 21]]
#coloque o valor aqui do preto = Direito: [[-2, 6, 3], [14, 22, 19]]      Esquerdo:  [[3, 7, 0], [19, 23, 16]]


#----------------------------------------------------------------------------------------------------------------------------------
#Teste para andar em cm

'''motor_left.run_angle(280, -360,  wait=False)
motor_right.run_angle(280, -360~,  wait=True)
print("Esquerdo", (motor_left.angle()))
print("Direito", (motor_right.angle()))
'''


#----------------------------------------------------------------------------------------------------------------------------------
#Teste dos lugares
#
school()
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
#
#close_claw(750)
#stop()
#69o,turn_right(90)
#turn_left(90)
#move_backward_cm(60)
#move_backward_cm(60)


'''while not saw_black():
  move_forward(500)

stop()'''

#----------------------------------------------------------------------------------------------------------------------------------


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



#------------------------------------------------------------------------------------------------------
#treinar kp e ki
"""i = 0
while i < 10 :
  #turn_left(90)
  turn_right(90)
  print("Virei")
  stop()
  wait(1000)
  i+=1"""
#turn_left(90)

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

