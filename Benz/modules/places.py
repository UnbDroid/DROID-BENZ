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
def find_blue(walls_num):
    tempo = StopWatch()
    side_to_turn = ["Left", 1]

    if walls_num < 4:
        stop()

        print("starting")
        while not saw_blue() and not saw_black() and not saw_yellow() and not saw_red() and not obstacle():
            move_forward(380)
        time_forward = [motor_left.angle(), motor_right.angle()]
        stop()
        if saw_red():
            print("Parede vermelha 1")
            reposition()
        elif saw_black():
            reposition()
        elif saw_yellow():
            reposition()
        if not saw_blue() and not saw_red() and not saw_black() and not saw_yellow() and not obstacle():
            while not saw_blue() and not saw_black() and not saw_red() and not saw_yellow() and not obstacle():
                move_forward(380)

            stop()

        if saw_red():
            print("Parede vermelha 2")
            stop()
            move_backward_cm(40) #ver valor
            turn_left(90)
            stop()
            while not saw_blue():
                print("Entrei aqui")
                move_forward(380)
                if saw_black() or saw_yellow():
                    stop()
                    print("Parede preta")
                    
                    reposition() #reposicionar
                    move_backward_cm(15)
                    turn_left(90)
                    stop()
                    turn_left(90)
                elif obstacle():
                    stop()
                    path_obstacle()
                
                    if side_to_turn[0] == "Left":
                        turn_left(90)
                        if side_to_turn[1] == 2:
                            side_to_turn = ["Right", 1]
                        elif side_to_turn[1] == 1:
                            side_to_turn[1] += 1
                    else:
                        turn_right(90)
                        if side_to_turn[1] == 2:
                            side_to_turn = ["Left", 1]
                        elif side_to_turn[1] ==1:
                            side_to_turn[1] += 1
                    tempo.reset()
                    while not saw_red() and not obstacle() and not saw_blue()  and not saw_yellow():
                        move_forward(380)
                    stop()
                    if tempo.time() < 3000 or obstacle():
                        if not obstacle():
                            reposition() #verificar
                        while not saw_red() and not saw_black() and not saw_yellow() and not saw_blue():
                            move_forward(390)
                        stop()
                        if saw_red():
                            print("Parede vermelha")
                            reposition()
                            stop()
                            move_backward_cm(38)
                            if side_to_turn[0] == "Left":
                                turn_left(90)
                                if side_to_turn[1] == 2:
                                    side_to_turn = ["Right", 1]
                                elif side_to_turn[1] == 1:
                                    side_to_turn[1] += 1
                            else:
                                turn_right(90)
                                if side_to_turn[1] == 2:
                                    side_to_turn = ["Left", 1]
                                elif side_to_turn[1] == 1:
                                    side_to_turn += 1
                    elif saw_black():
                        print("Parede preta")
                        reposition()
                        move_backward_cm(8)
                        if side_to_turn[0] == "Left":
                            turn_left(90)
                            if side_to_turn[1] == 2:
                                side_to_turn = ["Left", 1]
                            elif side_to_turn[1] == 1:
                                side_to_turn[1] += 1
                        else:
                            turn_right(90)
                            stop()
                            if side_to_turn[1] == 2:
                                side_to_turn = ["Left", 1]
                            elif side_to_turn[1] == 1:
                                side_to_turn[1] += 1
                        find_blue(0)
                    elif obstacle():
                        stop()
                        path_obstacle()
                        if side_to_turn[0] == "Left":
                            turn_left(90)
                            if side_to_turn[1] == 2:
                                side_to_turn = ["Right", 1]
                            elif side_to_turn[1] == 1:
                                side_to_turn[1] += 1
                        else:
                            turn_right(90)
                            stop()
                            if side_to_turn[1] == 2:
                                side_to_turn = ["Left", 1]
                            elif side_to_turn[1] == 1:
                                side_to_turn[1] += 1
                        while not saw_blue():
                            move_forward(380)
                            if saw_black() or saw_yellow():
                                stop()
                                reposition() #se arrumar
                                move_backward_cm(7)
                                if side_to_turn[0] == "Left":
                                    turn_left(90)
                                    if side_to_turn[1] == 2:
                                        side_to_turn = ["Right", 1]
                                    elif side_to_turn[1] == 1:
                                        side_to_turn[1] += 1
                                else:
                                    turn_right(90)
                                    stop()
                                    if side_to_turn[1] == 2:
                                        side_to_turn = ["Left", 1]
                                    elif side_to_turn[1] == 1:
                                        side_to_turn[1] += 1
                            elif obstacle():
                                stop()
                                path_obstacle()
                                if side_to_turn[0] == "Left":
                                    turn_left(90)
                                    if side_to_turn[1] == 2:
                                        side_to_turn = ["Right", 1]
                                    elif side_to_turn[1] == 1:
                                        side_to_turn[1] += 1
                                else:
                                    turn_right(90)
                                    stop()
                                    if side_to_turn[1] == 2:
                                        side_to_turn = ["Left", 1]
                                    elif side_to_turn[1] == 1:
                                        side_to_turn[1] += 1
                                
                            elif saw_red():
                                stop()
                                reposition()
                                stop()
                                move_backward_cm(38)
                                if side_to_turn[0] == "Left":
                                    turn_left(90)
                                    if side_to_turn[1] == 2:
                                        side_to_turn = ["Right", 1]
                                    elif side_to_turn[1] == 1:
                                        side_to_turn[1] += 1
                                else:
                                    turn_right(90)
                                    if side_to_turn[1] == 2:
                                        side_to_turn = ["Left", 1]
                                    elif side_to_turn[1] == 1:
                                        side_to_turn += 1
            else:
                print("Cheguei aqui")
                if saw_blue():
                    stop()
                    reposition()
                    return 0
                stop()
                reposition()
                move_backward_cm(38)
                if (side_to_turn[0] == "Left" and side_to_turn[1] == 1) or (side_to_turn[0] == "Right" and side_to_turn[1] == 2):
                    turn_left(90)
                else:
                    turn_right(90)

                while not saw_blue() or not saw_red() or not obstacle() or not saw_black() or not saw_yellow():
                        print("oi friends")
                        move_forward(360)
                        stop()
                        if saw_red():
                            reposition()
                            move_backward_cm(38)
                            if side_to_turn[0] == "ESQUERDA":
                                stop()
                                turn_left(90)
                                if side_to_turn[1] == 2:
                                    side_to_turn = ["DIREITA", 1]
                                elif side_to_turn[1] == 1:
                                    side_to_turn[1] += 1
                            else:
                                turn_right(90)
                                if side_to_turn[1] == 2:
                                    side_to_turn = ["ESQUERDA", 1]
                                elif side_to_turn[1] == 1:
                                    side_to_turn[1] += 1
                        elif saw_black():
                            stop()
                            reposition()
                            move_backward_cm(8)
                            if side_to_turn[0] == "ESQUERDA":
                                turn_left(90)
                                if side_to_turn[1] == 2:
                                    side_to_turn = ["DIREITA", 1]
                                elif side_to_turn[1] == 1:
                                    side_to_turn[1] += 1
                            else:
                                turn_right(90)
                                if side_to_turn[1] == 2:
                                    side_to_turn = ["ESQUERDA", 1]
                                elif side_to_turn[1] == 1:
                                    side_to_turn[1] += 1
                            find_blue(0)
                        elif obstacle():
                            stop()
                            if side_to_turn[0] == "ESQUERDA":
                                turn_left(90)
                                if side_to_turn[1] == 2:
                                    side_to_turn = ["DIREITA", 1]
                                elif side_to_turn[1] == 1:
                                    side_to_turn[1] += 1
                            else:
                                turn_right(90)
                                if side_to_turn[1] == 2:
                                    side_to_turn = ["ESQUERDA", 1]
                                elif side_to_turn[1] == 1:
                                    side_to_turn[1] += 1
                            while not saw_blue():
                                move_forward_cm(500)
                                if saw_black() or saw_yellow():
                                    stop()
                                    reposition()
                                    move_backward_cm(8)
                                    if side_to_turn[0] == "ESQUERDA":
                                        turn_left(90)
                                        if side_to_turn[1] == 2:
                                            side_to_turn = ["DIREITA", 1]
                                        elif side_to_turn[1] == 1:
                                            side_to_turn[1] += 1
                                    else:
                                        turn_right(90)
                                        if side_to_turn[1] == 2:
                                            side_to_turn = ["ESQUERDA", 1]
                                        elif side_to_turn[1] == 1:
                                            side_to_turn[1] += 1
                                elif obstacle():
                                    stop()
                                    if side_to_turn[0] == "ESQUERDA":
                                        turn_left(90)
                                        if side_to_turn[1] == 2:
                                            side_to_turn = ["DIREITA", 1]
                                        elif side_to_turn[1] == 1:
                                            side_to_turn[1] += 1
                                    else:
                                        turn_right(90)
                                        if side_to_turn[1] == 2:
                                            side_to_turn = ["ESQUERDA", 1]
                                        elif side_to_turn[1] == 1:
                                            side_to_turn[1] += 1
                                elif saw_red():
                                    stop()
                                    reposition()
                                    move_backward_cm(38)
                                    if side_to_turn[0] == "ESQUERDA":
                                        turn_left(90)
                                        if side_to_turn[1] == 2:
                                            side_to_turn = ["DIREITA", 1]
                                        elif side_to_turn[1] == 1:
                                            side_to_turn[1] += 1
                                    else:
                                        turn_right(90)
                                        if side_to_turn[1] == 2:
                                            side_to_turn = ["ESQUERDA", 1]
                                        elif side_to_turn[1] == 1:
                                            side_to_turn[1] += 1







       
        elif saw_black() or saw_yellow() or obstacle():
            print("Tentando me achar")
            if saw_black() or saw_yellow():
                stop()
                move_backward_cm(15)
                stop()
            elif obstacle():
                path_obstacle()
                stop()
            turn_right(90)
            print("Vai somar mais um no numero_de_paredes")
            print(walls_num)
            find_blue(walls_num + 1)
    else:
        reposition()
        turn_right(90)
        while ultra_sensor.distance() > 145 and not saw_black() and not saw_yelllow():
            move_forward(350)
        stop()
        if saw_black() or saw_yellow():
            reposition()
            move_backward_cm(8)
        find_blue(0)


