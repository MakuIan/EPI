'''
GPR - Übung 10
'''

__author__ = '8175858, Braun'

import re

import os


current_dir = os.path.dirname(os.path.abspath(__file__))

wortgitter_file = os.path.join(current_dir, "Wortgitter_mitZahlen.txt")

i = r'0\d[a-zA-Z]'
iii = r'\d{2,3}'


def task_a(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        print('i)')
        for line in lines:
            if re.search(i, line):
                print(re.search(i, line).group())
                break
        print('ii)')
        temp = []
        for line in lines:
            if re.search(i, line):
                temp.append(re.search(i, line).group())
        print(temp)
        print('iii')
        s = ''
        for line in lines:
            if re.search(iii, line):
                s = re.findall(iii, line)
                print(s)


if __name__ == '__main__':
    task_a(wortgitter_file)
