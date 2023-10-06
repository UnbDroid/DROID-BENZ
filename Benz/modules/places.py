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

def path_black_or_yellow():
    stop()
    reposition()
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
    # stop()
    # reposition()
    # stop()
    # move_backward_cm(5)
    # stop()
    # turn_right(90)
    find_passenger()

def path_red():
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

def recognize():
    stop()
    print("starting")
    obstacle_count = 0

    maybe_red = 0
    wall_first = 0
    case_1 = 0
    case_2 = 0
    case_3 = 0
    case_4 = 0
    
    while not saw_blue():
        move_forward(400)
            
        if saw_red():
            stop()
            reposition()
            if wall_first == 0:
                case = scanner_initial("Red")
                wall_first += 1              


            elif case_1 == 2 or case_4 == 2:
                move_backward_cm(35)
                turn_right(90)
                stop()
                case_1 = 4
            
        if saw_black():
            stop()
            reposition()
            if wall_first == 0:
                case = scanner_initial("Black")
                wall_first += 1   
            
            elif case_1 == 3 or case_2 == 3:
                #E bateu na parede preta
                stop()
                reposition()
                move_backward_cm(9)
                turn_right(90)
                move_forward_cm(35) #B
                turn_right(90)
            else:
                move_backward_cm(10)
                stop()
                turn_left(90)
                stop()
                turn_left(90)
            

        if saw_yellow():
            stop()
            reposition()
            if wall_first == 0:
                case = scanner_initial("Yellow")
                wall_first += 1  
            yellow_wall += 1 
            
        if obstacle():            
            #vai virando aos poucos 
            if case_1 == 1 or case_2 == 2:
                #Vê obstáculo no J 
                stop()
                move_backward_cm(5)
                stop()
                print("Vi e irei virar")
                if obstacle("lado"):
                    turn_left(90)
                    stop()
                    case_1 += 1
                turn_left(90)
                case_1 += 1
                case_2 += 1

            elif case_1 == 2 or case_4 == 1:
                #G
                stop()
                move_backward_cm(5)
                stop()
                turn_left(90)
                case_1 += 1
                case_4 += 1
            elif case_1 == 4 or case_2 == 1 :
                #vira para direita e vira na outra rua
                turn_right(90)
                stop()
                move_forward_cm(35)
                stop()
                turn_left(90)
                stop()
                case_2 += 1 
            else:
                path_obstacle()

        if wall_first == 1:
            wall_first = 2
            print(wall_first)
            if case == 1: #[Black, Vermelho, Yellow]
                print("Entrei aqui")
                move_backward_cm(38) #verificar
                maybe_red += 1
                stop()
                turn_left(90)
                case_1 += 1
            elif case == 2: #[Yellow, Vermelho, Yellow]
                move_backward_cm(38)
                stop()
                turn_right(90)
                case_2 += 1
                
            elif case == 3: #[Yellow, White, Yellow]
                turn_left(90)
                case_3 += 1
                
            elif case == 4: #[Black, White, Yellow]
                turn_right(90)
                stop()
                case_4 += 1
            
         #   elif case == 5: #[Yellow, Red, Yellow]
          #      move_backward_cm(38)
           #     stop()
            #    turn_right(90)
            elif case == 6: #[White, Black, White]
                pass

    if saw_blue():
        stop()
        reposition()
        return False
        

def forward_while_white(distance = 10):
    print(distance != 0 and saw_white())
    print(distance,"  ", saw_white())
    while distance != 0 and saw_white():
        print(distance)
        move_forward_cm(1)
        distance -= 1
    stop()
    print(whiteRight(),"   ", whiteLeft())
    if not saw_white():
        print("ue")
        #reposition()
    return 5 - distance

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
            #Preto, vermelho, amarelo
        elif lista.count("Yellow") == 2:
            return 5
            #Amarelo, vermelho, amarelo
        else:
            return 2
            #Acho que n precisa
    else:
        if lista.count("Yellow") == 2:
            return 3
            #Amarelo, Branco e Amarelo
        elif lista.count("White") == 3:
            return 6
            #rapaz, to sem zap
        else:
            #Preto, Branco e Amarelo
            return 4


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
        move_backward(-250) # implementar questão do tempo sem ver nada
        if side_detection():  # ainda sendo implementado
            print("Voltando")
            tempo.reset()
    stop()
    print("Ready to start taking passangers")



