import copy


def greedy_traversal(matrix):
    '''
    Traversal through a matrix with a greedy algorithm

    >>> greedy_traversal([[5 , 6, 3], [9 , 8, 3], [4 , 4, 2]])
    [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

    >>> greedy_traversal([[2 , 9, -4], [-7 , 6, 8], [-3 , 1, 5]])
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

    >>> greedy_traversal([[5 , 3], [-6 , 7]])
    [(0, 0), (1, 0), (1, 1)]
    '''
    i = j = 0
    way = []
    while i < len(matrix):
        way.append((i, j))
        if j == len(matrix[i]) - 1:
            i += 1
        elif i == len(matrix) - 1:
            j += 1
        elif matrix[i][j+1] > matrix[i+1][j]:
            i += 1
        else:
            j += 1
    return way


def find_best_way(matrix, i=0, j=0, visited=set()):
    # Base Case
    print('i', i, 'j', j)
    if (i, j) in visited:
        return 0
    if i < 0 or j < 0:
        return 0
    if i >= len(matrix) or j >= len(matrix[i]) - 1:
        return 0
    cost = matrix[i][j]
    # TODO: check if we reached the end
    if i == len(matrix) - 1 and j == len(matrix[i]) - 1:
        return cost

    visited.add((i, j))
    # Recursive Case
    down = cost + find_best_way(matrix, i+1, j, visited)
    up = cost + find_best_way(matrix, i-1, j, visited)
    left = cost + find_best_way(matrix, i, j - 1, visited)
    right = cost + find_best_way(matrix, i, j + 1, visited)

    visited.remove((i, j))
    return min(down, up, left, right)


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    matrix = [[4, 0, 8], [-3, -4, 7], [-8, -1, 7]]
    print(find_best_way(matrix))
