__author__ = '8175858, Braun'

# Handlungsvorschrift 1
a, b = eval(input("Bitte geben Sie die erste Zahl ein: ")), eval(
    input("Bitte geben Sie die zweite Zahl ein: "))
while b != 0:
    h = a % b
    a = b
    b = h
print(a)
