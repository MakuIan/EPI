'''
ue03 EPR
using functions defined in epr_functions.py
'''
__author__ = '8175858, Braun'

import epr_functions as epr
if __name__ == '__main__':

    func = input('Enter function name: ')

    try:

        if func == 'decimal_to_octal':
            num = int(input('Enter number to convert: '))
            print(epr.decimal_to_octal(num))
        elif func == 'decimal_to_basis':
            num = int(input('Enter number to convert: '))
            basis = int(input('Enter basis: '))
            print(epr.decimal_to_basis(num, basis))
        elif func == 'chaos_turtle':
            i = float(input('Enter iteration count: '))
            x = float(input('Enter x-position: '))
            y = float(input('Enter y-postion: '))
            print(epr.chaos_turtle(i, x, y))
        else:
            print('Invalid function name')
    except ValueError:
        print('Invalid input')

# Testcases
# Enter function name: decimal_to_octal
# Enter number to convert: 10
# 12

# Enter function name: decimal_to_basis
# Enter number to convert: 10
# Enter basis: 2
# 1010

# Enter function name: chaos_turtle
# Enter iteration count: 1000
# Enter x-position: 0
# Enter y-postion: 0

# Enter function name: none
# Invalid function name
