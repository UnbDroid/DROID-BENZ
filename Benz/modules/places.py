from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait,
import time


from modules.motors import *
from modules.colors import *
from modules.detect import *
from modules.claw import *
from modules.varaiables import *



count = 0 
count_turns_left = 0
count_turns_right = 0
passenger_size = 0 
total_of_passengers = 1
total_of_passengers_of_10cm = 1
total_of_passengers_of_15cm = 1
time_forward = 0


def recognize_first():
    print("starting")
    #print(saw_red())
    while not saw_red() and not saw_blue():
        print("andando")
        move_forward(140)
        if(saw_black() or saw_yellow()):
           stop()
           reposition_wall()
           move_backward_cm(3) #calcular
           turn_left(90)  
           wait(500)       

    stop()
    if saw_red(): 
        #turn_left(180)
        move_forward_cm(30)
        turn_right(90)
        wait(500)
        while not saw_blue():
            move_forward(150)
            if(saw_black()):
                turn_left(180)
        stop()
    if(saw_blue()):
        stop()
        reposition("Blue")
        move_backward_cm(9)
        turn_right(90)
        find_passenger()
    recognize_first()
    
    #colocar para ir para trás
    

def final_tube():
    tempo = StopWatch()
    tempo.reset()
    while tempo.time() <= 3000:
        move_backward(80)  # implementar questão do tempo sem ver nada
        if side_detection():  # ainda sendo implementado
            print("oi")
            tempo.reset()
    stop()
    print("Ready to start taking passangers")

def recognize_first2():
    print("starting")
    # print(saw_red())
    while not saw_red() and not saw_blue():
        print("andando")
        move_forward(140)
        if (saw_black() or saw_yellow() or obstacle):
           stop()
           move_backward_cm(3)  # calcular
           turn_left(90)

    stop()
    if saw_red():
        # turn_left(180)
        move_forward_cm(30)
        turn_right(90)
        while not saw_blue():
            move_forward(150)
            if (saw_black()):
                turn_180()
        stop()
    if (saw_blue()):
        stop()
        reposition("Blue")
        move_backward_cm(7)
        turn_right(90)
        find_passenger()
    recognize_first()




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
    final_tube()
    while not side_detection():
        move_forward(50)
    stop()   
    move_backward_cm(1.8)   
    turn_left(90)
    stop()
    while not blueRight() and not blueLeft():
        move_forward(50) 
    stop()
    reposition("Blue")
    print("vou te pegar")
    close_claw(250)
    move_forward_cm(6)
    #verificar se tem algo na frente por preucação
    close_claw()
    move_backward_cm(6)
    stop()
    reposition("Blue")
    move_backward_cm(6)
    check_point()
    #ver como vai ser tratado o return
    


def check_point():
    turn_left(90)
    while not saw_red():
        print("andando")
        move_forward(120)
    stop()
    move_backward_cm(1)
    stop()
    reposition("Red")
    stop()
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
        print("Indo para a escola")
        school()
    elif place == "PREFEITURA":
        print("Indo para a prefeitura")
        city_hall()
    elif place == "BIBLIOTECA":
        print("Indo para a biblioteca")
        library()
    elif place == "FARMACIA":
        print("Indo para a farmácia")
        drugstore()
    elif place == "MUSEU":
        print("Indo para o museu")
        museum()
    elif place == "PARQUE":
        print("Indo para o parque")
        park()
    elif place == "PADARIA":
        print("Indo para a padaria")
        bakery()
        #get back from school depois      
#Funções referentes ao trajeto do robô

def school():
    command_stack()
    move_backward_cm(35)
    stack.append(["straight_cm", 35])
    
    #depois verificar tubo
    turn_left(90)
    stack.append(["turn_right", 90])
    move_forward_cm(32)
    stack.append(["back_cm", 30])
    turn_right(90)
    stack.append(["turn_leftt", 90])
    leave_passenger()
    stack.append(["back_cm", 15])
    stack.reverse()

