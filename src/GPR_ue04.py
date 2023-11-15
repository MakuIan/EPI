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
