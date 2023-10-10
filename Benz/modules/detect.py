from pybricks.ev3devices import (ColorSensor, UltrasonicSensor,InfraredSensor )
from pybricks.nxtdevices import ColorSensor as ColorNxt
from pybricks.parameters import Port
from pybricks.tools import StopWatch
from pybricks.hubs import EV3Brick
from pybricks.messaging import BluetoothMailboxServer, TextMailbox
import time

ultra_sensor = UltrasonicSensor(Port.S3)
infra_sensor = InfraredSensor(Port.S4)

ev3 = EV3Brick()

server = BluetoothMailboxServer()
eve3box = TextMailbox('greeting', server)
for i in range(900,0, -100):
    ev3.speaker.beep(i)
print('waiting for connection...')
server.wait_for_connection()
print('connected!')

def obstacle(default = "frente", distance = 39):

    if default == "frente":
        if ultra_sensor.distance() <= 180:
            ev3.speaker.beep(200)
            return True
        else:
            return False
    elif default == "lado":
        print(infra_sensor.distance())
        if infra_sensor.distance() <= distance:
            ev3.speaker.beep(200)
            return True
        else:
            return False


def message():
    eve3box.send("True")
    eve3box.wait()
    print(eve3box.read())
    eve3box.send("False")
    return eve3box.read().split()

def side_detection():
    if infra_sensor.distance() <= 8: #25 ############### lembrar de adicionar sensor
        print(infra_sensor.distance())
        return True
    else:
        return False



