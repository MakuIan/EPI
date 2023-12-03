'''
GPR Exercise 6  - Ex. 3
'''

__author__ = '8175858, Braun'


# Ex. 3)


def get_school_info(student_infos: list[tuple[str, str]]) -> tuple[int, int, set[str]]:
    '''
    Takes a list of tuples with student names and subjects and 
    returns a tuple with the number of students, 
    the number of subjects and the most popular subject.
    '''
    names = set()
    subjects = {}

    for name, subject in student_infos:
        if name not in names:
            names.add(name)
        if subject not in subjects:
            subjects[subject] = 1
        else:
            subjects[subject] += 1
    name_count = len(names)
    subject_count = len(subjects)
    most_popular_subject_count = max(subjects.values())
    most_popular_subject = set()
    for key, val in subjects.items():
        if val == most_popular_subject_count:
            most_popular_subject.add(key)

    T_out = (name_count, subject_count, most_popular_subject)

    return T_out


if __name__ == '__main__':
    # Test 1
    student_info = [('Alice', 'Math'), ('Bob', 'Physics'),
                    ('Alice', 'Physics'), ('Bob', 'History'),
                    ('Charlie', 'Math'), ('Charlie', 'Physics')]
    school_info = get_school_info(student_info)
    print('Tupel T_out:', school_info)
    print(f'Number of student names: {school_info[0]}')
    print(f'Number of subjects: {school_info[1]}')
    print(f'Most popular subject: {", ".join (school_info[2])}')
    print('')

    # Test 2
    student_info = [('Alice', 'History'), ('Bob', 'Physics'),
                    ('Kenny', 'Physics'), ('Jude', 'History'),
                    ('Rob', 'History'), ('Charlie', 'Physics'), ('David', 'Math')]
    school_info = get_school_info(student_info)

    print('Tupel T_out:', school_info)
    print(f'Number of student names: {school_info[0]}')
    print(f'Number of subjects: {school_info[1]}')
    print(f'Most popular subject: {", ".join (school_info[2])}')
    print('')
