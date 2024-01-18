'''
Count the number of times each letter occurs in a text file.
'''

import math


def count_letters(text):
    """Count the number of times each letter occurs in text."""
    counts = {}
    for letter in text:
        if letter in counts:
            counts[letter][0] += 1
        else:
            counts[letter] = [1]
    for letter, count in counts.items():
        count.append(round(count[0] / len(text), 3))
        def entropie_formula(x): return -1 * count[1] * math.log2(count[1])
        count.append(round(entropie_formula(count[1]), 3))
    print(counts)
    return counts


def display_counts(counts):
    """Display the letter counts in a text file."""
    header = ('Letter', 'Absolute', 'Relative', 'Entropie')
    letters = sorted(counts.keys())

    with open('table_GPR11.txt', 'w', encoding='utf-8') as file:
        # Write the header row
        file.write('{:<7}{:>10}{:>10}{:>10}\n'.format(*header))

        # Write the data rows
        for letter in letters:
            file.write('{:<7}{:>10}{:>10}{:>10}\n'.format(
                letter, *counts[letter]))


if __name__ == '__main__':
    QUOTE = 'One Ring to rule them all, One Ring to find them, One Ring to bring them all, and in the darkness bind them'
    counts_dict = count_letters(QUOTE)
    display_counts(counts_dict)
