import turtle
import random

t = turtle.Turtle()
windows = turtle.Screen()
windows.title("Night_View")
screen = turtle.Screen()
screen.setup(width=700, height=600)
windows.bgcolor("#000")
colors = ['red', 'blue', 'orange', 'yellow', 'magenta', 'purple', 'peru', 'ivory', 'dark orange']
star = turtle.Turtle()
star.speed(0)
star.hideturtle()

text = turtle.Turtle()
text.speed(6)
text.hideturtle()

def draw(pos, color):
    x, y = pos
    t.color(color)
    t.begin_fill()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(50)
    t.end_fill()

def stars(x, y, color, length):
    star.color(color)
    star.penup()
    star.goto(x, y)
    star.pendown()
    star.begin_fill()
    for _ in range(5):
        star.forward(length)
        star.right(144)
        star.forward(length)
    star.end_fill()

def random_pos():
    return random.randint(-390, 390), random.randint(-200, 290)

def random_length():
    return random.randint(5, 10)

def write_text(color):
    text.color(color)
    text.penup()
    text.goto(-180, -270)
    text.pendown()
    style = ('Stencil Std Bold', 50, 'normal')
    text.write('Good Night', font=style, move=True)

# Main program

draw((-300, 170), 'white')
draw((-278, 183), 'black')

num_stars = 0
while num_stars < 25:  # Draw only 25 stars
    color = random.choice(colors)
    x, y = random_pos()
    length = random_length()
    stars(x, y, color, length)
    write_text(color)
    num_stars += 1

turtle.done()
