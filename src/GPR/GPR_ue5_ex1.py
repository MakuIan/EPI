'''
Aufgabe 1: String Slicing
'''
__author__ = '8175858, Braun'

S = 'Ich_mag_programmieren'
A = S[-1::-2]
B = S[4:7]
C = S[:8]
D = S[2:]
E = S[-1:2:-1]
F = S[-2:-9:-2]

if __name__ == '__main__':
    print('a)', A)
    print('b)', B)
    print('c)', C)
    print('d)', D)
    print('e)', E)
    print('f)', F)
