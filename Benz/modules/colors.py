from pybricks.parameters import  Color
from pybricks.parameters import Port
from pybricks.ev3devices import ColorSensor


sensor_color_left = ColorSensor(Port.S1) 
sensor_color_right = ColorSensor(Port.S2) 

def calibration(sensor):
    print(sensor.rgb())

#Declaration of RGB values of color sensors
#min and max

#arrumar o marrom e verde
red_left = [[30,5,0],[49,25,20]]
red_right = [[54,5,0],[77,25,20]]#check

blue_left = [[0,15,43],[17,34,65]]
blue_right = [[6,18,32],[23,35,53]]#check

yellow_left = [[35,64, 11],[55,82,30]]
yellow_right = [[58,78,13],[78,92,30]] #check

green_left = [[30,5,0],[49,25,20]]
green_right = [[54,5,0],[77,25,20]]

black_left = [[2,5,0],[15,15,10]]
black_right = [[5,5,0],[16,22,10]] #check

brown_left = [[20,10,0],[35,30,18]]
brown_right = [[24,9,0],[45,32,15]] #check


#left 

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

def saw_brown():
    return brownRight() or brownLeft()

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
    elif brownRight():
        return "Brown"
    elif yellowRight():
        print("vi amarelo")
        return "Yellow"
    else:
        print("vi branco")
        return "White"

def seeLeft():
    if redLeft():
        print("vi vermelho")
        return "Red"
    elif blueLeft():
        print("vi azul")
        return "Blue"
    elif blackLeft():
        print("vi preto")
        return "Black"
    # elif greenLeft():
    #     return "Green"
    elif brownLeft():
        print("vi marrom")
        return "Brown"
    elif yellowLeft():
        print("vi amarelo")
        return "Yellow"
    else:
        print("vi branco")
        return "White"
