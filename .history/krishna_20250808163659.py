import turtle
"""
This program uses the turtle graphics library to draw a stylized depiction of Lord Krishna with a decorative background and text.
Functions:
    background(tur): Draws a filled rectangular background using the provided turtle object.
    back_circle(tur): Draws a large blue circle as part of the artwork using the provided turtle object.
    krishna_shape(tur): Draws the main Krishna figure using a series of turtle movements and fills.
    text(tur): Writes the text "Radhe Krishna...." on the canvas using the provided turtle object.
    main(): Sets up the turtle screen, initializes the turtle, and calls the drawing functions in sequence.
The drawing consists of a red background, a blue circle, a stylized Krishna figure, and a greeting text.
"""


def background(tur):
    tur.speed(0)
    tur.fillcolor("#f20707")
    tur.begin_fill()
    tur.forward(400)
    tur.right(90)
    tur.forward(100)
    tur.right(90)
    tur.forward(800)
    tur.right(90)
    tur.forward(100)
    tur.right(90)
    tur.forward(400)
    tur.end_fill()
    tur.forward(160)

def back_circle(tur):
    tur.speed(0)
    tur.left(40)
    tur.fillcolor("#ffff00")
    tur.begin_fill()
    tur.circle(250, 280)
    tur.left(40)
    tur.forward(160)
    tur.end_fill()

def krishna_shape(tur):
    tur.fillcolor("#041E4B")
    tur.speed(0)
    tur.hideturtle()
    tur.begin_fill()
    tur.forward(160);tur.left(130);tur.circle(-300, 30);tur.forward(95);tur.circle(50, 40);tur.right(40);tur.forward(43);tur.circle(80, 25)
    tur.circle(50, 30);tur.left(10);tur.circle(35, 28);tur.right(160);tur.circle(10, 100);tur.right(100);tur.circle(10, 80);tur.forward(20)
    tur.left(80);tur.circle(100, 15);tur.right(90);tur.forward(6);tur.left(65);tur.circle(60, 55);tur.right(160);tur.circle(20, 100);tur.forward(10)
    tur.circle(-20, 25);tur.left(170);tur.circle(-20, 40);tur.forward(10);tur.circle(20, 80);tur.right(135);tur.circle(60, 15);tur.left(70);tur.forward(6)
    tur.right(110);tur.forward(9);tur.left(80);tur.circle(70, 24);tur.right(60);tur.circle(65, 30);tur.circle(-5, 110);tur.circle(5, 120);tur.right(90)
    tur.circle(5, 60);tur.forward(10);tur.circle(10, 5);tur.right(80);tur.forward(15);tur.circle(-5, 160);tur.forward(6);tur.circle(2, 180);tur.forward(6)
    tur.circle(20, 30);tur.right(140);tur.circle(3, 150);tur.right(110);tur.circle(4, 80);tur.forward(2);tur.right(100);tur.forward(6);tur.right(60)
    tur.forward(9);tur.circle(2, 180);tur.forward(10);tur.left(30);tur.forward(15);tur.right(85);tur.forward(40);tur.right(60);tur.circle(5, 310);tur.right(80)
    tur.forward(3);tur.right(90);tur.forward(42);tur.right(30);tur.forward(10);tur.left(90);tur.circle(20, 60);tur.left(95);tur.forward(12)
    tur.right(29);tur.forward(42);tur.right(90);tur.forward(34);tur.right(85);tur.forward(2);tur.circle(60, 25);tur.right(80);tur.circle(10, 40);tur.forward(45)
    tur.left(10);tur.forward(130);tur.left(90);tur.forward(20);tur.right(90);tur.forward(10);tur.left(90);tur.forward(10);tur.right(90)
    tur.forward(5);tur.left(90);tur.forward(25);tur.left(100);tur.forward(120);tur.right(175);tur.circle(50, 50);tur.right(80);tur.circle(110, 15);tur.forward(75);tur.left(97);tur.forward(360)
    tur.end_fill()

def text(tur):
    tur.pu()
    tur.hideturtle()
    tur.right(90)
    tur.forward(90)
    tur.right(90)
    tur.forward(420)
    tur.color("#ffffff")
    tur.write("Radhe Krishna....", font=("Georgia", 40, "bold"))

def main():
    turtle.bgcolor("#000000")
    turtle.title("Radhe Krishna")
    screen = turtle.Screen()
    screen.setup(650, 580)

    tur = turtle.Turtle()
    tur.right(90)
    tur.penup()
    tur.forward(180)
    tur.left(90)
    tur.pendown()


    background(tur)
    back_circle(tur)
    krishna_shape(tur)
    text(tur)

    turtle.done()

main()
