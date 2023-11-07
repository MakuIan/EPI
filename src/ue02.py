# task a
def task_a(num1: int, num2: int):
    if num1 > num2:
        num1, num2 = num2, num1
    return sum([num for num in range(num1, num2 + 1)])

# Testcases
# print(task_a(1, 5)) => 15
# print(task_a(5, 1)) => 15
# print(task_a(1, 1)) => 1

# task b


def task_b(num):
    i = 0
    while num != 0:
        num /= 2
        i += 1
    return i

# Testcases
# print(task_b(2)) => 1076
# print(task_b(3)) => 1077
# print(task_b(10)) => 1078

# task c


def task_c(n: int, m: int):
    if n or m < 0:
        return 'n or m must be greater than 0'
    row = tuple(j % 2 for j in range(0, m))
    row2 = tuple(j % 2 for j in range(1, m + 1))
    for i in range(0, n):
        if i % 2 == 0:
            print(*row)
            continue
        print(*row2)

# Testcases
# task_c(3, 4) => 0 1 0 1
#                 1 0 1 0
#                 0 1 0 1
# task_c(0, 4) =>
# task_c(-2, 4) => n or m must be greater than 0


def task_d(n: int):
    if n < 0:
        return 0
    temp = 0
    for k in range(0, n):
        temp += (((-1) ** k) / (2*k + 1) ** 2)
    return temp

# Testcases
# print(task_d(7)) => 0.9184791015893248
# print(task_d(0)) => 0
# print(task_d(-1)) => 0

# task e


def task_e(num1: int, num2: int, num3: int):
    if num3 < 0 and num1 < num2:
        print('end not in range')
        return
    if num3 > 0 and num1 > num2:
        print('end not in range')
        return
    if num1 < num2:
        while num1 < num2:
            temp = num1 + num3
            cat_num1 = task_d(num1)
            cat_temp = task_d(temp)
            difference = cat_temp - cat_num1
            print('n=', num1, ':', cat_num1, ';', 'n=', temp,
                  ':', cat_temp, ';', 'difference:', difference)
            num1 = temp
    else:
        while num1 > num2:
            temp = num1 + num3
            cat_num1 = task_d(num1)
            cat_temp = task_d(temp)
            difference = cat_temp - cat_num1
            print('n=', num1, ':', cat_num1, ';', 'n=', temp,
                  ':', cat_temp, ';', 'difference:', difference)
            num1 = temp


# Testcases
# task_e(4, 10, 3) => n= 4 : 0.9084807256235827 ; n= 7 : 0.9184791015893248 ; difference: -0.009998375965742046
#                     n= 7 : 0.9184791015893248; n= 10 : 0.914724781654844; difference: -0.003754319934480721
# task_e(4, 10, -3) => n= 4 : end not in range
# task_e(10, 4, -3) => n= 10 : 0.914724781654844 ; n= 7 : 0.9184791015893248 ; difference: 0.003754319934480721
#                      n= 7 : 0.9184791015893248 ; n= 4 : 0.9084807256235827 ; difference: -0.009998375965742046


if __name__ == "__main__":
    print('task a:', task_a(1, 1))
    print('task b:', task_b(2))
    print('task c:')
    task_c(0, 4)
    print('task d:', task_d(7))
    print('task e:')
    task_e(10, 4, -3)