def swap_and_add():
    if side_to_turn[0] == "Left":
        turn_left(90)
        if side_to_turn[1] == 2:
            side_to_turn = ["Right", 1]
        elif side_to_turn[1] == 1:
            side_to_turn[1] += 1
    else:
        turn_right(90)
        if side_to_turn[1] == 2:
            side_to_turn = ["Left", 1]
        elif side_to_turn[1] == 1:
            side_to_turn += 1

def recognize_first():
    #trabalhar
    wall_red = 0
    obstacle_count = 0
    wall_black_or_yellow = 0

    stop()
    print("starting")
    while not saw_blue():
        move_forward(330)
        if obstacle():
           # if(obstacle_count == 2):
                #ish
            obstacle_count += 1
            path_obstacle()

        if (saw_black() or saw_yellow()):
            if wall_red == 2:
                wall_red = 0
                stop()
                reposition()
                move_backward_cm(15)
                turn_right(90)
                wait(500)
                turn_right(90)
                wait(500)
            elif wall_red == 1:
                break 
            else:
                path_black_or_yellow()

        if saw_red():
            wall_red += 1
            path_red()
    stop()

    if (saw_blue()):
        path_blue()

    print("Bora para o próximo")
    recognize_first()

def recognize():
    obstacle_count = 0
    red_wall = 0
    yellow_wall = 0
    black_wall = 0
    maybe_red = 0
    wall_first = 0
    
    while not saw_blue():
        if saw_blue():
            stop()
            reposition()
            return False
            
        if saw_red():
            stop()
            reposition()
            if wall_first == 0:
                case = scanner_initial("Red")
                wall_first += 1              
            elif red_wall == 2:
                #algo
                red_wall = 0
            red_wall +=1
            
        if saw_black():
            stop()
            reposition()
            if wall_first == 0:
                case = scanner_initial("Black")
                wall_first += 1   
            elif black_wall == 1 and obstacle_count == 0:
                stop()
                turn_left(90)
                stop()
                turn_left(90)
            black_wall += 1
            

        if saw_yellow():
            stop()
            reposition()
            if wall_first == 0:
                case = scanner_initial("Yellow")
                wall_first += 1  
            yellow_wall += 1 
            
        if obstacle():
            path_obstacle()

        if wall_first == 1:
            if case == 1: #[Black, Vermelho, Yellow]
                move_backward_cm(38) #verificar
                maybe_red += 1
                stop()
                turn_left(90)
            elif case == 2: #[Yellow, Vermelho, Yellow]
                move_backward_cm(38)
                stop()
                turn_right(90)
                
            elif case == 3: #[Yellow, White, Yellow]
                pass
            elif case == 4: #[Black, White, Yellow]
                pass
            
            elif case == 5: #[Yellow, Red, Yellow]
                move_backward_cm(38)
                stop()
                turn_right(90)
            elif case == 6: #[White, Black, White]
                pass

                

