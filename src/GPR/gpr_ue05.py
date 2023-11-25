'''
GPR - Übung 05
'''
__author__ = 'Braun, 8175858'


def str_find(needle: str, haystack: str) -> int:
    ''' 
    This function finds the first occurence of needle within haystack and 
    returns the lowest index of the occurrence of needle in haystack.
    '''
    l = 0
    r = 0
    n = 0
    while l < len(haystack):
        if haystack[l] == needle[n]:
            if n == 0:
                r = l + 1
                n += 1
            else:
                if haystack[r] == needle[n]:
                    r += 1
                    n += 1
                else:
                    n = 0
                    l += 1
        else:
            l += 1

        if n == len(needle) - 1:
            return l
    return -1


if __name__ == '__main__':
    print(str_find('abc', 'abcabc'))
