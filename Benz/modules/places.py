from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import StopWatch
from pybricks.hubs import EV3Brick
import time


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
        move_backward_cm(5)
        turn_90_right()
        find_passenger()
    #colocar para ir para trás
    
    

def reposition(color):
    print("Entriu")
    if seeRight() != color and seeLeft() == color:
        print("Diferenciou")
        while seeRight() != color:
            circle_left()
        stop()
    elif seeRight() == color and seeLeft() != color:
        print("1")
        while seeLeft() != color:
            circle_right()
        stop()
    elif seeRight() == seeLeft():
        print("2")
        #pass
    elif seeRight() != color and seeLeft() != color:
        print("3")
        #pass
    print("rodou tuto")

def posicionate_in_blue():

    turn_90_left()
    while tempo <= 2:
        move_backward(80) #implementar questão do tempo sem ver nada
        if side_detection(): #ainda sendo implementado
            tempo = 2
    stop()
    print("Ready to start taking passangers")





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

def find_passenger():
    print("procurando")
    while not side_detection():
        move_backward(80)
    move_backward_cm(10)   
    turn_90_left()
    while not blueRight() and not blueLeft():
        move_forward(50) 
    reposition("Blue")
    print("vou te pegar")
    close_claw_s(200)
    move_forward_cm(6)
    #verificar se tem algo na frente por preucação
    close_claw()
    move_backward_cm(6)


def check_point():
    turn_90_left()
    while not saw_red():
        print("andando")
        move_forward(150)
    stop()
    turn_180()

#Funções referentes ao trajeto do robô


#def go_to_passengers() :
   