def forward_while_white(distance = 10):
    while distance != 0 and saw_white():
        move_forward_cm(1)
        distance -= 1
    stop()
    reposition()
    return 10 - distance

    

def scanner_initial(first):
    paredes = []
    paredes.append(first)
    distance = 10
    move_backward_cm(distance)
    if first != "Red":
        for i in range(3):
            stop()
            turn_right(90)
            distance = forward_while_white()
            left = seeLeft()
            right = seeRight()
            if (left == "Black" and right == "Yellow") or (left == "Yellow" and right == "Black") or (left == "Yellow" and right == "Yellow"):
                paredes.append("Yellow")
            elif right == "Red" or left == "Red":
                paredes = ["Red"]
                break
            elif left == "Black" or right == "Black":
                paredes.append("Black")
            else:
                paredes.append("White")
            move_backward_cm(distance)
        turn_right(90)
    else:
        paredes = ["Red"]
    if "Red" in  paredes or first == "Red":
        turn_left(90)
        distance = forward_while_white()
        left = seeLeft()
        right = seeRight()
        if (left == "Black" and right == "Yellow") or (left == "Yellow" and right == "Black") or (left == "Yellow" and right == "Yellow"):
            paredes.insert(0, "Yellow")
        elif left == "Black" or right == "Black":
            paredes.insert(0, "Black")
        move_backward_cm(15)
        turn_left(90)
        turn_left(90)
        distance = forward_while_white()
        left = seeLeft()
        right = seeRight()
        if (left == "Black" and right == "Yellow") or (left == "Yellow" and right == "Black") or (left == "Yellow" and right == "Yellow"):
            paredes.append("Yellow")
        elif left == "Black" or right == "Black":
            paredes.append("Black")
        move_backward_cm(15)
        turn_left(90)
        print(paredes)
    return cases(paredes)
        
    
