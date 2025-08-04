import turtle
from turtle import *
hideturtle()
screensize(90,100)
Screen().bgcolor("#fa7e1e")
pensize(7)
circle(50)
up()
goto(1,19)
down()
circle(32)
pencolor("black")

up()
goto(-50,-25)
down()

for i in range(4):
     forward(100)
     circle(25,90)

up()
goto(-53,-24)
down()

for i in range(4):
     forward(100)
     circle(25,90)

up()
goto(55,95)
down()
circle(2,360)

done()

