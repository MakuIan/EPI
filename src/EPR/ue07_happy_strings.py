'''
Implementation of the happy strings problem.
'''

__author__ = '8175858, Braun'


def is_happy_string(s):
    ''' Function to check if a string is happy'''
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 1
        else:
            memo[c] += 1
    for value in memo.values():
        if value % 2 != 0:
            return False
    return True


def traverse_string(s, i, happy_pairs):
    ''' Helper function to traverse a string'''
    if i < 0:
        return ''
    return traverse_string(s, i - 1, happy_pairs) + s[i]


def find_happy_pairs_helper(s, i, happy_pairs):
    ''' Helper function to find all happy pairs in a string'''
    n = len(s)
    if i >= n:
        return is_happy_string(s)
    string = traverse_string(s, i, happy_pairs)

    if is_happy_string(string):
        happy_pairs.add(string)
    return find_happy_pairs_helper(s, i + 1, happy_pairs)


def find_happy_pairs(s):
    ''' Function to find all happy pairs in a string'''
    n = len(s)
    happy_pairs = set()
    for i in range(n):
        find_happy_pairs_helper(s[i:], 0, happy_pairs)
    return len(happy_pairs)


if __name__ == '__main__':
    S = '20230322'
    result = find_happy_pairs(S)
    print(result)
