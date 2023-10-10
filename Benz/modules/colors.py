from pybricks.parameters import Color
from pybricks.parameters import Port
from pybricks.ev3devices import ColorSensor
from pybricks.tools import StopWatch
from pybricks.nxtdevices import ColorSensor as ColorNxt

sensor_color = ColorSensor(Port.S2)
sensor_sup = ColorNxt(Port.S3)


def calibration(sensor):
    print(sensor.rgb())

# Declaration of RGB values of color sensors
# min and max


def calibration_auto(array):
    global teste
    colors = sensor_color.rgb()
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
red = [[23, 0, 0], [39, 12, 10]] #check

blue = [[1, 31, 58], [17, 47, 74]]  # check

#yellow = [[35, 64, 11], [55, 82, 30]]  

green = [[0, 45, 22], [16, 61, 38]]  # check

brown = [[0, 0, 0], [14, 16, 10]]
#rgb[15.6, 7.6, 5.8]

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

def test(color):
    rgb = sensor_color.rgb()
    print("r  ",(color[0][0] <= rgb[0] and rgb[0]  <= color[1][0]),"    ", rgb[0])
    print("g  ", (color[0][1] <= rgb[1] and rgb[1] <= color[1][1]), "    ", rgb[1])
    print("b  ", (color[0][2] <= rgb[2] and rgb[2] <= color[1][2]), "    ", rgb[2])



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
    for i in range(20):
        cor = sensor_sup.rgb()
        if  cor[0] >= 10 or cor[1] >= 10 or cor[2] >= 10:
            return "15"
    return "10"

def test(sensor, color):
    rgb = sensor.rgb()
    print("r  ",(color[0][0] <= rgb[0] and rgb[0]  <= color[1][0]),"    ", rgb[0])
    print("g  ", (color[0][1] <= rgb[1] and rgb[1] <= color[1][1]), "    ", rgb[1])
    print("b  ", (color[0][2] <= rgb[2] and rgb[2] <= color[1][2]), "    ", rgb[2])
    print("#####################################################################")
    wait(2000)

def check():
    color = see()
    time = StopWatch()
    time.pause()
    time.reset()
    while time.time() <= 5000:
        time.resume()
        if color == "White":
            color = see()
        else:
            break
    tamanho = size()
    if tamanho == "10":
        tamanho = size()
    return color + " " + tamanho
def verify():
    rgb = sensor_sup.rgb()
    if rgb[0] >= 5 or rgb[1] >= 5 or rgb[2] >= 5:
        return "TRUE" #Para quando existe um tubo
    else:
        return "FALSE" #Para qunaod ele nn pegou nada
        