__author__ = '8175858, Braun'
# change parameters to test different cases

# task 2


def task2(epr, gpr, zbnp=50):
    if epr > 110 or gpr > 110:
        return 'Invalid input: epr and gpr must be less than 110!'
    if epr < 0 or gpr < 0:
        return 'Invalid input: epr and gpr must be greater than or equal 0!'
    return round(min(zbnp / 4, (epr + gpr) / 14), 1)

# Test cases:
# task2(110, 110) = 12.5
# task2(120, 110) = Invalid input: epr and gpr must be less than 110!
# task2(80, 40) = 8.6

# task 3


def task3(num1, num2):
    minimal = min(num1, num2)
    is_divisible = {"minimal": minimal, "2": False, "4": False, "8": False}
    if (minimal % 2 == 0):
        is_divisible["2"] = True
    if (minimal % 4 == 0):
        is_divisible["4"] = True
    if (minimal % 8 == 0):
        is_divisible["8"] = True
    return is_divisible

# Test cases:
# task3(2, 4) = {'2': True, '4': False, '8': False}
# task3(4, 5) = {'2': True, '4': True, '8': False}
# task3(7, 8) = {'2': False, '4': False, '8': False}


if __name__ == '__main__':
    epr = eval(input('Enter EPR Bonuspoints: '))
    gpr = eval(input('Enter GPR Bonuspoints: '))
    print(f'{task2(epr, gpr)} Bonuspoints given!')
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    is_divisible = task3(num1, num2)
    print(f'min Value:{is_divisible["minimal"]}')
    print(f'is divisible by 2:{is_divisible["2"]} ')
    print(f'is divisible by 4:{is_divisible["4"]} ')
    print(f'is divisible by 8:{is_divisible["8"]} ')
