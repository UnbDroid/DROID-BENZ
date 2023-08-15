from pybricks.parameters import Color
from pybricks.parameters import Port
from pybricks.ev3devices import ColorSensor

sensor_color = ColorSensor(Port.S1)
sensor_sup = ColorSensor(Port.S2)


def calibration(sensor):
    print(sensor.rgb())

# Declaration of RGB values of color sensors
# min and max


# arrumar o marrom e verde
red = [[30, 5, 0], [49, 25, 20]]  # check

blue = [[0, 15, 43], [17, 34, 65]]  # check

yellow = [[35, 64, 11], [55, 82, 30]]  # check

green = [[30, 5, 0], [49, 25, 20]]

black = [[2, 5, 0], [15, 15, 10]]  # check

brown = [[20, 10, 0], [35, 30, 18]]  # check


# 

def red():
    rgb = sensor_color.rgb()
    return ((red[0][0] <= rgb[0] and rgb[0] <= red[1][0]) and (red[0][1] <= rgb[1] and rgb[1] <= red[1][1]) and (red[0][2] <= rgb[2] and rgb[2] <= red[1][2]))


def black():
    rgb = sensor_color.rgb()
    return ((black[0][0] <= rgb[0] and rgb[0] <= black[1][0]) and (black[0][1] <= rgb[1] and rgb[1] <= black[1][1]) and (black[0][2] <= rgb[2] and rgb[2] <= black[1][2]))


def blue():
    rgb = sensor_color.rgb()
    return ((blue[0][0] <= rgb[0] and rgb[0] <= blue[1][0]) and (blue[0][1] <= rgb[1] and rgb[1] <= blue[1][1]) and (blue[0][2] <= rgb[2] and rgb[2] <= blue[1][2]))


def yellow():
    rgb = sensor_color.rgb()
    return ((yellow[0][0] <= rgb[0] and rgb[0] <= yellow[1][0]) and (yellow[0][1] <= rgb[1] and rgb[1] <= yellow[1][1]) and (yellow[0][2] <= rgb[2] and rgb[2] <= yellow[1][2]))


def brown():
    rgb = sensor_color_right.rgb()
    return ((brown[0][0] <= rgb[0] and rgb[0] <= brown[1][0]) and (brown[0][1] <= rgb[1] and rgb[1] <= brown[1][1]) and (brown[0][2] <= rgb[2] and rgb[2] <= brown[1][2]))


def see():
    if red():
        print("vi vermelho")
        return "Red"
    elif blue():
        print("vi azul")
        return "Blue"
    elif black():
        print("vi preto")
        return "Black"
    # elif green():
    #     return "Green"
    elif brown():
        print("vi marrom")
        return "Brown"
    elif yellow():
        print("vi amarelo")
        return "Yellow"
    else:
        print("vi branco")
        return "White"


def size():
    if sensor_sup().reflection() <= 50:
        return "10"
    else:
        return "15"



def check():
    color = see()
    return color + " " + size()