def school2():
    move_backward_cm(35)
    if obstacle(False):
        move_backward_cm(60)
        turn_right(92)
        move_backward_cm(60)
        if obstacle(False):
            move_backward_cm(60)
            turn_left(92)
            move_forward_cm(60)
            turn_right(92)
            move_forward_cm(55)
            turn_left(92)
            move_forward_cm(35)
            turn_right(92)
            #leave_passenger()
        else:
            turn_left(92)
            move_forward_cm(90)
            turn_right(92)
           # leave_passenger()
    #depois verificar tubo
    else:
        turn_left(92)
        move_forward_cm(30)
        turn_right(92)
    leave_passenger()

def city_hall():
    command_stack()
    move_backward_cm(35)
    stack.append(["straight_cm", 35])
    #depois verificar tubo
    turn_left(92)
    stack.append(["turn_right", 90])
    move_forward_cm(30)
    stack.append(["back_cm", 15])
    turn_left(92)
    stack.append(["turn_right", 90])
    leave_passenger()
    stack.append(["back_cm", 15])
    stack.reverse()

def city_hall2(): #check
    move_backward_cm(35)
    if obstacle(False):
        move_backward_cm(60)
        turn_left(90)
        move_forward_cm(30)
        turn_right(90)
    #depois verificar tubo
    else:
        turn_left(92)
        move_forward_cm(30)
        turn_left(92)
    leave_passenger()

def library():
    move_backward_cm(95)#verificar se é isto mesmo que a distancia da biblioteca
    turn_left(90)
    move_forward_cm(30)
    turn_left(90)
    leave_passenger()

def museum():
    move_backward_cm(95)
    turn_left(90)
    move_forward_cm(95)
    turn_left(90)
    leave_passenger()

def museum2():
    move_backward_cm(32)
    if obstacle(False):
        move_backward_cm(60)
        turn_left(92) #mexer caso eleveja o primeiro obstaculo
        move_forward_cm(30)
        if obstacle(False):
            move_forward_cm(60)
            turn_left(90)
            move_forward_cm(35)
            turn_left(92)
            move_forward_cm(20)
            turn_right(90)
            if obstacle():
                turn_left(92)
                move_foward_cm(15)
                turn_right(92)
            else:
                move_foward_cm(30)
                turn_left(92)
    else:
        turn_left(96)
        move_forward_cm(120)
        turn_left(94)
        move_forward_cm(75)
        turn_left(94)
        move_forward_cm(25)
        turn_right(94)
        
    leave_passenger()


def drugstore():
    move_backward_cm(40)
    #depois verificar tubo
    turn_left(93)
    move_forward_cm(60)
    turn_left(93)
    move_forward_cm(25)
    turn_right(92)
    leave_passenger()


def drugstore2():
    move_backward_cm(40)
    # depois verificar tubo
    if obstacle(False):
        move_backward_cm(60)
        turn_right(90)
        move_backward_cm(45)
        if obstacle(False):
            move_backward_cm(55)
            turn_left(90)
            move_forward_cm(25)
            turn_right(90)
        else:
            turn_left(90)
            move_forward_cm(25)
            turn_left(90)
    else:
        turn_left(93)
        move_forward_cm(60)
        turn_left(93)
        if obstacle():
            turn_right(90)
            move_forward_cm(60)
            turn_left(90)
            move_forward_cm(25)
            turn_left(90)
        else:
            move_forward_cm(25)
            turn_right(92)
    leave_passenger()

def bakery():
    move_backward_cm(35)
    #depois verificar tubo
    turn_left(90)
    move_forward_cm(95)
    turn_right(90)
    leave_passenger()

def leave_passenger():
    while not saw_yellow() and not saw_black():
        move_forward(50)
    stop()
    reposition_wall()
    enter()
    open_claw(850) #fazer leave depois 

def enter():
    entered = False
    while not entered:
        print(yellowRight()," ", yellowLeft())
        if(yellowRight() and yellowLeft()):
            stop()
            reposition("Yellow")
            move_forward_cm(10)
            return None
        elif yellowLeft() and blackRight():
            stop()
            reposition_wall()
            move_backward_cm(3)
            turn_right(90)
            move_backward_cm(3)
            stop()
            turn_left(90) 
            stop()
            reposition_wall()
            move_backward_cm(2)
        elif yellowRight() and blackLeft():
            stop()
            reposition_wall()
            move_backward_cm(3)
            turn_left(90)
            move_backward_cm(3)
            stop()
            turn_right(90) 
            stop()
            reposition_wall()
            move_backward_cm(2)
        else:
            move_forward_cm(1)