def cases(lista):
    if lista[1] == "Red":
        if lista[0] == "Black" and lista[2] == "Yellow":
            return 1
        elif lista.count("Yellow") == 2:
            return 5
        else:
            return 2
    else:
        if lista.count("Yellow") == 2:
            return 3
        elif lista.count("White") == 3:
            return 6
        else:
            return 4

def path_black_or_yellow():
    stop()
    reposition_wall()
    stop()
    move_backward_cm(15) 
    stop() # calcular
    turn_left(90)
   

def path_obstacle():
    stop()
    #código para verificar se viu um tubo ou não
    move_forward_cm(1.5)
    if(saw_blue()):
        path_blue()
    else:
        move_backward_cm(10) #ver o tam
        stop()
        turn_right(90)
        stop()
        turn_right(90)
        stop()

def path_blue():
    #move_backward_cm(0.2)
    stop()
    reposition()
    stop()
    wait(500)
    move_backward_cm(3)
    stop()
    turn_right(90)
    wait(500)
    find_passenger()

def path_red():
   # move_backward_cm(1.5)
    stop()
    reposition()   
    stop()
    move_backward_cm(43)
    stop()
    turn_right(90)
    stop()
    '''while not saw_blue():
        move_forward(380)
        if obstacle():
            stop()
            stop()
            move_backward_cm(2)
            stop()
            turn_right()
        if blackRight() and blackLeft():
            print("ops")
            move_backward_cm(0.1)
            stop()
            stop()
            reposition()
            stop()
            move_backward_cm(3)
            turn_right(90)
            wait(500)
            turn_right(90)
            stop()
            wait(500)'''
    stop()

