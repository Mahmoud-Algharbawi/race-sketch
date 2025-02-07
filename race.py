

import turtle as t
import random



#create the screen object and define the window size and window color
screen = t.Screen()
screen.setup(width = 500, height = 400)
screen.bgcolor("black") 

is_race_on = False
# Get the user input and store their bet to user for later
user_bet = screen.textinput(title = "Make your bets!", prompt = "Which turtle will win the race?! \nEnter a color from:\nred, orange, yellow, green, blue, purple").lower()


# define the turtle colors, and the y indices
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_indexes = [120, 80, 40, 0, -40, -80]
turtle_list = []
#create turtle objects and append them to the list
for i in range(0,6):
    new_turtle = t.Turtle(shape = "turtle")
    new_turtle.color(colors[i])
    new_turtle.pu()
    new_turtle.goto(x = -230,y = y_indexes[i])
    turtle_list.append(new_turtle)

#check if the user entered their bet, and only start the race when the user has entered their bet
if user_bet:
    is_race_on = True


# start the race 
while is_race_on:
    
    # move each turtle randomly by 10 stepd if it hasn't reached the finishing line
    for turtle in turtle_list:
        
        #if a turtle won, print to the command line the winning turtle color and inform the user if they lost or won
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            is_race_on = False
            
            if winning_turtle == user_bet:
                print(f"You won! The {winning_turtle} turtle won.")
                
            else:
                print(f"You lost! The {winning_turtle} turtle won.")
                
        #choose a random distance and move the turtle forward        
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
    
    
    


screen.exitonclick()