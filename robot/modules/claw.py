from pybricks.parameters import Port, Stop
from pybricks.ev3devices import Motor
from pybricks.tools import  StopWatch
from pybricks.parameters import Stop

motor_claw = Motor(Port.D)

time_open_claw = 2500
stopwatch = StopWatch() 

def open_claw():
    global time_open_claw
    motor_claw.run_time(600, time_open_claw, Stop.HOLD, True)
    motor_claw.hold()

def close_claw() : 
    global time_open_claw
    motor_claw.run_time(-600, time_open_claw, Stop.HOLD, True)
    motor_claw.hold()
    