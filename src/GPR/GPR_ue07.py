'''
GPR - Übung 07
'''

__author__ = '8175858, Braun'


def get_best_students(students: dict) -> dict:
    '''
    Takes in a dictionary of students and their grades and 
    returns a dictionary of the best students.
    '''

    best_grades = {}
    for key, value in students.items():
        if value[0] == 'EPI':
            sum_of_grades = sum(value[1]) / len(value[1])
            if len(best_grades) < 3:
                best_grades[key] = sum_of_grades
            else:
                if sum_of_grades > any(value for value in best_grades.values()):
                    min_grade = min(best_grades.values())
                    print('min_grade', min_grade)
                    print('best', best_grades)
                    min_grade_key = min(
                        best_grades, key=lambda k: best_grades[k])
                    print('min_grade_key', min_grade_key)
                    best_grades.pop(min_grade_key)
                    best_grades[key] = sum_of_grades
    best_students = {key: students[key] for key in best_grades}
    return best_students


if __name__ == '__main__':
    input_dict = {'mark': ['EPI', (1, 2, 3, 4, 5)],
                  'peter': ['EPI', (2, 2, 3, 4, 5)],
                  'hans': ['EPI', (3, 2, 3, 4, 5)],
                  'michael': ['EPI', (4, 2, 3, 4, 5)],
                  'hans2': ['EPI', (5, 2, 2, 4, 5)],
                  'hans3': ['EPI', (6, 2, 1, 4, 5)],
                  'hans4': ['EPI', (6, 2, 4, 4, 5)],
                  'hans5': ['EPI', (6, 1, 2, 4, 5)],
                  'hans6': ['EPI', (6, 1, 5, 4, 5)],
                  'hans7': ['EPI', (6, 2, 3, 5, 6)]}
    print(get_best_students(input_dict))
