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

velocity = 2
class command_stack():
    def __init__(self):
        self.lista = []
    
    def forward_cm(self,cm):
        tempo = StopWatch()
        tempo.pause()
        tempo.reset()
        print(tempo.time())
        duration = ((cm*10)/velocity)*10
        while tempo.time() <= duration:
            tempo.resume()
            motors.drive(velocity*100, 0)
            if obstacle():
                stop()
                self.reset()
                break
        stop()
    def backward_cm(self, cm): #volta para trás metodo
        tempo = StopWatch()
        tempo.pause()
        print(1)
        tempo.reset()
        turn_right(180)
        print(2)
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
        if command[0] == "straight_cm":
            self.forward_cm(command[1])
        elif command[0] == "back_cm":
            move_backward_cm(command[1])
        elif command[0] == "turn_left":
            turn_left(command[1])
        elif command[0] == "back":
            move_backward(command[1])
        elif command[0] == "forward":
            move_forward(command[1])
        elif command[0] == "turn_right":
            turn_right(command[1])
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

stack = command_stack()

def circle_right():
    motor_right.run(80)
    motor_left.run(-10)

def circle_left():
    motor_left.run(80)
    motor_right.run(-10)

motors = DriveBase(motor_left, motor_right, wheel_diameter = 42.1, axle_track = 107.6)
#motors.distance_control.pid(200 , 600, 2,  8, 2, 0)
motors.settings(150, 300, 100, 250)

def move_forward2(velocity):
    motors.drive(velocity, 0)

def move_forward(velocity):
    kp_right = 1.08 #0.06
    kp_left = 1.7
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
        
    

def move_forward_cm(cm, save = False, reference = "B", standard = True) :
    if not standard:
        tempo = StopWatch()
        tempo.pause()
        tempo.reset()
        print(tempo.time())
        velocity = 200
        duration = ((cm*10)/velocity)*1000
        while tempo.time() <= duration:
            tempo.resume()
            move_forward(velocity*360)
            if obstacle() or saw_red():
                stop()
                reposition("Red")
                move_backward_cm(3)
                wait(500)
                turn_right(90)
                turn_right(90)
                wait(500)
                move_forward_cm(65, False, "S", False)
                break
        stop()
    else:
        motors.straight(cm*10)
    if save and reference == "F":
        stack.append(["straight_cm", cm])
    elif save:
        stack.append(["back_cm", cm])
        
def move_backward(velocity):
    motors.drive(-velocity, 0)
    
def move_backward_cm(mm, save = False, reference = "F") :
    motors.straight(-mm*10)
    if save and reference == "F":
        stack.append(["straight_cm", mm])
    elif save:
        stack.append(["back_cm", mm])
    
def move_right(velocity):
    motors.drive(0, velocity)

def turn_left(angle, save = False, reference = 'R'):
    kp = 0.9
    ki = 0.0002
    set_point = 824*(angle/360)
    set_point = round(set_point)
    stop_motors()
    while not (abs(set_point - motor_right.angle()) <= 18):
        current_angle = motor_right.angle()
        current_angle  += calculate_pid(kp, ki, set_point, current_angle)
        motor_left.run_angle(200, - current_angle -(set_point - motor_right.angle())*0.1, wait=False)
        motor_right.run_angle(200, current_angle +(set_point - motor_right.angle())*0.1, wait=True)
        #print(" motor right and left :",motor_right.angle(), motor_left.angle())
        print(" motor left :",motor_left.angle())
        print("difference", abs(set_point - motor_right.angle()))
        print(set_point)
    stop_motors()
    if save and reference == 'L':
        stack.append(["turn_left", angle])
    elif save and reference == 'R':
        stack.append(["turn_right", angle])



def turn_right(angle, save = False, reference = 'L'):
    kp = 0.92
    ki = 0.00007
    print("rightou")
    set_point = 824*(angle/360)
    set_point = round(set_point)
    stop_motors()
    while not (abs(set_point-motor_left.angle()) <= 21):
        current_angle = motor_left.angle()
        current_angle  += calculate_pid(kp, ki, set_point, current_angle)
        motor_left.run_angle(200, current_angle  + (set_point - motor_right.angle())*0.1, wait=False)
        motor_right.run_angle(200, -current_angle  -(set_point - motor_right.angle())*0.1, wait=True)
        #print(" motor left :",motor_left.angle())
        #print("difference", abs(set_point - motor_left.angle()))
        #print(set_point)
       # print(current_angle)
    stop_motors()
    # print("Saí")
    if save and reference == 'L':
        stack.append(["turn_left", angle])
    elif save and reference == 'R':
        stack.append(["turn_right", angle])

def turn_right_180(angle = 180, save = False):
    #kp = 0.1
    kp = 0.58
    ki = 0.0002
    set_point = 828*(angle/360)
    set_point = round(set_point)
    stop_motors()
    while not (abs(set_point-motor_left.angle()) <= 18):
        current_angle = motor_left.angle()
        control_signal = calculate_pid(kp, ki, set_point, current_angle)
        motor_left.run_angle(200, control_signal, wait=False)
        motor_right.run_angle(200, -control_signal, wait=True)
        # print(" motor right and left :",motor_right.angle(), motor_left.angle())
        # print("difference", set_point - motor_left.angle())
    stop_motors()
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

def stop_motors():
    motors.stop()
    motor_left.reset_angle(0)
    motor_right.reset_angle(0)


    
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
    motors.stop()
    if save:
        stack.append(['stop'])
    #stack.append(["stop"])

def calibrate():
    turn_right(360)
    stop()
    wait(1000)

def reposition(color):
    print("Se alinhando")
    print("Entrou")
    if seeRight() != color and seeLeft() == color:
        print("Diferenciou")
        #if color == "White":
         #   while seeRight() != color:
          #      circle_right()
        while seeRight() != color:
            circle_right()
        stop()
    elif seeRight() == color and seeLeft() != color:
        print("1")
        while seeLeft() != color:
            circle_left()
        stop()
    elif seeRight() == seeLeft():
        print("2")
        #pass
    elif seeRight() != color and seeLeft() != color:
        while seeRight() != color:
            circle_right()
        stop()
    print("rodou tudo")


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

