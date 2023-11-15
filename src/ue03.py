'''
ue03 EPR
'''

import epr_functions as epr

func = input('Enter function name: ')

try:

    if func == 'decimal_to_octal':
        num = int(input('Enter number to convert: '))
        epr.decimal_to_octal(num)
    elif func == 'decimal_to_basis':
        num = int(input('Enter number to convert: '))
        basis = int(input('Enter basis: '))
        epr.decimal_to_basis(num, basis)
    elif func == 'chaos_turtle':
        i = int(input('Enter iteration count: '))
        x = int(input('Enter x-position: '))
        y = int(input('Enter y-postion: '))
        epr.chaos_turtle(i, x, y)
    else:
        print('Invalid function name')
except ValueError:
    print('Invalid input')
