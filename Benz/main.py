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

#turn_right(90)
#recognize_first2()
#move_forward(200)

#while True:
 # move_forward_pid(360*10)
#Abrir e fechar a garra
#find_passenger()
#close_claw(30)
#open_claw()
#final_tube()
#turn_right(90)
#recognize_first2()

# oi entrei
#oii
#vei, n sei o que ta acontecendo
#to testando, não está funcinando a hora da pilha
#vou testar aqui mais uma vez, vei simplesmente n funda
#ele printa mas na faz
# okok vou olhar a pilha okay/
#Declaração de variáveis globais e objetos

#----------------------------------------------------------------------------------------------------------------------------------

#Programa principal (minúsuclo pq é o programa principal lmfao)
# close_claw(760)
# school()
#
school()
time.sleep(5)
stack.reverse()
# 
# stack.backward_cm(12)
#turn_right(90)
#move_forward_cm(90)
#check_point()
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
#865
# motors.turn(330)
# while not blackRight() or not blackLeft():
#    motors.turn(1)
# motors.stop()
# print(motor_left.angle(), motor_right.angle())

#----------------------------------------------------------------------#

'''

motors.turn(90)

wait(500)
print(motor_left.angle())
print(motor_right.angle())
print("a")
turn_left(90)


'''
#turn_right_180(180)
'''
i = 0
while i < 2:
  turn_left(90)
#  motors.turn(360)
  print("Virei")
  stop()
  wait(1000)
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