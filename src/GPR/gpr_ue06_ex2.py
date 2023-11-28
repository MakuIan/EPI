author__ = '8175858, Braun'

# Ex. 1)


def unicode_strings(a: int, b: int) -> str:
    code = ('\u2600', '\u2601', '\u2602', '\u2603', '\u2604',
            '\u262E', '\u262F', '\u263A', '\u263B', '\u263C')
    c = a + b

    def own_decode(num: int) -> str:
        s = ''
        while (num > 0):
            r = num % 10
            num = num // 10
            s = code[r] + s
        return s
    print(own_decode(a))


print(unicode_strings(1, 456))
# Ex. 2)
# a)
# Sorted() accepts an iterable (sets, generators, lists, dictionaries, strings) and returns a new sorted list.

# List() accepts an iterable and returns it as a list.


# Test
numbers = [13, 22, 10, 44, 52, 20, 76, 78, 549, 10]
names = {'Bob', 'Alice', 'David', 'Charlie', 'Eve'}

print('a)')
print(sorted(numbers))
print(sorted(names))
print('')
print(list(numbers))
print(list(names))

# b)
multiple1 = {2, 'a'}
multiple2 = {2, (1, 2)}
multiple3 = {2, 3, True}
print('b)')
try:
    print(list(multiple1))
    print(sorted(multiple1))
except TypeError as e:
    print(e)
try:
    print(list(multiple2))
    print(sorted(multiple2))
except TypeError as e:
    print(e)
print(list(multiple3))

# sorted() can't sort a set with multiple differnet types It would work with int and bool, because bool is a subclass of int.
# list() might not return a liste with the elements in the same order as seen with list(multiple3)
# (list() : for all Sets where order is not important, sorted() : for all Sets with the same type that can be compated)
