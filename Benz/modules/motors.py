from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

from modules.colors import *
from modules.detect import *

motor_left = Motor(Port.A) 
motor_right = Motor(Port.B)

control_signal_right = 0
control_signal_left = 0

motors = DriveBase(motor_left, motor_right, wheel_diameter = 42.1, axle_track = 107.6)
#motors.distance_control.pid(200 , 600, 2,  8, 2, 0)
motors.settings(150, 300, 100, 250)


velocity = 2
class command_stack():
    def __init__(self):
        self.lista = []
    
    def forward_cm(self,cm):
        tempo = StopWatch()
        tempo.pause()
        tempo.reset()
        print(tempo.time())
        duration = ((cm*10)/340)*11
        while tempo.time() <= duration:
            tempo.resume()
            move_forward(340)
            if obstacle():
                stop()
                self.reset()
                break
        stop()
    def backward_cm(self, cm): #volta para trás metodo
        tempo = StopWatch()
        tempo.pause()
       # print(1)
        tempo.reset()
       # turn_right(180)
        #print(2)
        duration = ((cm*10)/velocity)*10
        print(duration)
        tempo.resume()
        while tempo.time() <= duration:
            motors.drive(velocity*100, 0)
            if obstacle():
                stop()
                self.reset()
                break
        stop()
        turn_right(180)

    def append(self, command):
        self.lista.append(command)
        return True

    def size(self):
        return len(self.lista)
    def reset(self):
        while not self.isEmpty():
            self.lista.pop()
    def isEmpty(self):
        return len(self.lista) == 0

    def unpille(self):
        command = self.lista.pop()
        print(command)
        print(command[0])
        print(command[1])
        if command[0] == "straight_cm":
            self.forward_cm(command[1])
        elif command[0] == "back_cm":
            move_backward_cm(command[1])
        elif command[0] == "turn_left":
            turn_left(command[1])
        elif command[0] == "back":
            move_backward(command[1])
        elif command[0] == "forward_cm":
            move_forward_cm(command[1])
        elif command[0] == "turn_right":
            print("Antes de entrar na função")
            turn_right(command[1])
            print("Opa, sai")
        elif command[0] == "stop":
            stop()
        return command
    def onTop(self):
        return self.lista[-1]
    
    def reverse(self):    
        while not self.isEmpty():
            print(self.lista)
            print(self.size())
            self.unpille()
            stop()

stack = command_stack()

def save(reference, param):
    if reference == "F":
        stack.append(["forward_cm", param])
    elif reference == "B":
        stack.append(["back_cm", param])
    elif reference == "L":
        stack.append(["turn_left", param])
    elif reference == "R":
        stack.append(["turn_right", param])
    
def move_forward(velocity):
    kp_right = 0.72 #1.08
    kp_left = 0.78
     #0.38 
    
    #kp left crescendo vai direita
    
      
    ki_right = 0 #0.0004 #0.005 #-0.7
    ki_left = 0 #0.0001 #0.08 #0.01

    control_signal_right = motor_right.speed()
    control_signal_left = motor_left.speed()
    

    control_signal_right += calculate_pid(kp_right, ki_right, velocity, control_signal_right)
    control_signal_left += calculate_pid(kp_left, ki_left, velocity, control_signal_left)

    if control_signal_left < 1 and control_signal_left > -1:
        control_signal_left = 1
    if control_signal_right < 1 and control_signal_right > -1:
        control_signal_right = 1
    
    motor_left.run(control_signal_left)
    motor_right.run(control_signal_right)
           
def moving_straight_cm(distance, velocity = 600):
    motor_left.reset_angle(0)
    motor_right.reset_angle(0)
    angle = (distance * 1580)/60
    while motor_left.angle() < angle or motor_right.angle() < angle:
        move_forward(velocity)  
        
    # print(left_motor.angle(), right_motor.angle()) # Teste para o erro
    print("Esquerdo", (motor_left.angle()))
    print("Direito", (motor_right.angle()))
    
    stop()

def moving_backward_cm(distance, velocity = 1400):
    motor_left.reset_angle(0) 
    motor_right.reset_angle(0)
    angle = (distance * -1321)/52
    while ( motor_left.angle() > angle or motor_right.angle() > angle ) or (motor_left.angle == 0 and motor_right.angle == 0) :
        move_backward(-velocity)  
    # print(left_motor.angle(), right_motor.angle()) # Teste para o erro
    # print("Esquerdo", (motor_left.angle()))
    # print("Direito", (motor_right.angle()))
    stop()

