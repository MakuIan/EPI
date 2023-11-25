__author__ = 'Braun, 8175858'


def decimal_to_binary(a: int) -> int:
    """Converts a decimal number to a binary number

    Args:
        a (int): Decimal number

    Returns:
        int: Binary number
    """
    res = ''
    if a == 0:
        return 0
    while (a > 0):
        r = a % 2
        res = str(r) + res
        a = a // 2
    return int(res)
# Testcase
# print(decimal_to_binary(10)) # 1010
# print(decimal_to_binary(0)) # 0
# print(decimal_to_binary(1)) # 1


if __name__ == '__main__':
    try:
        print(decimal_to_binary(int(input("Decimal number: "))))
    except ValueError:
        print("Invalid input")
