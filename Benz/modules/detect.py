from pybricks.ev3devices import (ColorSensor, UltrasonicSensor)
from pybricks.parameters import Port

color_front_sensor = UltrasonicSensor(Port.S4)
color_front_sensor = ColorSensor(Port.S3) 

def collision():
     if (ultra_front_sensor.distance() > 0) :
        print("cuidado motorista")

def side_detection():
    if "sensor da esquerda".reflection() <= 80: ############### lembrar de adicionar sensor
        return True
    else:
        return False
#outro brick
#color_left_sensor = ColorSensor(Port.S3) #cima