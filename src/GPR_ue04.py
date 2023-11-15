'''
Exercise 3 - GPR UE04
'''


def decimal_to_basis(num: int, basis: int) -> str:
    '''
    function that I wrote in EPR ue03. Converts a decimal number to a number of a given basis
    '''
    if num == 0:
        return '0'
    res = ''
    while (num != 0):
        r = num % basis
        num //= basis
        res = str(r) + res
    return res


def decimal_to_binary_floating_point(num: float) -> str:
    '''
    Converts a decimal number to binary
    '''
    if num <= 0 or num >= 1:
        return 'Invalid input'

    temp = ''
    for i in range(0, 31):
        fraction = num * 2
        if fraction >= 1:
            temp += '1'
            num = fraction - 1
        elif fraction == 0:
            temp += '0' * (31 - i)
            break
        else:
            temp += '0'
            num = fraction

    return ('0.' + temp)


if __name__ == '__main__':
    print(decimal_to_binary_floating_point(0.5))
