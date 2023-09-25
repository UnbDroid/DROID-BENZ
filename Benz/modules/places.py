from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch
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




#1: 872 2: 874


def recognize_first():
    #trabalhar
    stop_motors()
    print("starting")
    while not saw_red() and not saw_blue():
        move_forward(380)
        if obstacle():
            path_obstacle()

        if (saw_black() or saw_yellow()):
            path_black_or_yellow()
    stop()

    if saw_red():
        path_red()

    if (saw_blue()):
        path_blue()

    print("Bora para o próximo")
    recognize_first()


def path_black_or_yellow():
    stop()
    reposition_wall()
    move_backward_cm(10)  # calcular
    turn_left(90)
    stop()
    move_forward_cm(30, False, "S")
    wait(500)
    turn_right(90)    

def path_obstacle():
    #código para verificar se viu um tubo ou não
    move_forward_cm(2)
    if(saw_blue()):
        path_blue()
    else:
        #testar
        move_backward_cm(15)
        turn_left(90)
        wait(500)

def path_blue():
    move_backward_cm(0.2)
    stop()
    reposition("Blue")
    stop()
    wait(500)
    move_backward_cm(0.75)
    stop_motors()
    turn_right(90)
    wait(500)
    find_passenger()

def path_red():
    wait(500)
    move_backward_cm(1.5)
    stop()
    reposition("Red")   
    stop()
    wait(500)
    move_backward_cm(30)
    turn_right(90)
    wait(500)
    while not saw_blue():
        move_forward(380)
        if obstacle():
            stop()
            stop_motors()
            move_backward_cm(2)
            stop_motors()
            turn_right()
        if blackRight() and blackLeft():
            print("ops")
            move_backward_cm(0.1)
            stop_motors()
            stop()
            reposition("Black")
            stop()
            move_backward_cm(3)
            turn_right(90)
            wait(500)
            turn_right(90)
            stop()
            wait(500)
    stop()

def forward_and_turn(cm, side, save = False):
    if side == 'L':
        move_forward_cm(cm)
        stop_motors()
        turn_left(90, save)
    elif side == 'R':
        move_forward_cm(cm)
        stop_motors()
        turn_right(90, save)
    wait(500)

def backward_and_turn(cm, side, save = False):
    if side == 'L':
        move_backward_cm(cm)
        turn_left(90, save)
    elif side == 'R':
        move_backward_cm(cm)
        turn_right(90, save)
    wait(500)


def final_tube():
    tempo = StopWatch()
    tempo.reset()
    while tempo.time() <= 3000:
        move_backward(-120)  # implementar questão do tempo sem ver nada
        if side_detection():  # ainda sendo implementado
            print("Voltando")
            tempo.reset()
    stop()
    print("Ready to start taking passangers")



def recognize():
    down = 0
    up = 0
    center = 0
    turn_90_right()
    move_forward(480)
    if(saw_black_left() and saw_black_right()):
        stop()
        down += 1
    elif (saw_yellow_left() and saw_yellow_right()):
        up += 1

    turn_180()
    move_forward(360*10)

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
    while not side_detection() and not saw_red():
        move_forward(280)
    stop()   
    if(saw_red()):
        reposition("Red")
        while not side_detection():
            move_backward(-100)
        stop()
    #move_backward_cm(0.1)   
    turn_left(90)
    stop()
    wait(500)
    while not blueRight() and not blueLeft():
        move_forward(180) 
    stop()
    reposition("Blue")
    print("vou te pegar")
 #   close_claw(250)
    move_forward_cm(4)
    #verificar se tem algo na frente por preucação
  #  close_claw()
    move_backward_cm(6)
    stop()
    reposition("Blue")
    move_backward_cm(6)
    check_point()
    #ver como vai ser tratado o return
    


def check_point():
    turn_left(90)
    #stop()
    wait(500)
    while not saw_red():
       # print("andando")
        move_forward(380)
    stop()
    move_backward_cm(1)
    stop()
    reposition("Red")
    stop()
    tube = message()
    print(tube)
    decision(tube)


def decision(tube):
    color = tube[0]
    size = tube[1]
    stack.reset()
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
#def path_ n                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

def school():
    move_backward_cm(30)
    wait(500)
    if obstacle("lado"):
        #caminho J-G-F
        print("Vish, acidente")
        backward_and_turn(62, 'L')
        move_forward_cm(62)
        turn_right(90, True) #ver isso

        if obstacle():
            #caminho J-E-B-D-F
            print("Vish, acidente")
            move_backward_cm(3)
            turn_left(90)
            forward_and_turn(65, 'R')
            move_forward_cm(60, True, 'F')
            turn_right(90, True)
            move_forward_cm(60, True, 'F')
            turn_left(90, True)
            move_forward_cm(25, True, "F")
        else:

            print("Sem obstáculo")
            move_forward_cm(91, True, 'F')

    else:
        #caminho I
        print("Sem obstáculo")
        turn_left(90)
        wait(500)
        move_forward_cm(26)
    wait(500)
    turn_right(90, True, 'R')
    stop_motors()
        
    leave_passenger()

def city_hall(): #check
    move_backward_cm(30)
    stop_motors()
    if obstacle("lado"):
        #caminho I
        print("Vish, acidente")
        backward_and_turn(60, 'L')
        move_forward_cm(30)
        turn_right(90, True, 'R')
    else:
        #caminho J
        move_backward_cm(3)
        turn_left(90)
        move_forward_cm(25)
        turn_left(90, True, 'L')
    leave_passenger()

