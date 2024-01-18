'''
Count the number of times each letter occurs in a text file.
'''

import math


def count_letters(text):
    """Count the number of times each letter occurs in text."""
    counts = {}
    for letter in text.lower():
        if letter in counts:
            counts[letter][0] += 1
        else:
            counts[letter] = [1]
    for letter, count in counts.items():
        count.append(round(count[0] / len(text), 3))
        def entropie_formula(x): return -1 * x * math.log2(x)
        count.append(round(entropie_formula(count[1]), 3))
    huffman_codes = ['00', '11010', '10111', '11100', '10110', '011', '11111', '11001',
                     '10100', '10001', '11101', '10101', '11000', '010', '10011', '10010', '11011', '10000', '11110']
    for letter, count in sorted(counts.items()):
        count.append(huffman_codes.pop(0))
        count.append(round(len(count[3]) * count[1], 3))
    print(counts)
    print()
    print(sorted(counts.items(), key=lambda x: x[1]))
    return counts


def display_counts(counts):
    """Display the letter counts in a text file."""
    header = ('Letter', 'Absolute', 'Relative', 'Entropie',
              'Huffman', 'Mittlere Codewortlänge')
    letters = sorted(counts.keys())
    with open('table_GPR11.txt', 'w', encoding='utf-8') as file:
        # Write the header row
        file.write('{:<7}{:>10}{:>10}{:>10}{:>10}{:>25}\n'.format(*header))

        # Write the data rows
        for letter in letters:
            file.write('{:<7}{:>10}{:>10}{:>10}{:>10}{:>15}\n'.format(
                letter, *counts[letter]))
    s = 0
    for letter in counts:
        s += counts[letter][1]
    print(s)


if __name__ == '__main__':
    QUOTE = 'One Ring to rule them all, One Ring to find them, One Ring to bring them all, and in the darkness bind them'
    counts_dict = count_letters(QUOTE)
    display_counts(counts_dict)
