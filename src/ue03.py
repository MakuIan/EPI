__author__ = 'Braun, 8175858'


def decimal_to_binary(a: int) -> int:
    """Converts a decimal number to a binary number

    Args:
        a (int): Decimal number

    Returns:
        int: Binary number
    """
    res = 0
    i = 0
    while (a > 0):
        r = a % 2
        res += r * (10 ** i)
        a = a // 2
        i += 1
    return res


if __name__ == '__main__':
    try:
        print(decimal_to_binary(int(input("Decimal number: "))))
    except ValueError:
        print("Invalid input")
