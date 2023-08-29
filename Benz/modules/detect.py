from pybricks.ev3devices import (ColorSensor, UltrasonicSensor,InfraredSensor )
from pybricks.nxtdevices import ColorSensor as ColorNxt
from pybricks.parameters import Port
from pybricks.tools import StopWatch
from pybricks.hubs import EV3Brick
from modules.motors import *
from pybricks.messaging import BluetoothMailboxServer, TextMailbox
import time

ultra_sensor = UltrasonicSensor(Port.S3)
infra_sensor = InfraredSensor(Port.S4)

ev3 = EV3Brick()
'''
server = BluetoothMailboxServer()
eve3box = TextMailbox('greeting', server)

print('waiting for connection...')
server.wait_for_connection()
print('connected!')
'''
def obstacle(default = True):
    if default:
        if ultra_sensor.distance() <= 200:
            ev3.speaker.beep(200)
            return True
        else:
            ev3.speaker.beep(200)
            ev3.speaker.beep(300)
            return False
    else:
        if infra_sensor.distance() <= 23:
            ev3.speaker.beep(200)
            return True
        else:
            ev3.speaker.beep(200)
            ev3.speaker.beep(300)
            return False


def message():
    eve3box.send("True")
    eve3box.wait()
    print(eve3box.read())
    eve3box.send("False")
    return eve3box.read().split()




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


def final_tube():
    tempo = StopWatch()
    tempo.reset()
    while tempo.time() <= 2000:
        move_backward(80) #implementar questão do tempo sem ver nada
        if side_detection(): #ainda sendo implementado
            print("oi")
            tempo.reset()
    stop()
    print("Ready to start taking passangers")