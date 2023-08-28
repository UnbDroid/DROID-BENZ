from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from modules.colors import *

motor_left = Motor(Port.A) 
motor_right = Motor(Port.B)

def circle_right():
    motor_right.run(80)
    motor_left.run(-10)

def circle_left():
    motor_left.run(80)
    motor_right.run(-10)

motors = DriveBase(motor_left, motor_right, wheel_diameter = 42.1, axle_track = 103)
#motors.distance_control.pid(200 , 600, 2,  8, 2, 0)
motors.distance_control.pid(200 , 600, 2,  8, 2, 0)
motors.settings(150, 300, 100, 250)

def move_forward(velocity):
    motors.drive(velocity, 0)


def move_forward_cm(mm) :
    motors.straight(mm*10)
        
def move_backward(velocity):
    motors.drive(-velocity, 0)
    
def move_backward_cm(mm) :
    motors.straight(-mm*10)
    
def move_right(velocity):
    motors.drive(0, velocity)

def turn_right(angle):
    motors.turn(angle)
    
def move_left(velocity):
    motors.drive(0, -velocity)
    
def turn_left(angle):
    motors.turn(-angle)
    
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
    
def stop():
    motors.stop()

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