def forward_and_turn(cm, side, save = False):
    if side == 'L':
        move_forward_cm(cm)
        stop()
        turn_left(90, save)
    elif side == 'R':
        move_forward_cm(cm)
        stop()
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
        move_backward_cm(-120)  # implementar questão do tempo sem ver nada
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


def find_passenger(final = True):
    print("procurando")
    if final:
        final_tube()
    else:
        turn_right(90)
        stop()
        turn_right(90)

    while not side_detection() and not saw_red():
        move_forward(280)
    stop()   
    if(saw_red()):
        reposition()
        while not side_detection():
            move_backward_cm(-100)
        stop()
    move_backward_cm(3)   
    turn_left(90)
    stop()
    wait(500)
    while not blueRight() and not blueLeft():
        move_forward(180) 
    stop()
    reposition()
    print("vou te pegar")
   # close_claw(250)
    move_forward_cm(4)
    #verificar se tem algo na frente por preucação
    #close_claw()
    move_backward_cm(6)
    stop()
    reposition()
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
    reposition()
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
    else:
        open_claw()
        find_passenger(False)
        #get back from school depois      
#Funções referentes ao trajeto do robô
#def path_ n                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

def school():
    move_backward_cm(40)
    wait(500)
    if obstacle("lado"):
        #caminho J-G-F
        print("Vish, acidente")
        backward_and_turn(65, 'L')
        move_forward_cm(72)
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
            move_forward_cm(93, True, 'F')

    else:
        #caminho I
        print("Sem obstáculo")
        turn_left(90)
        wait(500)
        move_forward_cm(37)
    wait(500)
    turn_right(90, True, 'R')
    stop()
        
    leave_passenger()

def city_hall(): #check
    move_backward_cm(40)
    stop()
    if obstacle("lado"):
        #caminho I
        print("Vish, acidente")
        backward_and_turn(65, 'L')
        move_forward_cm(35)
        turn_right(90, True, 'R')
    else:
        #caminho J
        move_backward_cm(3)
        turn_left(90)
        move_forward_cm(39)
        turn_left(90, True, 'L')
    leave_passenger()

def library():
    #caminho sem obstáculo
    backward_and_turn(65, 'R')
    while not saw_blue():
        move_forward(380)
    stop()
    reposition()
    move_backward_cm(10)
    stop()
    wait(500)
    turn_right(90)
    while not saw_red():
        move_forward(400)
    move_backward_cm(10)
    turn_right(90)
    leave_passenger()
    # turn_left(90)
    # backward_and_turn(65, 'L')
    # leave_passenger()
    # turn_right(90)
    # turn_right(90)

