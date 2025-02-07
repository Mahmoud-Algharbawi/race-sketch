
#import the modules needed
import turtle as t


# Create a new turtle object and a new screen object
tim = t.Turtle()
screen = t.Screen()

screen.colormode(255)
screen.bgcolor("black")
tim.color("white")




# functions to control the turtle.
def move_forward():
    tim.fd(10)
    
def move_backward():
    tim.bk(10)

def turn_counter():
    tim.lt(10)
    
def turn_clock():
    tim.rt(10)
    
def reset_canvas():
    tim.home()
    tim.clear()

    # screen.colormode(255)
    # screen.bgcolor("black")
    # tim.color("white")


# commands for moving in different directions
# These use the following keys:
#       up -> move forward
#       down -> move backward
#       left -> move counterclockwise by 10 degrees
#       right -> move clockwise by 10 degrees
screen.onkey(key = "Up", fun = move_forward)
screen.onkey(key = "Down", fun = move_backward)
screen.onkey(key = "Left", fun = turn_counter)
screen.onkey(key = "Right", fun = turn_clock)
screen.onkey(key = "c", fun = reset_canvas)


screen.listen()
















screen.exitonclick()