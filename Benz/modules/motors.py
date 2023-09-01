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
            if obstacle():
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

motors = DriveBase(motor_left, motor_right, wheel_diameter = 42.1, axle_track = 107)
#motors.distance_control.pid(200 , 600, 2,  8, 2, 0)
motors.distance_control.pid(200 , 600, 2,  8, 2, 0)
motors.settings(150, 300, 100, 250)

def move_forward(velocity):
    motors.drive(velocity, 0)



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

def turn_right(angle, save = False):
    stop()
    motor_left.run_angle(150, (228 * (angle / 90)), then=Stop.HOLD, wait=False)
    motor_right.run_angle(150, (-228 * (angle / 90)), then=Stop.HOLD, wait=True)
    if save:
        stack.append(["turn_left", angle])
   # stack.append(["turn_left", angle])
    
def move_left(velocity):
    motors.drive(0, -velocity)
    
def turn_left(angle, save = False):
    stop()
    motor_left.run_angle(150, (-228 * (angle / 90)), then=Stop.HOLD, wait=False)
    motor_right.run_angle(150, (228 * (angle / 90)), then=Stop.HOLD, wait=True)
 
    if save:
        stack.append(["turn_right", angle])
  #  stack.append(["turn_right", angle])
    
def turn_90_left():
    motors.turn(-92)

def turn_90_right():
    motors.turn(92)
    
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

