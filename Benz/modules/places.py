from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.hubs import EV3Brick
import time


from modules.motors import *
from modules.colors import *
from modules.detect import *
from modules.claw import *
from modules.varaiables import *

ev3 = EV3Brick()


count = 0 
count_turns_left = 0
count_turns_right = 0
passenger_size = 0 
total_of_passengers = 1
total_of_passengers_of_10cm = 1
total_of_passengers_of_15cm = 1
time_forward = 0


def recognize_first():
    print("oii")
    print(saw_red())
    while not saw_red() and not saw_blue():
        print("andando")
        move_forward(140)
        if(saw_black() or saw_yellow()):
           stop()
           move_backward_cm(3) #calcular
           turn_90_left()         

    stop()
   # check_point()
    if saw_red(): 
        turn_left(180)
        move_forward_cm(30)
        turn_90_left()
        while not saw_blue():
            move_foward(150)
            if(saw_black()):
                turn_180()
        stop()
    if(saw_blue()):
        #stop()
        reposition("Blue")
        move_backward_cm(7)
        turn_90_right()
        find_passenger()
    #colocar para ir para trás
    
    



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

#def enter():
    

def enter():
    entered = False
    while not entered:
        print(yellowRight()," ", yellowLeft())
        if(yellowRight() and yellowLeft()):
            move_forward_cm(10)
            return None
        elif yellowLeft() and blackRight():
            turn_right(89)
            move_forward_cm(2)
            turn_left(90) 
            #move_forward_cm(10)
        elif yellowRight() and blackLeft():
            turn_left(90)
            move_forward_cm(2)
            turn_right(90) 
        #else:
         #   stop()
          #  reposition("Black")        

            #move_forward_cm(10)

def find_passenger():
    print("procurando")
    final_tube()
    
    while not side_detection():
        move_forward(50)
    stop()   
    move_backward_cm(2)   
    turn_90_left()
    while not blueRight() and not blueLeft():
        move_forward(50) 
    stop()
    reposition("Blue")
    print("vou te pegar")
    close_claw(250)
    move_forward_cm(6)
    #verificar se tem algo na frente por preucação
    close_claw()
    move_backward_cm(9)
    check_point()
    #ver como vai ser tratado o return
    


def check_point():
    turn_90_left()
    while not saw_red():
        print("andando")
        move_forward(140)
    stop()
    reposition("Red")
    turn_180()
    tube = message()
    decision(tube)

def decision(tube):
    color = tube[0]
    size = tube[1]
    if size == "15":
        place = dic_15[color]
    else:
        place = dic_10[color]  
    if place == "ESCOLA":
        school()
        #get back from school depois      
#Funções referentes ao trajeto do robô

def school():
    move_forward_cm(30)
    turn_right(90)
    move_forward_cm(30)
    turn_90_right()
    while not saw_yellow():
        move_forward(50)
    stop()
    enter()


    open_claw(850) #fazer leave depois 

