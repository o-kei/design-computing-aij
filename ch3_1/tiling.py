import turtle

scale = 0.5

def FJtile(n, c):
    center = turtle.position()
    turtle.penup();
    turtle.setheading(0)
    turtle.left(n * 90); turtle.forward(38.0 * scale)
    turtle.left(90); turtle.forward(7.0 * scale)
    turtle.pendown()
    turtle.color("#e8e2cc")
    turtle.begin_fill()
    turtle.forward(31.0 * scale)
    turtle.left(90); turtle.forward(76.0 * scale)
    turtle.left(90); turtle.forward(76.0 * scale)
    turtle.left(90); turtle.forward(31.0 * scale)
    turtle.left(90); turtle.forward(25.0 * scale)
    turtle.right(90); turtle.forward(25.0 * scale)
    turtle.left(90); turtle.forward(12.0 * scale)
    turtle.left(90); turtle.forward(11.0 * scale)
    turtle.right(90); turtle.forward(8.0 * scale)
    turtle.right(90); turtle.forward(31.0 * scale)
    turtle.end_fill()
    if c % 2 == 0:
        turtle.color("#5775b1")
    else:
        turtle.color("#804235")        
    turtle.begin_fill()
    turtle.right(90); turtle.forward(45.0 * scale)
    turtle.right(90); turtle.forward(45.0 * scale)
    turtle.right(90); turtle.forward(25.0 * scale)
    turtle.right(90); turtle.forward(25.0 * scale)
    turtle.left(90); turtle.forward(12.0 * scale)
    turtle.left(90); turtle.forward(11.0 * scale)
    turtle.right(90); turtle.forward(8.0 * scale)
    turtle.right(90); turtle.forward(31.0 * scale)
    turtle.end_fill()
    turtle.penup();
    turtle.setheading(0)
    turtle.goto(center)
    return n


def R(n, i=2, c=0):
    turtle.setheading(0); turtle.forward(80.0 * scale)
    return FJtile((n + i) % 4, c)


def U(n, i=2, c=0):
    turtle.setheading(90); turtle.forward(80.0 * scale)
    return FJtile((n + i) % 4, c)


def L(n, i=2, c=0):
    turtle.setheading(180); turtle.forward(80.0 * scale)
    return FJtile((n + i) % 4, c)


def D(n, i=2, c=0):
    turtle.setheading(270); turtle.forward(80.0 * scale)
    return FJtile((n + i) % 4, c)


def I(n, x, y, c=0):
    turtle.speed('fastest')
    turtle.hideturtle()
    turtle.penup()
    turtle.goto((x * 80.0 + 40.0) * scale, (y * 80.0 + 40.0) * scale)
    return FJtile(n, c)

#--------------


def S(n, i=2, c1=0, c2=0):  # 2 * 5 up pattern, i = swap rotation
    return R(U(L(U(R(U(L(U(R(n))), 2, c1), i, c2)))))


def Z(n, i=2, c1=0, c2=0):  # 2 * 5 down pattern, i = swap rotation
    return R(D(L(D(R(D(L(D(R(n))), 2, c1), i, c2)))))

#--------------


def C(n, d, i=2):     # FJ Tile
    turtle.left((n + d) * 90); turtle.forward(80.0 * scale)
    return FJtile((n + i) % 4, 1)


def V(n):
    turtle.left((n + 1) * 90); turtle.forward(80.0 * scale)
    turtle.setheading(0)
    return n


def E(n):
    return C(V(C(V(C(C(V(C(C(n, 0), 3)), 0, 0), 3)), 2)), 1)

#--------------


def pattern1_1():
    for y in range(0, 8):
        for x in range(0, 8):
            c = y // 2 % 2 + x % 2
            U(R(D(I(0, y % 2 + x * 2 - 6, y * 2 - 5, c), 1, c), 1, c), 1, c)
    turtle.done()


def pattern1_2():
    for y in range(0, 4):
        for x in range(0, 8):
            c = (x + y) % 2
            n = U(R(D(I(0, x * 2 - 8, y * 4 - 7, c), 1, c), 1, c), 1, c)
            D(L(U(U(n, 2, c), 3, c), 3, c + 1), 3, c + 1)
    turtle.done()


def pattern2_1():
    for y in range(-1, 1):
        for x in range(-2, 2):
            R(U(L(U(R(U(L(U(R(I(2 + y % 2, x * 4, y * 5))))))))))
            R(U(L(U(R(U(L(U(R(I(3 - y % 2, x * 4 + 2, y * 5))))))))))
    turtle.done()

def pattern2_2():
    S(R(Z(R(S(R(Z(R(S(R(Z(I(3, -6, -1)), 1)), 2), 3, 0, 1), 1), 3, 1, 0), 2)), 1))
    Z(R(S(R(Z(R(S(R(Z(R(S(I(2, -6,  0)), 3)), 2), 1, 0, 1), 3), 1, 1, 0), 2)), 3))
    turtle.done()


def pattern3():
    for y in range(0, 2):
        for x in range(0, 3):
            C(C(C(I(0, x * 7 - 8, y * 7 - 3.5, 1), 3, 1), 3, 1), 3, 1)
            E(C(E(C(E(C(E(I(0, x * 7 - 7.5, y * 7 - 7, 1)), 3, 3)), 3, 3)), 3, 3))
    turtle.done()

#--------------

# turtle.tracer(0, 0)  # onにすると一瞬で描画する
# pattern1_1()
# pattern1_2()
# pattern2_1()
# pattern2_2()
pattern3()

