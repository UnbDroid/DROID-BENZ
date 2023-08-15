from pybricks.ev3devices import (ColorSensor, UltrasonicSensor,InfraredSensor )
from pybricks.nxtdevices import ColorSensor as ColorNxt
from pybricks.parameters import Port
from pybricks.messaging import BluetoothMailboxServer, TextMailbox
import time



server = BluetoothMailboxServer()
eve3box = TextMailbox('greeting', server)

print('waiting for connection...')
server.wait_for_connection()
print('connected!')

def message():
    eve3box.send("True")
    eve3box.wait()
    print(eve3box.read())
    eve3box.send("False")
    return eve3box.read()


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