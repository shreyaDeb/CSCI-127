# Our aim for this Program was:

# The functionality to detect a click in the third segment is present and working correctly.
# Yellow is present as a possible color for a section of flag, and the color cycling functionality works correctly.
# The six countries represented by specific flags designs are identified correctly in the messaging:
    # FRANCE: Blue, White, Red
    # ITALY: Green, White, Red
    # PERU: Red, White, Red
    # NIGERIA: Green, White, Green
    # ROMANIA: Blue, Yellow, Red
    # MALI: Green, Yellow, Red
# Flag designs not representative of the six countries above are displayed with messaging that reads, "That design is available."
# The onscreen messaging about the flag design is always clear and legible, correct, and font is consistently 20 pixel Arial. (You don't
    # have to change the font size of the initial messaging that says, "Click anywhere to begin designing a flag.") In order to erase the
    # current message before writing the new one, it will be necessary to complete the erase_message() function.
# The Python solution is easy to understand and does not contain unnecessary code. You may remove the #TODO tags once they are complete, and add
    # comments of your own to help explain what your code is doing. (2 points for each type of improvement up to 10 points).
                                                                                        
import turtle

#Sets up color indicator
width = 800 
height = 500
turtle.setup(width, height)
wn = turtle.Screen()
wn.bgcolor("lightgray")


#Draws outline of flag
draw_color = "gray"
color_1, color_2, color_3 = draw_color, draw_color, draw_color
section = turtle.Turtle()
section.color(draw_color, "lightgray")
section.shapesize(2)
section.speed(0)
section.penup()


#Displays chosen message
message = turtle.Turtle()
message.hideturtle()
message.penup()
message.goto(-150, -150) #Changed x to 150 so text would be aligned with left edge of flag
message.color("gray")
message.speed(0)
message.write("Click anywhere to begin designing a flag.", font = ("Arial", 12))


#Defines a section
def draw_section():
    section.begin_fill()
    section.pendown()
    for i in range(2):
        section.forward(100)
        section.right(90)
        section.forward(200)
        section.right(90)
    section.end_fill()
    section.penup()
    section.goto(-250, 0)
        
#Draws respective section
def draw_first(): 
    section.goto(-150,100)
    draw_section()

def draw_second():
    section.goto(-50,100)
    draw_section()

def draw_third():
    section.goto(50,100)
    draw_section()
    


#Tells the color indicator to change its color
def cycle_color(current_color):
    if current_color == "green" or current_color == "gray" :
        new_color = "white"
    elif current_color == "white":
        new_color = "blue"
    elif current_color == "blue":
        new_color = "red"
    elif current_color == "red":
        new_color = "yellow"
    elif current_color == "yellow":
        new_color = "green"
    else:
        print("There seems to be a mistake with the color cycling.")
        new_color = "gray"
        
    return new_color


#Changes section color based on location of user click
def color_flag(x, y):

    global draw_color, color_1, color_2, color_3
    print("x: ", x, "y: ", y)

    if (-150 < x < -50) and (100 > y > -100):
        draw_first()
        color_1 = draw_color
    elif (-50 < x < 50) and (100 > y > -100):
        draw_second()
        color_2 = draw_color
    elif (50 < x < 150) and (100 > y > -100):
        draw_third()
        color_3 = draw_color
    else:
        draw_color = cycle_color(draw_color) 
        section.color(draw_color)
        
    check_flag(color_1, color_2, color_3)
    
    
#Clears previous message
def erase_message():
    message.fillcolor("lightgray")
    message.begin_fill()
    message.goto(-300, -120)
    message.goto(300, -120)
    message.goto(300, -160)
    message.goto(-300, -160)
    message.goto(-300, -120)
    message.end_fill()
    message.goto(-150, -150) #Changed x to 150 so text would be aligned with left edge of flag

    
#Recognizes if chosen flag belongs to a specified existing country or not
def check_flag(one, two, three):

    print("left: " + one + ", center: " + two + ", right: " + three)
    erase_message()

    if (one == 'blue' and two == 'white' and three == 'red'):
        message.write("National Flag of France.", font = ("Arial", 20))
        
    elif (one == 'green' and two == 'white' and three =='red'): 
        message.write("National Flag of Italy.", font = ("Arial", 20))
        
    elif (one == 'red' and two == 'white' and three =='red'): 
        message.write("National Flag of Peru.", font = ("Arial", 20))
        
    elif (one == 'green' and two == 'white' and three == 'green'): 
        message.write("National Flag of Nigeria.", font = ("Arial", 20))
        
    elif (one == 'blue' and two == 'yellow' and three == 'red'): 
        message.write("National Flag of Romania.", font = ("Arial", 20))
        
    elif (one == 'green' and two == 'yellow' and three == 'red'): 
        message.write("National Flag of Mali.", font = ("Arial", 20))

    elif (one == "gray" or two == "gray" or three == "gray"):
        message.write("Color all three sections.", font = ("Arial", 20))
    else:
        message.write("That design is available.", font = ('Arial', 20))
        
draw_first()
draw_second()
draw_third()

wn.onclick(color_flag)
      

    
    
