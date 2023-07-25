from pybricks.ev3devices import (ColorSensor, UltrasonicSensor)
from pybricks.parameters import Port

ultra_front_senot = UltrasonicSensor(Port.S3)
color_front_sensor = ColorSensor(Port.S4) 

#outro brick
color_left_sensor = ColorSensor(Port.S3) #cima