'''
GPR - Übung 07
'''

__author__ = '8175858, Braun'
import ast

# Exercise 1


def get_best_students(students: dict) -> dict:
    '''
    Takes in a dictionary of students and their grades and 
    returns a dictionary of the best students.
    '''

    best_students = list()
    for key, value in students.items():
        if value[0] == 'EPI':

            best_grade = min(value[1])
            if len(best_students) < 3:
                best_students.append(key)
            else:
                worst_student = best_students[0]
                for student in enumerate(best_students, start=1):

                    if min(students[student[1]][1]) > min(students[worst_student][1]):
                        worst_student = student[1]

                if best_grade < min(students[worst_student][1]):
                    best_students.remove(worst_student)
                    best_students.append(key)

    return {student: students[student] for student in best_students}

# Exercise 2


def christmas_storie(n: int, memo: dict = {}) -> int:
    '''
    Uses Tribonacci to calculate the number of possible ways to climb a stair with n steps.
    Dict memo is used to store already calculated values.
    '''
    if n in (2, 1):
        return 1
    if n == 0:
        return 0
    if n not in memo:
        result = christmas_storie(n-1, memo) + christmas_storie(
            n-2, memo) + christmas_storie(n-3, memo)
        memo[n] = result
    return memo[n]


if __name__ == '__main__':
    input_dict = {}
    try:
        # Example input {'Alice': ['ARA', (1, 2, 4)], 'Bob': ['EPI', (5)],
        # 'Charlie': ['EPI', (2.2, 1)], 'David': ['EPI', (5, 5, 5)], 'Eve': ['EPI', (5,5,1)]}
        input_dict = ast.literal_eval(input('Enter a dictionary: '))
    except Exception:
        print('Invalid input.')
    # turning int grades into tuples (5) => (5,)
    for value in input_dict.values():
        if isinstance(value[1], int):
            value[1] = (value[1],)
    print(get_best_students(input_dict))
    print('Case 5:', christmas_storie(5))
    print('Case 6:', christmas_storie(6))
