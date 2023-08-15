from pybricks.parameters import Color
from pybricks.parameters import Port
from pybricks.ev3devices import ColorSensor
from pybricks.nxtdevices import ColorSensor as ColorNxt

sensor_color = ColorSensor(Port.S2)
sensor_sup = ColorNxt(Port.S3)


def calibration(sensor):
    print(sensor.rgb())

# Declaration of RGB values of color sensors
# min and max


# arrumar o marrom e verde
red = [[50, 3, 0], [72, 25, 10]]  # check

blue = [[0, 7, 10], [12, 19, 21]]  # check

yellow = [[35, 64, 11], [55, 82, 30]]  

green = [[0, 18, 0], [12, 32, 12]]#check


brown = [[62, 62, 57], [78, 80, 70]]  


def calibration(sensor):
    print(sensor.rgb())


def Red():
    rgb = sensor_color.rgb()
    return ((red[0][0] <= rgb[0] and rgb[0] <= red[1][0]) and (red[0][1] <= rgb[1] and rgb[1] <= red[1][1]) and (red[0][2] <= rgb[2] and rgb[2] <= red[1][2]))


def Green():
    rgb = sensor_color.rgb()
    return ((green[0][0] <= rgb[0] and rgb[0] <= green[1][0]) and (green[0][1] <= rgb[1] and rgb[1] <= green[1][1]) and (green[0][2] <= rgb[2] and rgb[2] <= green[1][2]))


def Black():
    rgb = sensor_color.rgb()
    return ((black[0][0] <= rgb[0] and rgb[0] <= black[1][0]) and (black[0][1] <= rgb[1] and rgb[1] <= black[1][1]) and (black[0][2] <= rgb[2] and rgb[2] <= black[1][2]))


def Blue():
    rgb = sensor_color.rgb()
    return ((blue[0][0] <= rgb[0] and rgb[0] <= blue[1][0]) and (blue[0][1] <= rgb[1] and rgb[1] <= blue[1][1]) and (blue[0][2] <= rgb[2] and rgb[2] <= blue[1][2]))


def Yellow():
    rgb = sensor_color.rgb()
    return ((yellow[0][0] <= rgb[0] and rgb[0] <= yellow[1][0]) and (yellow[0][1] <= rgb[1] and rgb[1] <= yellow[1][1]) and (yellow[0][2] <= rgb[2] and rgb[2] <= yellow[1][2]))


def Brown():
    rgb = sensor_color.rgb()
    return ((brown[0][0] <= rgb[0] and rgb[0] <= brown[1][0]) and (brown[0][1] <= rgb[1] and rgb[1] <= brown[1][1]) and (brown[0][2] <= rgb[2] and rgb[2] <= brown[1][2]))


def see():
    if Red():
        return "Red"
    elif Blue():
        return "Blue"
    elif Green():
        return "Green"
    elif Brown():
        return "Brown"
    elif Yellow():
        return "Yellow"
    else:
        return "White"


def size():
    if sensor_sup.reflection() <= 20:
        return "10"
    else:
        return "15"


def check():
    color = see()
    return color + " " + size()