def find_passenger_2(final = True):
    print("procurando")
    if final:
        final_tube()
    else: #chegou no check-point e não identifico o tubo
        turn_right(90)
        stop()
        turn_right(90)

    while not side_detection() and not saw_red():
        move_forward(280)
    stop()   
    if(saw_red()):
        reposition()
        while not side_detection():
            move_backward(-250)
        stop()
    move_backward_cm(3)   
    turn_left(90)
    stop()
    wait(500)
    while not blueRight() and not blueLeft():
        move_forward(180) 
    stop()
    #reposition()
    print("vou te pegar")
    close_claw(250)
    move_forward_cm(4)
    #verificar se tem algo na frente por preucação
    close_claw()
    move_backward_cm(6)
    stop()
    reposition()
    stop()
    move_backward_cm(10)
    check_point()
    #ver como vai ser tratado o return
    
def find_passenger(final_tube = True): #Função feita pelo Josh e Felipe e Luiz
    
    #Já começa alinhado no azul
    stop()
    reposition()
    stop()
    move_backward_cm(5)
    stop()
    turn_left(90)
    
    threshold = ((25 + 85)/2)+15

    while not saw_red():
        valor = sensor_color_right.rgb()[1]
        angulo = valor - threshold
        k = 0.8
        motors.drive(120, k*angulo)
    motors.stop()
    
    
    turn_left(90)
    stop()
    move_forward_cm(6)
    stop()
    turn_left(90)
    
    while not side_detection() and not saw_red():
        move_forward(280)
    
    stop()
    
    if(saw_red()):
        reposition()
        while not side_detection():
            move_backward(-250)
        stop()
    move_backward_cm(3)   
    turn_left(90)
    stop()
    wait(500)
    while not blueRight() and not blueLeft():
        move_forward(180) 
    stop()
    #reposition()
    print("vou te pegar")
    close_claw(250)
    reposition()
    move_forward_cm(4)
    #verificar se tem algo na frente por preucação
    close_claw()
    move_backward_cm(6)
    stop()
    reposition()
    stop()
    move_backward_cm(10)
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
    elif place == "Null":
        print("Nada encontrado")
        open_claw()
        find_passenger(False)

        
            
#Funções referentes ao trajeto do robô

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
            move_forward_cm(70)
            turn_right(90)
            move_forward_cm(10)
            if obstacle():
                move_backward_cm(10)
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
                turn_right(90, True, "R")
    leave_passenger()

def get_break():
    while not saw_yellow() and not saw_black():
        move_forward(300)
    move_backward_cm(2)
    stop()
    reposition()

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
            if obstacle():
                move_backward_cm(75)
                turn_left(90)
                move_forward_cm(70)
                turn_right(90)
                move_forward_cm(130)
                turn_right(90)
                move_forward_cm(35)
                turn_right(90)
            else:
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
        turn_left(90, True, "L")
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
            move_forward_cm(22, True, 'F')
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
    reposition()
    enter()
    open_claw()
    print("dando ré")
    move_backward_cm(10)
    stop()
    while not saw_yellow() and not saw_black():
        move_forward(180)
    stop()
    reposition()
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
            reposition()
            reposition()
            move_forward_cm(10)
            break
        elif count < 2 and yellowLeft() and blackRight():
            stop()
            reposition()
            reposition()
            move_backward_cm(5)
            turn_right(90)
            move_backward_cm(3)
            stop()
            turn_left(90)
            stop()
            reposition()
            move_backward_cm(2)
            count += 1
        elif count < 2 and yellowRight() and blackLeft():
            stop()
            reposition()
            reposition()
            move_backward_cm(5)
            turn_left(90)
            move_backward_cm(3)
            stop()
            turn_right(90)
            stop()
            reposition()
            move_backward_cm(2)
            count += 1
        elif count < 2 and sensor_color_left.rgb()[0] >= media_R_min and sensor_color_left.rgb()[0] <= media_R_max:
            print("Porcentagem 0,5% esquerda")
            stop()
            reposition()
            move_backward_cm(3)
            turn_left(90)
            move_backward_cm(3)
            stop()
            turn_right(90)
            stop()
            reposition()
            move_backward_cm(2)
            count += 1

        elif count < 2 and sensor_color_right.rgb()[0]>= media_L_min and sensor_color_right.rgb()[0] <= media_L_max:
            print("Porcentagem 0,5% direita")
            stop()
            reposition()
            move_backward_cm(3)
            turn_right(90)
            move_backward_cm(3)
            stop()
            turn_left(90)
            stop()
            reposition()
            move_backward_cm(2)
            count += 1
        else:
            move_forward_cm(1)

