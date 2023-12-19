'''
Implementation of the happy strings problem.
'''

__author__ = '8175858, Braun'


def is_happy_string(input_str):
    n = len(input_str)
    mid = n // 2
    if n % 2 == 0:
        left = input_str[:mid]
        right = input_str[mid:]
    else:
        left = input_str[:mid]
        right = input_str[mid + 1:]
    return left == right


def get_permutations(input_str):
    ''' Helper function to get all permutations of a string'''
    def generate_permutations(current_str, remaining_chars, permutations):
        ''' Recursive function to generate all permutations of a string'''
        if not remaining_chars:
            permutations.add(current_str)
            return
        for i in range(len(remaining_chars)):
            new_str = current_str + remaining_chars[i]
            new_remaining = remaining_chars[:i] + remaining_chars[i + 1:]
            generate_permutations(new_str, new_remaining, permutations)

    permutations = set()
    generate_permutations("", input_str, permutations)
    return permutations


def find_happy_pairs(s):
    ''' Function to find all happy pairs in a string'''
    permutations = get_permutations(s)
    happy_pairs = []
    for perm in permutations:
        if is_happy_string(perm):
            happy_pairs.append(perm)

    return (happy_pairs)


if __name__ == '__main__':
    S = '20230322'
    result = find_happy_pairs(S)
    print(result)