def library():
    #caminho sem obstáculo
    backward_and_turn(65, 'R')
    while not saw_blue():
        move_forward(380)
    stop()
    reposition("Blue")
    move_backward_cm(3.5)
    stop()
    wait(500)
    turn_left(90)
    backward_and_turn(65, 'L')
    leave_passenger()
    turn_right(90)
    turn_right(90)

def museum():
    move_backward_cm(30)
    if obstacle("lado"):
        backward_and_turn(60, 'L')
        move_forward_cm(30)
        if obstacle("lado"):
            forward_and_turn(60, 'L')
            forward_and_turn(35, 'L')
            forward_and_turn(20, 'R')
            if obstacle():
                turn_left(90)
                forward_and_turn(15, 'R')
            else:
                forward_and_turn(30, 'L')
    else:
        turn_left(90)
        move_forward_cm(60)
        turn_left(90)
        wait(500)
        move_forward_cm(30)
        turn_left(90)
        get_break()
        move_backward_cm(10)
        turn_right(90, True, 'R')
        move_forward_cm(30)
        move_forward_cm(30, True, 'F' )
        turn_right(90, True, 'R')

    leave_passenger()
def get_break():
    while not saw_yellow() and not saw_black():
        move_forward(300)
    move_backward_cm(2)
    stop()
    reposition_wall()

def drugstore():
    move_backward_cm(30)
    # depois verificar tubo
    if obstacle("lado"):
        backward_and_turn(60, 'R')
        move_backward_cm(45)
        if obstacle("lado"):
            move_backward_cm(55, True, "F")
            turn_left(90, True)
            move_forward_cm(25, True)
            turn_right(90, True)
        else:
            turn_left(90, True)
            move_forward_cm(25, True)
            turn_left(90, True)
    else:
        turn_left(90)
        move_forward_cm(60)
        turn_left(90, True, "R")
        if obstacle():
            turn_right(90)
            move_forward_cm(60)
            turn_left(90)
            move_forward_cm(25)
            turn_left(90)
        else:
            move_forward_cm(35, True, "F")
            turn_right(90, True, "R")
    leave_passenger()

def bakery():
    move_backward_cm(30)
    #depois verificar tubo
    if obstacle("lado"): 
        #caminho J
        move_backward_cm(60)
        turn_left(90)
        move_backward_cm(60)
        if obstacle("lado"):
            #caminho E-B-A
            turn_left(90)
            turn_left(90)
            move_forward_cm(65)
            turn_right(90)
            move_forward_cm(90)
            turn_right(90)
        else:
            #caminho G-D
            turn_left(90)
            move_forward_cm(55) #G
            if obstacle("lado"):
                move_backward_cm(55)#G
                turn_left(90)
                move_forward_cm(65) #E
                turn_right(90)
                move_forward_cm(90) #B-A
                turn_right(90)
            else:
                turn_left(90)
                move_forward_cm(25) #D
                turn_right(90)
    else:
        #caminho I
        move_backward_cm(3)
        turn_left(90)
        move_forward_cm(60)
        wait(500)
        if obstacle():
            turn_left(90)
            wait(500)
            if obstacle():
                #caminho I-J-E-B-A
                turn_left(90)
                move_forward_cm(60) #I
                turn_right(90)
                move_forward_cm(60) #anda
                turn_right(90)
                move_forward_cm(60) #J
                #se calibrar
                move_forward_cm(60)#E
                turn_right(90)
                move_forward_cm(90) #B-A
                turn_right(90)

            else:
                #caminho G-E-B-A
                move_forward_cm(65)
                turn_right(90)
                move_forward_cm(65)
                turn_right(90)
                stop_motors()
                move_forward_cm(90)
                turn_right(90)
        else:
            #caminho D
            move_forward_cm(30)
            turn_right(90, True, 'R')
            stop_motors()
            wait(500)
    leave_passenger()



def park():
    move_backward_cm(45, True)
    if obstacle("lado"):
        move_backward_cm(55)
        turn_left(90)
        move_forward_cm(55)
        if obstacle():
            turn_left(90)
            move_forward_cm(35)
            turn_right(90)
            move_forward_cm(65)
        else:
            move_forward_cm(60)
            if obstacle("lado"):
                turn_right(90)
                
    else:
        turn_left(90,True)
        move_forward_cm(65, True)
        if obstacle():
            pass
        else:
            turn_right(90)
            move_forward_cm(45)
            turn_left(90)
    leave_passenger()

def leave_passenger():
    print("Deixando o passageiro")
    while not saw_yellow() and not saw_black():
        move_forward(180)
    stop()
    reposition_wall()
    enter()
    #open_claw()
    print("dando ré")
    move_backward_cm(10)
    stop()
    while not saw_yellow() and not saw_black():
        move_forward(180)
    stop()
    reposition_wall()
    move_backward_cm(5) #fazer leave depois
    stack.reverse() 

def enter():
    entered = False
    media_R_min = 17
    media_R_max = 27
    media_L_min = 25
    media_L_max = 35
    while not entered:
        calibration(sensor_color_left)
        calibration(sensor_color_right)
       # print(yellowRight()," ", yellowLeft())
        if ((yellowRight() and yellowLeft()) or (saw_yellow() and saw_yellow_black())):
            stop()
            reposition_wall()
            move_forward_cm(10)
            break
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
        elif sensor_color_left.rgb()[0] >= media_R_min and sensor_color_left.rgb()[0] <= media_R_max:
            print("Porcentagem 0,5% esquerda")
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

        elif sensor_color_right.rgb()[0]>= media_L_min and sensor_color_right.rgb()[0] <= media_L_max:
            print("Porcentagem 0,5% direita")
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
        else:
            move_forward_cm(1)
