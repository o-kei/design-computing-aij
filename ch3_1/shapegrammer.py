import turtle

scale = 1.0
level = 1


def Urform(i, sign):
    turtle.pendown()
    turtle.forward(900.0 * scale / (3 ** i))
    turtle.left(90 * sign)
    turtle.forward(900.0 * scale / (3 ** i))
    turtle.penup()
    turtle.left(90 * sign)
    turtle.forward(900.0 * scale / (3 ** i))
    turtle.left(90 * sign)
    turtle.forward(180.0 * scale / (3 ** i))
    turtle.left(90 * sign)
    turtle.pendown()
    turtle.forward(180.0 * scale / (3 ** i))
    turtle.left(90 * sign)
    turtle.forward(180.0 * scale / (3 ** i))
    turtle.penup()


def Rule1(i, sign):
    start = turtle.position()
    Urform(i, sign)
    stop = turtle.position()
    if i < level:
        turtle.goto(start)
        turtle.forward(480.0 * scale / (3 ** i))
        turtle.right(90 * sign)
        Rule2(i + 1, -sign)
        turtle.goto(stop)
    else:
        Rule3()


def Rule2(i, sign):
    Rule1(i, sign)
    Rule1(i, -sign)
    turtle.left(90 * sign)
    turtle.forward(720.0 * scale / (3 ** i))
    turtle.right(90 * sign)
    Rule1(i, -sign)
    Rule1(i, sign)
    Rule1(i, -sign)
    turtle.left(90 * sign)
    turtle.forward(720.0 * scale / (3 ** i))
    turtle.right(90 * sign)
    Rule1(i, -sign)
    Rule1(i, sign)


def Rule3():
    return


def I(n):
    global level
    level = n
    turtle.speed('fastest')
    turtle.penup()
    turtle.goto(60.0 * scale, 180.0 * scale)
    turtle.pendown()
    turtle.forward(240.0 * scale)
    turtle.right(90)
    Rule1(1, -1)
    Rule1(1, 1)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(240.0 * scale)
    turtle.hideturtle()
    turtle.done()

I(3)
