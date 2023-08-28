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


def calibration_auto(sensor, array):
    global teste
    colors = sensor.rgb()
    # min
    print("Calibrando as cores")

    array[0][0] = colors[0]-8
    array[0][1] = colors[1]-8
    array[0][2] = colors[2]-8
    # max
    array[1][0] = colors[0]+8
    array[1][1] = colors[1]+8
    array[1][2] = colors[2]+8
    print("Devolvendo os valores")
    print(array)
    return array


# arrumar o marrom e verde
red = [[31, 0, 0], [47, 16, 10]]  # check

blue = [[0, 1, 5], [12, 14, 21]]  # check

#yellow = [[35, 64, 11], [55, 82, 30]]  

green = [[0, 13, 0], [11, 28, 13]]  # check

brown = [[36, 56, 54], [52, 72, 70]]  # check


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
    # elif Yellow():
    #     return "Yellow"
    else:
        return "White"


def size():
    if sensor_sup.reflection() <= 20:
        return "10"
    else:
        return "15"


def check():
    color = see()
    if color == "White":
        time.sleep(1)
        color = see()
    return color + " " + size()
