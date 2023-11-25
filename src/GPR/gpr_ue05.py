'''
GPR - Übung 05
'''
__author__ = '8175858, Braun'


def str_find(needle: str, haystack: str) -> int:
    ''' 
    This function finds the first occurence of needle within haystack and 
    returns the lowest index of the occurrence of needle in haystack.
    '''
    l = r = n = 0
    while r < len(haystack):
        if haystack[r] == needle[n]:
            r += 1
            n += 1
        else:
            l += 1
            r = l

        if n == len(needle):
            return l
    return -1


if __name__ == '__main__':
    needle = input('Enter needle: ')
    haystack = input('Enter haystack: ')
    print(str_find(needle, haystack))
