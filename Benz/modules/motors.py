from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

from modules.colors import *
from modules.detect import *

motor_left = Motor(Port.A) 
motor_right = Motor(Port.B)


class command_stack():
    tempo = StopWatch()
    velocity = 200
    def __init__(self):
        self.lista = []
    
    def forward_cm(self,cm):
        tempo.pause()
        tempo.reset()
        duration = (cm*10)/velocity
        while tempo.time() != duration:
            motors.drive(velocity, 0)
            if obstacle(stop()):
                stop()
                self.reset()
                break
        stop(False)
    def backward_cm(self, cm):
        tempo.pause()
        tempo.reset()
        turn_right(180)
        duration = (cm*10)/velocity
        while tempo.time() != duration:
            motors.drive(velocity, 0)
            if obstacle():
                stop()
                self.reset()
                break
        stop(False)

    def append(self, command):
        self.lista.append(command)
        return True

    def size(self):
        return len(self.lista)
    def reset(self):
        while not self.isEmpty():
            self.lista.pop()
    def isEmpty(self):
        return self.lista == []

    def unpille(self):
        command = self.lista.pop(-1)
        print(command[0])
        if command[0] == "straight_cm":
            self.forward_cm(command[1])
        elif command[0] == "back_cm":
            self.backward_cm(command[1])
        elif command[0] == "turn_left":
            turn_left(command[1],False)
        elif command[0] == "back":
            move_backward(command[1],False)
        elif command[0] == "forward":
            move_forward(command[1],False)
        elif command[0] == "turn_right":
            turn_right(command[1],False)
        elif command[0] == "stop":
            stop(False)
        self.lista.pop()
        return command
    def onTop(self):
        return self.lista[-1]
    
    def reverse(self):    
        while not self.isEmpty():
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
    kp_right = 1
    kp_left = 0.68
    ki_right = 0
    ki_left = 0

    control_signal_right = calculate_pid(kp_right, ki_right, velocity, motor_right.speed())
    control_signal_left = calculate_pid(kp_left, ki_left, velocity, motor_left.speed())
    if control_signal_right > 300:
        control_signal_right = 300

    if control_signal_left > 300:
        control_signal_left = 300

    if control_signal_left < 1 and control_signal_left > -1:
        control_signal_left = 1
    if control_signal_right < 1 and control_signal_right > -1:
        control_signal_right = 1
    
    motor_left.run(control_signal_left)
    motor_right.run(control_signal_right)
        
    


def move_forward_cm(mm, save = False) :
    motors.straight(mm*10)
    if save:
        stack.append(["back_cm", mm])
        
def move_backward(velocity):
    motors.drive(-velocity, 0)
    
def move_backward_cm(mm, save = False) :
    motors.straight(-mm*10)
    if save:
        stack.append(["straight_cm", mm])
    
def move_right(velocity):
    motors.drive(0, velocity)

def turn_left(angle):
    kp = 0.1
    ki = 0
    set_point = 873*(angle/360)
    set_point = round(set_point)
    stop_motors()
    while not (abs(set_point - motor_right.angle()) <= 11):
        current_angle = motor_right.angle()
        control_signal = calculate_pid(kp, ki, set_point, current_angle)
        motor_left.run_angle(200, -control_signal -(set_point - motor_right.angle())*0.1, wait=False)
        motor_right.run_angle(200, control_signal +(set_point - motor_right.angle())*0.1, wait=True)
        print(" motor right and left :",motor_right.angle(), motor_left.angle())
        print("difference", set_point - motor_right.angle())
    stop_motors()


def turn_right(angle):
    kp = 0.1
    ki = 0
    set_point = 873*(angle/360)
    set_point = round(set_point)
    stop_motors()
    while not (abs(set_point-motor_left.angle()) <= 11):
        current_angle = motor_left.angle()
        control_signal = calculate_pid(kp, ki, set_point, current_angle)
        motor_left.run_angle(200, control_signal + (set_point - motor_right.angle())*0.1, wait=False)
        motor_right.run_angle(200, -control_signal -(set_point - motor_right.angle())*0.1, wait=True)
        print(" motor right and left :",motor_right.angle(), motor_left.angle())
        print("difference", set_point - motor_left.angle())
    stop_motors()
    print("Saí")




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

def turn_right2(angle, save = False):
    stop()
    motor_left.reset_angle(0)
    motor_right.reset_angle(0)
    valor_a_girar = (228 * (angle / 90))
    motor_left.run_angle(120, valor_a_girar, wait=False)
    motor_right.run_angle(120, -valor_a_girar, wait=True)
    print(motor_left.angle())
    print(motor_right.angle())

   # if motor_left.angle() != valor_a_girar:
    #    motor_left.run_angle(50, (motor_left.angle() - valor_a_girar), wait=True)

    #if motor_right.angle() != valor_a_girar:
     #   motor_right.run_angle(50, (motor_right.angle() + valor_a_girar), wait=True)
   
    if save:
        stack.append(["turn_left", angle])
   # stack.append(["turn_left", angle])
    
def move_left(velocity):
    motors.drive(0, -velocity)
    
def turn_left2(angle, save = False):
    stop()
    motor_left.reset_angle(0)
    motor_right.reset_angle(0)
    motor_left.run_angle(150, (-226 * (angle / 90)), wait=False)
    motor_right.run_angle(150, (226 * (angle / 90)), wait=True)
    print(motor_left.angle())
    print(motor_right.angle())
 
    if save:
        stack.append(["turn_right", angle])
  #  stack.append(["turn_right", angle])
    

    
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
    
def stop(save = True):
    motors.stop()
    if save:
        stack.append(['stop'])
    #stack.append(["stop"])

def calibrate():
    turn_right(360)
    stop()
    wait(1000)

def reposition(color):
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

