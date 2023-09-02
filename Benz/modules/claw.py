from pybricks.parameters import Port, Stop
from pybricks.ev3devices import Motor
from pybricks.tools import  StopWatch
from pybricks.parameters import Stop


motor_claw = Motor(Port.D)

time_open_claw = 2500 

def open_claw(seconds = 750):
    global time_open_claw
    motor_claw.run_time(seconds, time_open_claw, Stop.HOLD, True)
    motor_claw.hold()

def close_claw(seconds = 450) : 
    global time_open_claw
    motor_claw.run_time(-seconds, time_open_claw, Stop.HOLD, True)
    motor_claw.hold()
    
