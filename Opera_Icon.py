import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
opera_icon = turtle.Turtle()
opera_icon.speed(3)

# Function to draw the Opera logo
def draw_opera_logo():
    # Draw the outer red part of the logo
    opera_icon.fillcolor("red")
    opera_icon.begin_fill()
    opera_icon.circle(100, 180)  # Draw half circle
    opera_icon.left(90)
    opera_icon.forward(200)  # Draw vertical line
    opera_icon.left(90)
    opera_icon.circle(100, 180)  # Draw other half circle
    opera_icon.left(90)
    opera_icon.forward(200)  # Complete vertical line
    opera_icon.end_fill()

    # Draw the white inner part of the logo
    opera_icon.penup()
    opera_icon.goto(-40, 0)
    opera_icon.pendown()
    opera_icon.fillcolor("white")
    opera_icon.begin_fill()
    opera_icon.circle(40)  # Draw inner circle
    opera_icon.end_fill()

# Move to starting position for drawing
opera_icon.penup()
opera_icon.goto(0, -100)
opera_icon.pendown()

# Draw the Opera logo
draw_opera_logo()

# Hide the turtle and finish
opera_icon.hideturtle()
turtle.done()