def museum():
    move_backward_cm(43)
    if obstacle("lado"):
        backward_and_turn(70, 'L')
        move_forward_cm(80)
        if obstacle():
            move_backward_cm(10)
            turn_left(90)
            while not saw_red():
                move_forward(350)
            reposition()
            move_backward_cm(10)
            turn_right(90)
        else:
            move_forward_cm(25)
            turn_left(90)
    else:
        turn_left(90)
        move_forward_cm(75)
        if obstacle("lado"):
            move_backward_cm(75)
            turn_left(90)
            move_forward_cm(75)
            turn_right(90)
            if obstacle():
                turn_right(90)
                move_forward_cm(75)
                turn_left(90)
                while not saw_black():
                    move_forward(300)
                move_backward_cm(15)
                turn_left(90)
                move_forward_cm(75)
                turn_left(90)
                move_forward_cm(35)
                turn_right(90)
            else:
                turn_left(90)
                move_forward_cm(70)
                turn_right(90)
                move_forward_cm(80)
                if obstacle():
                    move_backward_cm(10)
                    turn_left(90)
                    while not saw_red():
                        move_forward(350)
                    reposition()
                    move_backward_cm(10)
                    turn_right(90)
                else:
                    move_forward_cm(25)
                    turn_left(90)
            
        
        else:
            turn_left(90)
            move_forward_cm(75)
            if obstacle():
                turn_right(90)
                move_forward_cm(35)
                turn_left(90)
            else:
                while not saw_red():
                    move_forward(350)
                reposition()
                move_backward_cm(10)
                turn_right(90)
            
            
        # move_forward_cm(30)
        # turn_left(90)
        # #get_break()
        # move_backward_cm(10)
        # turn_right(90, True, 'R')
        # move_forward_cm(30)
        # move_forward_cm(30, True, 'F' )
        # turn_right(90, True, 'R')

    leave_passenger()
def get_break():
    while not saw_yellow() and not saw_black():
        move_forward(300)
    move_backward_cm(2)
    stop()
    reposition_wall()

def drugstore():
    move_backward_cm(43)
    # depois verificar tubo
    if obstacle("lado"):
        backward_and_turn(70, 'R')
        move_backward_cm(70)
        if obstacle("lado"):
            move_backward_cm(70, True, "F")
            turn_left(90, True)
            move_forward_cm(40, True)
            turn_right(90, True)
        else:
            turn_left(90, True)
            move_forward_cm(35, True)
            turn_left(90, True)
    else:
        turn_left(90)
        move_forward_cm(75)
        if obstacle("lado"):
            move_forward_cm(65)
            turn_left(90)
            move_forward_cm(35)
            turn_left(90)
        else:
            turn_left(90)
            move_forward_cm(40, True, "F")
            turn_right(90, True, "R")
    leave_passenger()

def bakery():
    move_backward_cm(43)
    #depois verificar tubo
    if obstacle("lado"): 
        #caminho J
        move_backward_cm(65)
        turn_right(90)
        move_backward_cm(70)
        if obstacle("lado"):
            #caminho E-B-A
            turn_left(90)
            turn_left(90)
            while not saw_black():
                move_forward(400)
            reposition()
            move_backward_cm(15)
            turn_right(90)
            while not saw_red():
                move_forward(400)
            move_backward_cm(10)
            turn_right(90)
        else:
            #caminho G-D
            turn_left(90)
            move_forward_cm(70) #G
            if obstacle("lado"):
                move_backward_cm(70)#G
                turn_left(90)
                while not saw_black():
                    move_forward(400)
                reposition()
                move_backward_cm(15)
                turn_right(90)
                while not saw_red():
                    move_forward(400) #B-A
                move_backward_cm(10)
                turn_right(90)
            else:
                turn_left(90)
                move_forward_cm(35) #D
                turn_right(90)
    else:
        #caminho I
        move_backward_cm(3)
        turn_left(90)
        move_forward_cm(85)
        wait(500)
        if obstacle():
            move_backward_cm(10)
            turn_left(90)
            move_forward_cm(5)
            wait(500)
            if obstacle():
                #caminho I-J-E-B-A
                move_backward_cm(5)
                turn_left(90)
                move_forward_cm(70) #I
                turn_right(90)
                move_forward_cm(65) #anda
                turn_right(90)
                while not saw_black():
                    move_forward(360)
                #move_forward_cm(70) #J
                #se calibrar
                #move_forward_cm(65)#E
                reposition()
                move_backward_cm(15)
                turn_right(90)
                while not saw_red():
                    move_forward(360)
                #move_forward_cm(105) #B-A
                reposition()
                move_backward_cm(10)
                turn_right(90)

            else:
                #caminho G-E-B-A
                move_forward_cm(65)
                turn_right(90)
                while not saw_black():
                    move_forward(450)
                move_backward_cm(15)
                turn_right(90)
                stop()
                while not saw_red():
                    move_forward(400)
                move_backward_cm(10)
                turn_right(90)
        else:
            #caminho D
            move_forward_cm(22)
            turn_right(90, True, 'R')
            stop()
            wait(500)
    leave_passenger()



