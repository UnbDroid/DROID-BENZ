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
'''
turn_right(90)
wait(500)
turn_left(90)


motors.turn(90)
wait(500)
print(motor_left.angle())
print(motor_right.angle())

'''
#close_claw(800)
#leave_passenger()
#motor_left.run_angle(150, 247, then=Stop.HOLD, wait=False)
#motor_right.run_angle(150, -247, then=Stop.HOLD, wait=True)
#school()
#calibration_auto(sensor, array)

#open_claw(850)
# for i in range(100):
#   obstacle(False)
#   wait(1000)
  #obstacle()
  #wait(1000)
#recognize_first()
#open_claw(800)
#open_claw()
#school()
#while True:
 # calibration(sensor_color_right)
  #calibration(sensor_color_left)
  #wait(3000)
#calibration(sensor_color_right)
#reposition_two("Yellow", "Black")
#enter()
#open_claw()
#open_claw(200)
#turn_90_left() 
#check_point()
#turn_180()

#drugstore()
#while not saw_blue():
 # move_forward(160)
#stop()



#turn_left(360)
#turn_left(360)
#turn_left(360)
    
#open_claw(850)
#close_claw(250)
#move_forward_cm(6)
#verificar se tem algo na frente por preucação
#close_claw()
#move_backward_cm(9)
#check_point()
#move_backward_cm(5)
#close_claw(850)
#close_claw()

#Declaração de variáveis globais e objetos

#----------------------------------------------------------------------------------------------------------------------------------

#Programa principal (minúsuclo pq é o programa principal lmfao)

#school()
#
# 
#recognize_first()
#recognize_first()
# reposition("Blue")
#turn_90_left()
#command_stack()
#move_forward_cm(30)
#turn_left(90)
#move_forward_cm(30)
#turn_left(90)
#stack.reverse()

'''i = 0
while i < 10:
  motors.turn(360)
  wait(500)
  i+=1

'''
#while True:
 # print("diretinha", seeRight())
  #print("lula",  seeLeft())
  #time.sleep(1)
'''

tempo = StopWatch()
print(tempo.time())
print(tempo.reset())
time.sleep(2)
print(tempo.time())

'''

#recognize_first()
#museum2()