def move_forward_cm(cm, save = False, reference = "F") :
    motor_left.reset_angle(0)
    motor_right.reset_angle(0)
    if cm > 0 and cm < 3:
        moving_straight_cm(cm, 220) #! analizar esses valores
    elif cm < 11:
        moving_straight_cm(cm, 350) #! analizar esses valores
    else:
        moving_straight_cm(cm)

    if save and reference == "F":
        stack.append(["forward_cm", cm])
    elif save:
        stack.append(["back_cm", cm])
        
def move_backward(velocity):
    kp_right = 0.6315 #0.06
    kp_left = 0.63
    ki_right = 0.0000000001 #0.00000025
    ki_left = 0.00000003


    control_signal_right = motor_right.speed()
    control_signal_left = motor_left.speed()


    control_signal_right += calculate_pid(kp_right, ki_right, -velocity, control_signal_right)
    control_signal_left += calculate_pid(kp_left, ki_left, -velocity, control_signal_left)

    if control_signal_left < 1 and control_signal_left > -1:
        control_signal_left = 1
    if control_signal_right < 1 and control_signal_right > -1:
        control_signal_right = 1
    
    motor_left.run(-control_signal_left)
    motor_right.run(-control_signal_right)
    print(" motor right and left :",motor_right.angle(), motor_left.angle())
    
def move_backward_cm(mm, save = False, reference = "B") :
   
    if mm < 11:
        motor_left.reset_angle(0)
        motor_right.reset_angle(0)
        moving_backward_cm(mm, 400)
    else:
        motor_left.reset_angle(0)
        motor_right.reset_angle(0)
        moving_backward_cm(mm)

    if save and reference == "F":
        stack.append(["forward_cm", mm])
    elif save:
        
        stack.append(["back_cm", mm])


def turn_left(angle, save = False, reference = 'R'):
    kp_left = 0.87 # Crecendo vai pra direita Diminuindo vai pra esquerda 0.953
    ki_left = 0 #0.001 #0.00006 #sempre olhar isso
    kp_right = 0.98 # Crecendo vai mais Diminuindo vai menos
    ki_right = 0 # 0.001 #0.001 #0.0005  #0.00006 #sempre olhar isso
    # wait(500)
    set_point = 784*(angle/360)
    set_point = round(set_point)
    
    current_angle_left = motor_left.angle()
    current_angle_right = motor_right.angle()
    current_angle_left  += calculate_pid(kp_left, ki_left, set_point, current_angle_left)
    current_angle_right  += calculate_pid(kp_right, ki_right, set_point, current_angle_right)
    
    motor_left.run_angle(200, -current_angle_left  - (set_point - motor_left.angle())*0.1, wait=False)
    motor_right.run_angle(200, current_angle_right  + (set_point - motor_left.angle())*0.1, wait=True)
    #print(" motor left :",motor_left.angle())
    #regular sempre
    print("difference", abs(set_point - motor_left.angle()))
    #print(set_point)
    # print(current_angle)
    print("leftou")

    if save and reference == 'L':
        stack.append(["turn_left", angle])
    elif save and reference == 'R':
        stack.append(["turn_right", angle])
''' kp = 1.01
    ki = 0.00002 #0.0000001 #se tiver rodando mais coloca menos
    wait(500)
    set_point = 784*(angle/360)
    set_point = round(set_point)
    stop()
    while not (abs(set_point - motor_right.angle()) <= 177):
        current_angle = motor_right.angle()
        current_angle  += calculate_pid(kp, ki, set_point, current_angle)
        motor_left.run_angle(200, - current_angle , wait=False)
        motor_right.run_angle(200, current_angle, wait=True)
        #print(" motor right and left :",motor_right.angle(), motor_left.angle())
        #print(" motor left :",motor_left.angle())
        print("difference", abs(set_point - motor_right.angle()))
       # print(set_point)
    stop()'''


def turn_right(angle, save = False, reference = 'L'): #check
    kp_left = 0.94 # 47Crecendo vai pra direita Diminuindo vai pra esquerda 0.953
    ki_left = 0 #0.0001#0.0000007 #0.00006 #sempre olhar isso
    kp_right = 0.89 # Crecendo vai pra direita Diminuindo vai pra esquerda
    ki_right = 0.001#0.000005 #0.00006 #sempre olhar isso
    # wait(500)
    set_point = 784*(angle/360)
    set_point = round(set_point)
    
    current_angle_left = motor_left.angle()
    current_angle_right = motor_right.angle()
    current_angle_left  += calculate_pid(kp_left, ki_left, set_point, current_angle_left)
    current_angle_right  += calculate_pid(kp_right, ki_right, set_point, current_angle_right)
    
    motor_left.run_angle(200, current_angle_left  + (set_point - motor_right.angle())*0.1, wait=False)
    motor_right.run_angle(200, -current_angle_right  -(set_point - motor_right.angle())*0.1, wait=True)
    #print(" motor left :",motor_left.angle())
    #regular sempre
    print("difference", abs(set_point - motor_left.angle()))
    #print(set_point)
    # print(current_angle)
    print("rightou")
    stop()
    # print("SaÃ­")
    if save and reference == 'L':
        stack.append(["turn_left", angle])
    elif save and reference == 'R':
        stack.append(["turn_right", angle])
