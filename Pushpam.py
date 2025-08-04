import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("#7C909C")
t.speed(100)
cols = ('#ED7864','#6E544F','#592F2F','#6E382E')

for p in range(5):
    for n in range(9):
        t.speed(n+10)
        for i in range(2):
            t.pensize(3)
            t.circle(80+p*20,90)
            t.lt(90)
        t.lt(45)
    t.pencolor(cols[p%4])
s.exitonclick()