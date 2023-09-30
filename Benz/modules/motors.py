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

def circle_right():
    motor_right.run(80)
    motor_left.run(-10)

def circle_left():
    motor_left.run(80)
    motor_right.run(-10)

def move_forward2(velocity):
    motors.drive(velocity, 0)

def move_forward(velocity):
    kp_right = 1.08 #0.06
    kp_left = 0.38  #1.7
     #0.0648
    ki_right = -0.7 #0.00000025
    ki_left = 0.01

  #  global control_signal_right
   # global control_signal_left

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
           
def moving_straight_cm(distance, velocity = 380):
    motor_left.reset_angle(0)
    motor_right.reset_angle(0)
    angle = (distance * 1460)/60
    while motor_left.angle() < angle or motor_right.angle() < angle:
        move_forward(velocity)  
    # print(left_motor.angle(), right_motor.angle()) # Teste para o erro
 #   print("Esquerdo", (motor_left.angle()))
  #  print("Direito", (motor_right.angle()))
    
    stop()

def moving_backward_cm(distance, velocity = 320):
    motor_left.reset_angle(0)
    motor_right.reset_angle(0)
    angle = (distance * -1321)/55+6
    while motor_left.angle() > angle or motor_right.angle() > angle:
        move_backward(-velocity)  
    # print(left_motor.angle(), right_motor.angle()) # Teste para o erro
    print("Esquerdo", (motor_left.angle()))
    print("Direito", (motor_right.angle()))
    stop()

def move_forward_cm(cm, save = False, reference = "B") :
    if cm < 11:
        motor_left.reset_angle(0)
        motor_right.reset_angle(0)
        moving_straight_cm(cm, 150)
    else:
        motor_left.reset_angle(0)
        motor_right.reset_angle(0)
        moving_straight_cm(cm)
    #motors.straight(cm*10)
    if save and reference == "F":
        stack.append(["forward_cm", cm])
    elif save:
        stack.append(["back_cm", cm])
        
def move_backward(velocity):
    kp_right = 0.6315 #0.06
    kp_left = 0.635
    print("movando back")
     #0.0648
    ki_right = 0 #0.00000025
    ki_left = 0


    control_signal_right = motor_right.speed()
    control_signal_left = motor_left.speed()


    control_signal_right += calculate_pid(kp_right, ki_right, velocity, control_signal_right)
    control_signal_left += calculate_pid(kp_left, ki_left, velocity, control_signal_left)

    if control_signal_left < 1 and control_signal_left > -1:
        control_signal_left = 1
    if control_signal_right < 1 and control_signal_right > -1:
        control_signal_right = 1
    
    motor_left.run(-control_signal_left)
    motor_right.run(-control_signal_right)
   # print(" motor right and left :",motor_right.angle(), motor_left.angle())
    
def move_backward_cm(mm, save = False, reference = "F") :
   
    if mm < 11:
        motor_left.reset_angle(0)
        motor_right.reset_angle(0)
        moving_backward_cm(mm, 150)
    else:
        motor_left.reset_angle(0)
        motor_right.reset_angle(0)
        moving_backward_cm(mm)

    if save and reference == "F":
        stack.append(["straight_cm", mm])
    elif save:
        stack.append(["back_cm", mm])
    
def move_right(velocity):
    motors.drive(0, velocity)

def turn_left(angle, save = False, reference = 'R'):
    kp = 0.87
    ki = 0.00002 #0.0000001 #se tiver rodando mais coloca menos
    wait(500)
    set_point = 815*(angle/360)
    set_point = round(set_point)
    stop()
    while not (abs(set_point - motor_right.angle()) <= 20):
        current_angle = motor_right.angle()
        current_angle  += calculate_pid(kp, ki, set_point, current_angle)
        motor_left.run_angle(200, - current_angle -(set_point - motor_right.angle())*0.1, wait=False)
        motor_right.run_angle(200, current_angle +(set_point - motor_right.angle())*0.1, wait=True)
        #print(" motor right and left :",motor_right.angle(), motor_left.angle())
        #print(" motor left :",motor_left.angle())
        print("difference", abs(set_point - motor_right.angle()))
       # print(set_point)
    stop()
    if save and reference == 'L':
        stack.append(["turn_left", angle])
    elif save and reference == 'R':
        stack.append(["turn_right", angle])