'''    kp = 0.951 # Crecendo vai pra direita Diminuindo vai pra esquerda
    ki = 0 #0.00006 #sempre olhar isso
    # wait(500)
    set_point = 784*(angle/360)
    set_point = round(set_point)

    stop()
    
    while not (abs(set_point-motor_left.angle()) <= 177): #18
        current_angle = motor_left.angle()
        current_angle  += calculate_pid(kp, ki, set_point, current_angle)
        motor_left.run_angle(200, current_angle  + (set_point - motor_right.angle())*0.1, wait=False)
        motor_right.run_angle(200, -current_angle  -(set_point - motor_right.angle())*0.1, wait=True)
        #print(" motor left :",motor_left.angle())
        #regular sempre
        print("difference", abs(set_point - motor_left.angle()))
        #print(set_point)
       # print(current_angle)'''

def turn_right_180(angle = 180, save = False): #! ajustar
    kp = 0.58
    ki = 0.0002
    set_point = 811*(angle/360)
    set_point = round(set_point)
    stop()
    print(" motor right and left :",motor_right.angle(), motor_left.angle())
    while not (abs(set_point-motor_left.angle()) <= 18): #18
        current_angle = motor_left.angle()
        control_signal = calculate_pid(kp, ki, set_point, current_angle)
        motor_left.run_angle(200, control_signal, wait=False)
        motor_right.run_angle(200, -control_signal, wait=True)
        # print(" motor right and left :",motor_right.angle(), motor_left.angle())
        # print("difference", set_point - motor_left.angle())
    stop()
    # print("Saí")
    if save:
        stack.append(["turn_left", angle])

def jota(inverted = False):
    move_forward_cm(65)
    if inverted:
        turn_right(90)
    else:
        turn_left(90)
    move_forward_cm(60)
    if inverted:
        turn_right(90)
    else:
        turn_left(90)
    move_forward_cm(95)
    


    
def stop(save = False):
    motor_left.hold()
    motor_right.hold()
    while motor_right.speed() != 0 or motor_left.speed() != 0:
        wait(200)
    motor_left.reset_angle(0)
    motor_right.reset_angle(0)

    if save:
        stack.append(['stop'])



def reposition():
    stop()
    left = True
    right = True
    count_l = 0
    count_r = 0

    while seeLeft() != "White" or seeRight() != "White":
        move_backward_cm(1)
        print(1)
        
    stop()
    move_forward(100)
    while seeLeft() == "White" or seeRight() == "White":
        #print("COUNT LL ", count_l, "    COUNT RRR   ", count_r)
        if left and not right :
            count_l += 1
        if right and not left :
            count_r += 1

        if seeLeft() != "White" and left:
            motor_left.hold()
            motor_left.stop()
            motor_right.run(60)
            motor_left.run(-3)
            left = False
        if seeRight() != "White" and right:
            motor_right.hold()
            motor_right.stop()
            motor_left.run(60)
            motor_right.run(-3)
            right = False
        if count_l >= 100 or count_r >= 100:
            right = False
            left = False
            for i in range(count_l):
                motor_right.run(1)
                motor_left.run(-60)
            for i in range( count_r):
                motor_right.run(-60)
                motor_left.run(1)
                move_backward_cm(8)
                reposition()
        if right and left:
            move_forward(100)
        if not right and not left:
            stop()
            #print("PORRAAAAAA")
            return 0
        




def verification_path():
    for i in range(4):
        turn_right(90)
        if not obstacle():
            pass
        else:
            return True
    return False





# FUNÇÕES DE TESTES ------------------------------------------------------

def regular(): # Função de ajustar os valores
    motors.turn(280)
    while not blackRight() or not blackLeft():
        motors.turn(1)
    motors.stop()
    lista = [motor_left.angle(), motor_right.angle()]
    print(lista)
    return lista


def calculate_pid(kp, ki, set_point, current_value):
    integral = 0
    error = set_point - current_value
    proporcional = error * kp
    integral += error
    i = integral*ki
    control_signal = proporcional + i
   # print("Control ", control_signal)
    return control_signal