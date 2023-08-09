from pybricks.ev3devices import (ColorSensor, UltrasonicSensor,InfraredSensor )
from pybricks.nxtdevices import ColorSensor as ColorNxt
from pybricks.parameters import Port

#color_front_sensor = UltrasonicSensor(Port.S4)
#color_front_sensor = ColorSensor(Port.S3) 

infra_sensor = InfraredSensor(Port.S4)

def collision():
     if (ultra_front_sensor.distance() > 0) :
        print("cuidado motorista")

def side_detection():
    if infra_sensor.distance() <= 15: ############### lembrar de adicionar sensor
        return True
    else:
        return False
#outro brick
#color_left_sensor = ColorSensor(Port.S3) #cima