def regular():
    motors.turn(300)
    while not blackRight() or not blackLeft():
        motors.turn(1)
    motors.stop()
    lista = [motor_left.angle(), motor_right.angle()]
    print(lista)
    return lista

def turn_right(angle, save = False, reference = 'L'):
    kp = 0.85
    ki = 0.00006 #sempre olhar isso
    wait(500)
    set_point = 815*(angle/360)
    set_point = round(set_point)
    stop()
    while not (abs(set_point-motor_left.angle()) <= 82):
        current_angle = motor_left.angle()
        current_angle  += calculate_pid(kp, ki, set_point, current_angle)
        motor_left.run_angle(200, current_angle  + (set_point - motor_right.angle())*0.1, wait=False)
        motor_right.run_angle(200, -current_angle  -(set_point - motor_right.angle())*0.1, wait=True)
        #print(" motor left :",motor_left.angle())
        #regular sempre
        print("difference", abs(set_point - motor_left.angle()))

        #print(set_point)
       # print(current_angle)
    print("rightou")
    stop()
    # print("Saí")
    if save and reference == 'L':
        stack.append(["turn_left", angle])
    elif save and reference == 'R':
        stack.append(["turn_right", angle])

def turn_right_180(angle = 180, save = False):
    #kp = 0.1
    kp = 0.58
    ki = 0.0002
    set_point = 811*(angle/360)
    set_point = round(set_point)
    stop()
    while not (abs(set_point-motor_left.angle()) <= 18):
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



def calculate_pid(kp, ki, set_point, current_value):
    integral = 0
    error = set_point - current_value
    proporcional = error * kp
    integral += error
    i = integral*ki
    control_signal = proporcional + i

    return control_signal

    
def move_left(velocity):
    motors.drive(0, -velocity)


    
def turn_90_left_and_move_distance(distance):
    motors.straight(distance)
    motors.turn(-90)
    stop()

    
def turn_90_right_and_move_distance(distance):
    motors.straight(distance)
    motors.turn(90)
    stop()

def turn_180():
    print("turn")
    motors.turn(180)
    print("já tornou")
    
def stop(save = False):
    motor_left.hold()
    motor_right.hold()
    while motor_right.speed() != 0 or motor_left.speed() != 0:
        wait(500)
    motor_left.reset_angle(0)
    motor_right.reset_angle(0)
    # print(" motor right and left :",motor_right.speed(), motor_left.speed())
  
   # wait(200) 
    if save:
        stack.append(['stop'])
    #stack.append(["stop"])

def calibrate():
    turn_right(360)
    stop()
    wait(1000)



def reposition():
    stop()
    left = True
    right = True
    while seeLeft() != "White" or seeRight() != "White":
        move_backward(100)
        print(1)
    stop()
    move_forward(60)
    while seeLeft() == "White" or seeRight() == "White":
        print("RIGHT ", seeRight(), "LEFT ", seeLeft())
        if seeLeft() != "White" and left:
            motor_left.hold()
            motor_left.stop()
            motor_right.run(20)
            motor_left.run(-1)
            left = False
        if seeRight() != "White" and right:
            motor_right.hold()
            motor_right.stop()
            motor_left.run(20)
            motor_right.run(-1)
            right = False
        if right and left:
            move_forward(60)
        if not right and not left:
            return 0
        




def reposition_all():
	if reposition("Red"):
		pass
	elif reposition("Blue"):
		pass
	elif reposition("Black"):
		pass
	elif reposition("Green"):
		pass
	elif reposition("Yellow"):
		pass
	else:
		reposition_wall()
		print("Nothing to reposition")

def reposition_wall():
    colors =  ["Yellow","Black"]
    print(seeRight(), " ", seeLeft())
    if (seeRight() in colors and seeLeft() in colors):
        print("Perfecto")
    elif seeRight() in colors and seeLeft() not in  colors:
        print("1")
        while seeLeft() not in colors:
            circle_left()
        stop()
    elif seeRight() not in colors and seeLeft() in  colors:
        print("2")
        while seeRight() not in colors:
            circle_right()
        stop()
    else:
        print("Todo fudido")
    print("rodou tudo")


def verification_path():
    for i in range(4):
        turn_right(90)
        if not obstacle():
            pass
        else:
            return True
    return False