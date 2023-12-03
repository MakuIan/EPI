'''
GPR Exercise 6  - Ex. 1
'''
__author__ = '8175858, Braun'

# Ex. 1)


def unicode_strings(a: int, b: int) -> str:
    '''
    Takes two integers and decode them and the sum into unicode strings.
    Returns the decoded equation.
    '''
    code = ('\u2600', '\u2601', '\u2602', '\u2603', '\u2604',
            '\u262E', '\u262F', '\u263A', '\u263B', '\u263C')
    c = a + b

    def my_decode(num: int) -> str:
        s = ''
        while (num > 0):
            r = num % 10
            num = num // 10
            s = code[r] + s
        return s

    res = f'{my_decode(a)} + {my_decode(b)} = {my_decode(c)}'
    return res


if __name__ == '__main__':
    # Tests
    print(unicode_strings(123, 456))
    print(unicode_strings(12, 34))
    print(unicode_strings(1, 2))
