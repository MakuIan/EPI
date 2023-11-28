author__ = '8175858, Braun'

# Ex. 1)


def unicode_strings(a: int, b: int) -> str:
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


print(unicode_strings(123, 456))

# Ex. 3)


def get_school_info(student_info):
    names = set()
    subjects = {}

    for name, subject in student_info:
        if name not in names:
            names.add(name)
        if subject not in subjects:
            subjects[subject] = 1
        else:
            subjects[subject] += 1
    name_count = len(names)
    subject_count = len(subjects)
    most_popular_subject_count = max(subjects.values())
    most_popular_subject = []
    for key, val in subjects.items():
        if val == most_popular_subject_count:
            most_popular_subject.append(key)
        pass
    T_out = (name_count, subject_count, most_popular_subject[0])
    if len(most_popular_subject) > 1:
        print(
            f'All the most popular subjects include: {", ".join(str(subject) for subject in most_popular_subject)}')
    return T_out


student_info = [('Alice', 'Math'), ('Bob', 'Physics'),
                ('Alice', 'Physics'), ('Bob', 'Math'), ('Charlie', 'Math'), ('Charlie', 'Physics')]
print(get_school_info(student_info))  # (3, 2, 2)
