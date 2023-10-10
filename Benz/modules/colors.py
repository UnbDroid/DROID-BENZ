from pybricks.parameters import  Color, Port
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
red_left = [[62, 8, 5], [78, 24, 21]]
red_right = [[37, 5, 5], [53, 21, 21]]#ok

blue_left = [[7, 14, 24], [23, 30, 40]]
blue_right = [[0, 10, 34], [16, 26, 50]]#ok

yellow_left = [[50, 71, 4], [66, 87, 20]]
yellow_right = [[37, 60, 8], [53, 76, 24]]#ok

yell_i_black_left = [[63, 77, 11], [79, 93, 27]]
yell_i_black_right = [[63, 77, 11], [79, 93, 27]]

black_left = [[0,0, 0],[20, 21, 18]]
black_right = [[0,0,0],[7, 24, 21]] #ok


white_left = [[63, 81, 63], [79, 97, 79]]
white_right = [[45, 71, 92], [61, 87, 108]]

blue_i_white_left = [[18, 37, 36], [28, 47, 46]]
blue_i_white_right = [[8, 26, 63], [18, 36, 73]]


green_left = [[2, 25, 5], [18, 41, 21]]
green_right = [[0, 22, 7], [14, 38, 23]] 

brown_left = [[14, 8, 2], [30, 24, 18]]
brown_right = [[7, 6, 6], [23, 22, 22]]

def inside():
    return and_saw_blue() or and_saw_brown() or and_saw_green() or and_saw_red()

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

def greenLeft() :
    rgb = sensor_color_left.rgb()
    return ( (green_left[0][0] <= rgb[0] and rgb[0] <=green_left[1][0]) and (green_left[0][1] <= rgb[1] and rgb[1] <=green_left[1][1]) and (green_left[0][2] <= rgb[2] and rgb[2] <=green_left[1][2]) )



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

def greenRight():
    rgb = sensor_color_right.rgb()
    return ( (green_right[0][0] <= rgb[0] and rgb[0] <=green_right[1][0]) and (green_right[0][1] <= rgb[1] and rgb[1] <=green_right[1][1]) and (green_right[0][2] <= rgb[2] and rgb[2] <=green_right[1][2]) )


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

def saw_wall():
    return (blackRight() and blackLeft()) or (yellowRight() and yellowLeft()) or (blackRight() and yellowLeft()) or (yellowRight() and blackLeft())

def saw_red():
    return redRight() or redLeft()

def saw_black():
    return blackRight() or blackLeft()

def saw_yellow():
    return yellowRight() or yellowLeft()
    
def saw_blue():
    return blueRight() or blueLeft()

def saw_blue_white():
    return blue_i_white_l() or blue_i_white_r()

def and_saw_red():
    return redRight() and redLeft()

def and_saw_blue():
    return blueRight() and blueLeft()

def and_saw_green():
    return greenRight() and greenLeft()

def and_saw_brown():
    return brownRight() and brownLeft()


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
        # print("vi ama)
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
    wait(2000)

def percentagem(rgb, color_max): # porcentagem do maior valor
	aux = [(color_max[0]/rgb[0]), (color_max[1]/rgb[1]), (color_max[2]/rgb[2])]
	aux = ((aux[0] + aux [1] + aux[2])*100)//3
	return aux

def proportion(color_max, color_max_sup):
    return [(color_max_sup[0]/color_max[0]), (color_max_sup[1]/color_max[1]), (color_max_sup[2]/color_max[2])]
