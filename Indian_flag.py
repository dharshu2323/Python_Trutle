import turtle
t=turtle.Turtle()
windows=turtle.Screen()
windows.title("Independence Day")
screen = turtle.Screen()
screen.setup(width=700, height=600) 


t.penup()
t.goto(-180,250)
t.pendown()
t.pensize(0)
#orange
t.color("orange")
t.begin_fill()
t.forward(350)
t.right(90)
t.forward(50)
t.right(90)
t.forward(350)
t.end_fill()

t.penup()
t.left(90)
t.forward(80)
t.pendown()
#green rectangle
t.color("green")
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(350)
t.left(90)
t.forward(50)
t.end_fill()
#Ashoka symbol

t.penup()
t.color("navy")
t.width(2)
t.goto(10,160)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()
t.goto(0,160)
t.pendown()
t.pensize(2)
for i in range(24):
    t.forward(40)
    t.backward(40)
    t.left(15)
    t.circle(0,0)
t.penup()
t.left(150)
t.forward(250)
t.right(-50)
t.pendown()
t.color("orange")
style=("Fantasy",50,"normal")
t.write("HAPPY",font=style,align='left',move=False)
t.hideturtle()
t.penup()
t.forward(100)
t.left(90)
t.right(180)
t.pendown()
t.color("navy")
t.write("          INDEPENDENCE",font=style,align='center',move=False)
t.penup()
t.forward(250)
t.left(35)
t.right(180)
t.pendown()
t.color("green")
t.write("             DAY",font=style,move=False)
t.hideturtle()


t.hideturtle()




turtle.done()