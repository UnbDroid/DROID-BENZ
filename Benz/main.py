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
import time

#Declaração de variáveis globais e objetos

#----------------------------------------------------------------------------------------------------------------------------------

#Programa principal (minúsuclo pq é o programa principal lmfao)
#close_claw()
#motors.turn(180)
#print("rodei")
recognize_fisrt()
#move_forward_cm(30)
#i = 0
# while True:
#  #   calibrate()
#   #  i+=1
#    # calibration(sensor_color_left)
#     #calibration(sensor_color_right)
#    # teste_cor()
 #  print(saw_red())
    #time.sleep(1)