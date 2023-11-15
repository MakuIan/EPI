import turtle
import random
import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'


def decimal_to_octal(num: int) -> str:
    return decimal_to_basis(num, 8)


def decimal_to_basis(num: int, basis: int) -> str:
    if num == 0:
        return '0'
    res = ''
    while (num != 0):
        r = num % basis
        num //= basis
        res = str(r) + res
    return res


def chaos_turtle(i: int, x: int, y: int) -> None:
    triangle = ((10, 20), (0, 100), (100, 0))
    print(type(triangle))
    t = turtle.Turtle()
    t.penup()
    t.setpos(x, y)
    t.pendown()
    while (i > 0):
        r = random.randint(0, 2)
        v = triangle[r]
        midpoint = ((t.xcor() + v[0]) / 2, (t.ycor() + v[1]) / 2)
        t.penup()
        t.goto(midpoint)
        t.pendown()
        t.dot()
        i -= 1
    turtle.done()


if __name__ == '__main__':
    print(decimal_to_octal(10))
    print(decimal_to_basis(10, 2))
    chaos_turtle(10, 0, 0)
