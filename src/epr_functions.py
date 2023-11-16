'''
module for ue03
'''
__author__ = '8175858, Braun'

import turtle
import random
import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'


def decimal_to_octal(num: int) -> str:
    '''
    Converts a decimal number to octal
    '''
    return decimal_to_basis(num, 8)


# Testcases


def decimal_to_basis(num: int, basis: int) -> str:
    '''
    Converts a decimal number to a number of a given basis
    '''
    if num == 0:
        return '0'
    res = ''
    conversion_map = {0: '0', 1: '1', 2: '2', 3: '3',
                      4: '4', 5: '5', 6: '6', 7: '7',
                      8: '8', 9: '9', 10: 'A', 11: 'B',
                      12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    while num != 0:
        r = conversion_map[num % basis]
        num //= basis
        res = str(r) + res
    return res
# Testcases


def chaos_turtle(i: int, x: int, y: int) -> None:
    '''
    Draws dots with turtle module. In each step the turtle moves halfway to one of three points
    '''
    triangle = ((10, 20), (0, 100), (100, 0))
    t = turtle.Turtle()
    t.penup()
    t.setpos(x, y)
    t.pendown()
    while i > 0:
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
    print('decimal_to_octal')
    print(decimal_to_octal(10))  # 12
    print(decimal_to_octal(8))  # 10
    print(decimal_to_octal(0))  # 0
    print('decimal_to_basis')
    print(decimal_to_basis(10, 2))  # 1010
    print(decimal_to_basis(10, 8))  # 12
    print(decimal_to_basis(170, 16))  # AA
