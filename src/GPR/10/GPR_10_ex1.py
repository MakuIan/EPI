'''
GPR - Übung 10 Ex 1
'''

__author__ = '8175858, Braun'

import re

import os


current_dir = os.path.dirname(os.path.abspath(__file__))

kleopatra_file = os.path.join(current_dir, "Kleopatra.txt")

pattern = r'\bsie\b'

with open(kleopatra_file, 'r') as f:
    text = f.read()
    new_text = re.sub(pattern, 'er', text)

    print(new_text)
