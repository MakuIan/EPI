'''
EPR 7 - Exercise 1 and 2
'''

__author__ = "8168265, Karabacak, 8175858, Braun"


def find_smallest_neighbour(matrix, i, j, visited):
    '''
    Find the smallest neighbour of a given position in a matrix
    '''
    smallest_neighbour = 10
    smallest_neighbour_index = tuple()

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[i]):

            if matrix[ni][nj] < smallest_neighbour and (ni, nj) not in visited:

                smallest_neighbour = matrix[ni][nj]
                smallest_neighbour_index = (ni, nj)

    return smallest_neighbour_index


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
    visited = set()

    while i < len(matrix) and j < len(matrix[i]):
        way.append((i, j))
        visited.add((i, j))
        if i == len(matrix) - 1:
            j += 1
        elif j == len(matrix[i]) - 1:
            i += 1
        else:
            neighbor = find_smallest_neighbour(matrix, i, j, visited)
            if not neighbor:
                break
            i, j = neighbor if neighbor else (i, j)
    if way[-1] != (len(matrix) - 1, len(matrix[-1]) - 1):
        print('No way found')
    return way


def find_best_way(matrix, i=0, j=0, visited=set(), way=None):
    '''
    Find the best way through a matrix with a brute force approach

    >>> find_best_way([[5 , 3], [-6 , 7]])
    (6, [(0, 0), (1, 0), (1, 1)])

    >>> find_best_way([[2 , 9, -4], [-7 , 6, 8], [-3 , 1, 5]])
    (-2, [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)])

    >>> find_best_way([[5 , 6, 3], [9 , 8, 3], [4 , 4, 2]])
    (19, [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)])
    '''
    # Base Case
    if way is None:
        way = []

    if (i, j) in visited:
        # Return infinity to avoid revisiting already visited cells
        return float('inf'), way

    if i < 0:
        return float('inf'), way
    if j < 0:
        return float('inf'), way
    if i >= len(matrix):
        return float('inf'), way
    if j >= len(matrix[i]):
        return float('inf'), way

    cost = matrix[i][j]
    way.append((i, j))

    # Check if we reached the end
    if i == len(matrix) - 1 and j == len(matrix[i]) - 1:
        return cost, way

    visited.add((i, j))
    # Recursive Case
    down_cost, down_way = find_best_way(matrix, i+1, j, visited, way.copy())
    up_cost, up_way = find_best_way(matrix, i-1, j, visited, way.copy())
    left_cost, left_way = find_best_way(matrix, i, j - 1, visited, way.copy())
    right_cost, right_way = find_best_way(
        matrix, i, j + 1, visited, way.copy())

    visited.remove((i, j))

    # Find the minimum cost among the possible moves
    min_cost, min_way = min(
        (down_cost, down_way),
        (up_cost, up_way),
        (left_cost, left_way),
        (right_cost, right_way),
        key=lambda x: x[0]
    )

    return cost + min_cost, min_way


if __name__ == '__main__':

    import doctest
    doctest.testmod()