def park():
    move_backward_cm(43, True)
    if obstacle("lado"):
        move_backward_cm(70)
        turn_left(90)
        move_forward_cm(80)
        if obstacle():
            turn_right(90)
            move_forward_cm(70)
            turn_left(90)
            while not saw_black():
                move_forward(400)
            reposition()
            move_backward_cm(15)
            turn_right(90)
            move_forward_cm(15)
            if obstacle():
                move_backward_cm(50)
                turn_left(90)
            else:
                while not saw_red():
                    move_forward(250)
                move_backward_cm(15)
                turn_left(90)
            
        else:
            while not saw_black():
                move_forward(400)
            reposition()
            move_backward_cm(10)
            if obstacle("lado"):
                turn_right(90)
                move_forward_cm(40)
                turn_left(90)
            else:
                turn_left(90)
                while not saw_red():
                    move_forward(250)
                reposition()
                move_backward_cm(10)
                turn_right(90)
                
    else:
        turn_left(90,True)
        move_forward_cm(80, True)
        if obstacle():
            move_backward_cm(10)
            turn_left(90)
            move_forward_cm(70)
            turn_right(90)
            while not saw_black():
                move_forward(400)
            reposition()
            move_backward_cm(10)
            if obstacle("lado"):
                turn_right(90)
                move_forward_cm(40)
                turn_left(90)
            else:
                turn_left(90)
                while not saw_red():
                    move_forward(250)
                reposition()
                move_backward_cm(10)
                turn_right(90)
        else:
            while not saw_black():
                move_forward(400)
            reposition()
            move_backward_cm(15)
            turn_right(90)
            move_forward_cm(15)
            if obstacle():
                move_backward_cm(50)
                turn_left(90)
            else:
                while not saw_red():
                    move_forward(250)
                move_backward_cm(15)
                turn_left(90)
                
                    
            
    leave_passenger()

def leave_passenger():
    print("Deixando o passageiro")
    while not saw_yellow() and not saw_black():
        move_forward(240) #180 velocidade original
    stop()
    reposition_wall()
    enter()
  #  open_claw()
    print("dando ré")
    move_backward_cm(10)
    stop()
    while not saw_yellow() and not saw_black():
        move_forward(180)
    stop()
    reposition_wall()
    move_backward_cm(15) #fazer leave depois
    stack.reverse() 

def enter():
    entered = False
    media_R_min = 17
    media_R_max = 27
    media_L_min = 25
    media_L_max = 35
    count = 0
    while not entered:
        calibration(sensor_color_left)
        calibration(sensor_color_right)
       # print(yellowRight()," ", yellowLeft())
        if ((yellowRight() and yellowLeft()) or (yellow_i_black_left() and yellowRight())or (yellow_i_black_right() and yellowLeft())):
            stop()
            reposition_wall()
            reposition()
            move_forward_cm(10)
            break
        elif count < 2 and yellowLeft() and blackRight():
            stop()
            reposition()
            reposition_wall()
            move_backward_cm(5)
            turn_right(90)
            move_backward_cm(3)
            stop()
            turn_left(90)
            stop()
            reposition_wall()
            move_backward_cm(2)
            count += 1
        elif count < 2 and yellowRight() and blackLeft():
            stop()
            reposition_wall()
            reposition()
            move_backward_cm(5)
            turn_left(90)
            move_backward_cm(3)
            stop()
            turn_right(90)
            stop()
            reposition_wall()
            move_backward_cm(2)
            count += 1
        elif count < 2 and sensor_color_left.rgb()[0] >= media_R_min and sensor_color_left.rgb()[0] <= media_R_max:
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
            count += 1

        elif count < 2 and sensor_color_right.rgb()[0]>= media_L_min and sensor_color_right.rgb()[0] <= media_L_max:
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
            count += 1
        else:
            move_forward_cm(1)

