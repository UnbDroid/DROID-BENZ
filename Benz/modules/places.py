from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import StopWatch
from pybricks.hubs import EV3Brick

from modules.motors import *
from modules.colors import *
from modules.detect import *
from modules.claw import *

ev3 = EV3Brick()

count = 0 
count_turns_left = 0
count_turns_right = 0
passenger_size = 0 
total_of_passengers = 1
total_of_passengers_of_10cm = 1
total_of_passengers_of_15cm = 1
time_forward = 0

def follow_line() :
    global count_turns_left
    global count_turns_right
    move_forward(150)
    if (saw_black_left() and saw_black_right()) :
        pass
    elif saw_black_left() :
        turn_left(15)
        count_turns_left += 1
    elif saw_black_right() :
        turn_right(15)
        count_turns_right += 1

def recognize_fisrt():
    print("oii")
    print(saw_red())
    while not saw_red():
        print("andando")
        move_forward(150)
        if(saw_black() or saw_yellow()):
           stop()
           move_backward_cm(3) #calcular
           turn_90_left()
    stop() 
    turn_left(180)
    
    move_forward_cm(30)
    
   
    turn_90_left()
    while not saw_blue():
        move_foward(150)
        if(saw_black()):
            turn_180()
    stop()




def recognize():
    down = 0
    up = 0
    center = 0
    turn_90_right()
    move_forward(150)
    if(saw_black_left() and saw_black_right()):
        stop()
        down += 1
    elif (saw_yellow_left() and saw_yellow_right()):
        up += 1

    turn_180()
    move_forward(150)

    if(saw_yellow_left() and saw_yellow_right()):
        stop()
        down += 1
        up += 1

    turn_90_left()
    move_forward(150)

    if(saw_red_right() and saw_red_left()):
        stop()
        down += 1
        up += 1
    if(down == 3):
        move_forward_cm(15)
        turn_90_right()
    if(up == 3):
        move_forward_cm(15)
        turn_90_leftt()

    print("start")

#Funções referentes ao trajeto do robô


#def go_to_passengers() :
   

