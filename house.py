import turtle

#mặt trời vàng
turtle.setup(1000, 1000)
turtle.bgcolor("light blue")

turtle.penup()
turtle.goto(150,200)
turtle.pendown()
turtle.pensize(5)
turtle.pencolor("orange")
turtle.fillcolor ("yellow")
turtle.begin_fill()

turtle.circle (50)
turtle.end_fill()

# tia mặt trời
for i in range (8):
    turtle.right(90)
    turtle.forward(50)
    turtle.backward(50)
    turtle.left(90)
    turtle.circle(50,45)

# vẽ nhà
turtle.penup()
turtle.goto(-100,-350)
turtle.pendown()
turtle.pensize(2)
turtle.pencolor("black")
    # vẽ mặt trc
turtle.fillcolor("blue")
turtle.begin_fill()

for i in range (2):
    turtle.left(90)
    turtle.forward(250)
    turtle.left(90)
    turtle.forward(200)
turtle.end_fill()
    # vẽ cửa
turtle.backward(50)
turtle.fillcolor("light green")
turtle.begin_fill()

for i in range (2):
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(100)

turtle.end_fill()
    #vẽ mặt bên
turtle.forward(50)

turtle.fillcolor("yellow")
turtle.begin_fill()

turtle.left(45)
turtle.forward(100)
turtle.left(45)
turtle.forward(250)
turtle.left(135)
turtle.forward(100)
turtle.end_fill()
    #vẽ mái (mặt trc)
turtle.fillcolor("pink")
turtle.begin_fill()

turtle.right(105)
turtle.forward(200)
turtle.left(120)
turtle.forward(200)

turtle.end_fill()

turtle.backward(200)
    # vẽ mái mặt bên
turtle.fillcolor("orange")
turtle.begin_fill()
turtle.left(165)
turtle.forward(100)
turtle.right(105)
turtle.forward(200)
turtle.right(75)
turtle.forward(100)

turtle.end_fill()

# vẽ cây
turtle.penup()
turtle.goto(200,-20)
turtle.pendown()

turtle.fillcolor("light green")
turtle.begin_fill()
turtle.left(195)
turtle.forward(100)

for i in range (2):
    turtle.right(120)
    turtle.forward(100)
turtle.backward(50)

turtle.end_fill()

turtle.fillcolor("light green")
turtle.begin_fill()

turtle.left(60)
turtle.forward(100)

for i in range(3):
    turtle.left(120)
    turtle.forward(100)
turtle.left(120)
turtle.forward(50)

turtle.end_fill()

turtle.fillcolor("light green")
turtle.begin_fill()

turtle.right(120)
turtle.forward(100)
for i in range(3):
    turtle.left(120)
    turtle.forward(100)

turtle.end_fill()

turtle.right(60)
turtle.backward(40)

turtle.fillcolor("brown")
turtle.begin_fill()
for i in range (2):
    turtle.left(90)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(20)
turtle.end_fill()

turtle.done()