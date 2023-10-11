from pybricks.parameters import Port, Stop
from pybricks.ev3devices import Motor
from pybricks.tools import  StopWatch
from pybricks.parameters import Stop


motor_claw = Motor(Port.C)

time_open_claw = 2500 

def open_claw2(seconds = 750):
    global time_open_claw
    motor_claw.run_time(seconds, time_open_claw, Stop.HOLD, True)
    motor_claw.hold()

def close_claw2(seconds =  500) : 
    global time_open_claw
    motor_claw.run_time(-seconds, time_open_claw, Stop.HOLD, True)
    motor_claw.hold()
    


def close_claw(quantidade = 1000 , time = 1900 ):
    motor_claw.run_angle(time, -quantidade, wait = True)
    motor_claw.hold()

def open_claw(quantidade = 1600, time = 1900 ):
    motor_claw.run_angle(time, quantidade, wait = True)
    motor_claw.hold()

