from pybricks.parameters import  Color
from pybricks.parameters import Port
from pybricks.ev3devices import ColorSensor

sensor_color_left = ColorSensor(Port.S2) 
sensor_color_right = ColorSensor(Port.S1) 

global array
global teste

def calibration(sensor):
    print(sensor.rgb())

def treshold(color1, color2):
    R = abs(color1[0]-color2[0])
    G = abs(color1[1]-color2[1])
    B = abs(color1[2]+color2[2])
    aux = [R, G , B]
    index = aux.index(max(aux))
    if index == 0:
        return "R"
    elif index == 1:
        return "G"
    else:
        return "B"

def calibration_auto2(sensor, array):
  #  global array
   # global teste
    colors = sensor.rgb()
    #min
    print("Calibrando as cores")
    array[0][0] = colors[0]-8
    array[0][1] = colors[1]-8
    array[0][2] = colors[2]-8
    #max
    array[1][0] = colors[0]+8
    array[1][1] = colors[1]+8
    array[1][2] = colors[2]+8
    print("Devolvendo os valores")
    print(array)

def calibration_auto(sensor, array):

    colors = sensor.rgb()
    #min
    print("Calibrando as cores")
    
    array[0][0] = colors[0]-8
    array[0][1] = colors[1]-8
    array[0][2] = colors[2]-8
    #max
    array[1][0] = colors[0]+8
    array[1][1] = colors[1]+8
    array[1][2] = colors[2]+8
    print("Devolvendo os valores")
    print(array)

#Declaration of RGB values of color sensors
#min and max
teste = [[0,0,0],[0,0,0]]
#arrumar o marrom e verde
red_left = [[63, 10, 2], [79, 26, 18]]
red_right = [[42, 2, 3], [58, 18, 19]]#ok

blue_left = [[0,18,34],[23,38,54]]
blue_right = [[0,18,52],[18,38,74]]#ok

yellow_left = [[60, 77, 11], [76, 93, 28]]
yellow_right = [[42, 65, 12], [58, 81, 28]]#ok

yell_i_black_left = [[63, 77, 11], [79, 93, 27]]
yell_i_black_right = [[63, 77, 11], [79, 93, 27]]

green_left = [[14,35,0],[24,55,20]]
green_right = [[5,32,0],[20,45,20]] #ok

black_left = [[0,0, 0],[8, 16, 8]]
black_right = [[0,0,0],[7, 15, 9]] #ok

brown_left = [[20,10,0],[35,30,18]]
brown_right = [[24,9,0],[45,32,15]] 

white_left = [[67, 88, 73], [83, 104, 89]]
white_right = [[48, 80, 92], [64, 96, 108]]

blue_i_white_left = [[18, 37, 36], [28, 47, 46]]
blue_i_white_right = [[8, 26, 63], [18, 36, 73]]



#left
def blue_i_white_l():
    rgb = sensor_color_left.rgb()
    return ((blue_i_white_left[0][0] <= rgb[0] and rgb[0] <= blue_i_white_left[1][0]) and (blue_i_white_left[0][1] <= rgb[1] and rgb[1] <= blue_i_white_left[1][1]) and (blue_i_white_left[0][2] <= rgb[2] and rgb[2] <= blue_i_white_left[1][2]))

def yellow_i_black_left():
    rgb = sensor_color_left.rgb()
    return ((yell_i_black_left[0][0] <= rgb[0] and rgb[0] <= yell_i_black_left[1][0]) and (yell_i_black_left[0][1] <= rgb[1] and rgb[1] <= yell_i_black_left[1][1]) and (yell_i_black_left[0][2] <= rgb[2] and rgb[2] <= yell_i_black_left[1][2]))
 
def whiteLeft():
    rgb = sensor_color_left.rgb()
    return ( (white_left[0][0] <= rgb[0] and rgb[0] <=white_left[1][0]) and (white_left[0][1] <= rgb[1] and rgb[1] <=white_left[1][1]) and (white_left[0][2] <= rgb[2] and rgb[2] <=white_left[1][2]) )


def redLeft() :
    rgb = sensor_color_left.rgb()
    return ( (red_left[0][0] <= rgb[0] and rgb[0] <=red_left[1][0]) and (red_left[0][1] <= rgb[1] and rgb[1] <=red_left[1][1]) and (red_left[0][2] <= rgb[2] and rgb[2] <=red_left[1][2]) )

def blackLeft() :
    rgb = sensor_color_left.rgb()
    return ( (black_left[0][0] <= rgb[0] and rgb[0] <=black_left[1][0]) and (black_left[0][1] <= rgb[1] and rgb[1] <=black_left[1][1]) and (black_left[0][2] <= rgb[2] and rgb[2] <=black_left[1][2]) )

def blueLeft() :
    rgb = sensor_color_left.rgb()
    return ( (blue_left[0][0] <= rgb[0] and rgb[0] <=blue_left[1][0]) and (blue_left[0][1] <= rgb[1] and rgb[1] <=blue_left[1][1]) and (blue_left[0][2] <= rgb[2] and rgb[2] <=blue_left[1][2]) )

def yellowLeft() :
    rgb = sensor_color_left.rgb()
    return ( (yellow_left[0][0] <= rgb[0] and rgb[0] <=yellow_left[1][0]) and (yellow_left[0][1] <= rgb[1] and rgb[1] <=yellow_left[1][1]) and (yellow_left[0][2] <= rgb[2] and rgb[2] <=yellow_left[1][2]) )

