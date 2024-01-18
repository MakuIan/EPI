

def count_letters(text):
    """Count the number of times each letter occurs in text."""
    counts = {}
    for letter in text:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts


def display_counts(counts):
    """Display the letter counts in a GUI window."""
    with open('src/letter_counts.txt', 'w') as file:
        for letter, count in sorted(counts.items()):
            file.write(f'{letter}: {count}\n')


if __name__ == '__main__':
    QUOTE = 'One Ring to rule them all, One Ring to find them, One Ring to bring them all, and in the darkness bind them'
    counts_dict = count_letters(QUOTE)
    display_counts(counts_dict)
