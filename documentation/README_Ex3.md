__author__ = '8175858, Braun'

Analysis:
=========
The program is developed according to the EVA design pattern.
Input and output are done in the console. To call a function, write the function name.

Task a and b only allow Integers, while task c allows both Integers and Floating Point Numbers.

Output is done in the console or the Turtle window.

Testing the program:

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

Description of the program:
===========================
The program requires the epr_functions.py module.
The program is written and tested in Python 3.12.0. A Python interpreter must be installed.
The program can be started with the command "python3 ue03.py" in the terminal.
No bugs are known.

First the programm asks the user to give a function name. Based on that name i call the appropriate function and print the return value to the console or Turtle creates a window. The code is wrapped inside of a try except block to catch invalid function names and invalid input.