from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait


motor_left = Motor(Port.A) 
motor_right = Motor(Port.B)


motors = DriveBase(motor_left, motor_right, wheel_diameter = 42.1, axle_track = 94.3)

motors.settings(150, 300, 100, 3000)

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
    motors.turn(-90)

def turn_90_right():
    motors.turn(90)
    
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