def brownLeft() :
    rgb = sensor_color_right.rgb()
    return ( (brown_left[0][0] <= rgb[0] and rgb[0] <=brown_left[1][0]) and (brown_left[0][1] <= rgb[1] and rgb[1] <=brown_left[1][1]) and (brown_left[0][2] <= rgb[2] and rgb[2] <=brown_left[1][2]) )

#right

def blue_i_white_r():
    rgb = sensor_color_right.rgb()
    return ((blue_i_white_right[0][0] <= rgb[0] and rgb[0] <= blue_i_white_right[1][0]) and (blue_i_white_right[0][1] <= rgb[1] and rgb[1] <= blue_i_white_right[1][1]) and (blue_i_white_right[0][2] <= rgb[2] and rgb[2] <= blue_i_white_right[1][2]))

def yellow_i_black_right():
    rgb = sensor_color_right.rgb()
    return ((yell_i_black_right[0][0] <= rgb[0] and rgb[0] <= yell_i_black_right[1][0]) and (yell_i_black_right[0][1] <= rgb[1] and rgb[1] <= yell_i_black_right[1][1]) and (yell_i_black_right[0][2] <= rgb[2] and rgb[2] <= yell_i_black_right[1][2]))

def whiteRight():
    rgb = sensor_color_left.rgb()
    return ( (white_left[0][0] <= rgb[0] and rgb[0] <=white_left[1][0]) and (white_left[0][1] <= rgb[1] and rgb[1] <=white_left[1][1]) and (white_left[0][2] <= rgb[2] and rgb[2] <=white_left[1][2]) )

def redRight() :
    rgb = sensor_color_right.rgb()
    return ( (red_right[0][0] <= rgb[0] and rgb[0] <=red_right[1][0]) and (red_right[0][1] <= rgb[1] and rgb[1] <=red_right[1][1]) and (red_right[0][2] <= rgb[2] and rgb[2] <=red_right[1][2]) )

def blackRight() :
    rgb = sensor_color_right.rgb()
    return ( (black_right[0][0] <= rgb[0] and rgb[0] <=black_right[1][0]) and (black_right[0][1] <= rgb[1] and rgb[1] <=black_right[1][1]) and (black_right[0][2] <= rgb[2] and rgb[2] <=black_right[1][2]) )

def blueRight() :
    rgb = sensor_color_right.rgb()
    return ( (blue_right[0][0] <= rgb[0] and rgb[0] <=blue_right[1][0]) and (blue_right[0][1] <= rgb[1] and rgb[1] <=blue_right[1][1]) and (blue_right[0][2] <= rgb[2] and rgb[2] <=blue_right[1][2]) )

def yellowRight() :
    rgb = sensor_color_right.rgb()
    return ( (yellow_right[0][0] <= rgb[0] and rgb[0] <=yellow_right[1][0]) and (yellow_right[0][1] <= rgb[1] and rgb[1] <=yellow_right[1][1]) and (yellow_right[0][2] <= rgb[2] and rgb[2] <=yellow_right[1][2]) )

def brownRight() :
    rgb = sensor_color_right.rgb()
    return ( (brown_right[0][0] <= rgb[0] and rgb[0] <=brown_right[1][0]) and (brown_right[0][1] <= rgb[1] and rgb[1] <=brown_right[1][1]) and (brown_right[0][2] <= rgb[2] and rgb[2] <=brown_right[1][2]) )


#Declaration of detected colors

def saw_red():
    return redRight() and redLeft()

def saw_black():
    return blackRight() or blackLeft()

def saw_yellow():
    return yellowRight() or yellowLeft()
    
def saw_blue():
    return blueRight() or blueLeft()

def saw_blue_white():
    return blue_i_white_l() or blue_i_white_r()

#def saw_brown():
 #   return brownRight() or brownLeft()
    
def saw_white():
    return whiteRight() or whiteLeft()
def saw_yellow_black():
    return yellow_i_black_right() or yellow_i_black_left()
def seeRight():
    if redRight():
        return "Red"
    elif blueRight():
        return "Blue"
    elif blackRight():
        print("vi preto")
        return "Black"
    # elif greenRight():
    #     return "Green"
   # elif brownRight():
    #    return "Brown"
    elif yellowRight():
        print("vi amarelo")
        return "Yellow"
    elif saw_blue_white():
        return "Blue_White"
    else:
      #  print("vi branco")
        return "White"

def seeLeft():
    if redLeft():
        # print("vi vermelho")
        return "Red"
    elif blueLeft():
        # print("vi azul")
        return "Blue"
    elif blackLeft():
        # print("vi preto")
        return "Black"
    # elif greenLeft():
    #     return "Green"
    elif brownLeft():
        # print("vi marrom")
        return "Brown"
    elif yellowLeft():
        # print("vi amarelo")
        return "Yellow"
    else:
    #    print("vi branco")
        return "White"


def test(sensor, color):
    rgb = sensor.rgb()
    print("r  ",(color[0][0] <= rgb[0] and rgb[0]  <= color[1][0]),"    ", rgb[0])
    print("g  ", (color[0][1] <= rgb[1] and rgb[1] <= color[1][1]), "    ", rgb[1])
    print("b  ", (color[0][2] <= rgb[2] and rgb[2] <= color[1][2]), "    ", rgb[2])
    print("#####################################################################")

def percentagem(rgb, color_max): # porcentagem do maior valor
	aux = [(color_max[0]/rgb[0]), (color_max[1]/rgb[1]), (color_max[2]/rgb[2])]
	aux = ((aux[0] + aux [1] + aux[2])*100)//3
	return aux

def proportion(color_max, color_max_sup):
    return [(color_max_sup[0]/color_max[0]), (color_max_sup[1]/color_max[1]), (color_max_sup[2]/color_max[2])]
