'''
EPR 7 - Exercise 3
'''
__author__ = "8168265, Karabacak, 8175858, Braun"

import timeit
import ue07 as f


if __name__ == '__main__':
    matrices = [
        [[1, 2], [3, 4]],  # 2x2 matrix
        [[4, 2], [-8, 3]],  # 2x2 matrix
        [[1, 2, -3], [4, -5, 6], [7, - 8, 9]],  # 3x3 matrix
        [[5, 6, -7, 8], [9, 8, -2, 8], [1, -3, 4, 1],
            [1, 1, -1, 0]],  # 4x4 matrix
        [[1, 2, 3, -4, 5], [6, 7, 8, 9, 2], [9, -5, -4, 2, 2], [
            -1, 1, 8, - 9, 2], [2, 2, 2, - 2, 5]],  # 5x5 matrix
        [[2, 4, 6, -8, -9, 7],
         [3, -5, 1, 9, -6, 0],
            [8, -2, 5, -7, 4, -3],
            [1, 6, -4, 0, 9, -1],
            [-9, 3, 7, -6, 2, 8],
            [5, -1, 4, -3, 6, -8]],  # 6x6 matrix
    ]
    for matrix in matrices:
        print(f'Greedy traversal of {matrix}:')
        t = timeit.timeit(lambda: f.greedy_traversal(matrix), number=10)
        print('way: ', f.greedy_traversal(matrix))
        print(t)
        print()
        print(f'Optimal traversal of {matrix}:')
        t = timeit.timeit(lambda: f.find_best_way(matrix), number=10)
        print('way: ', f.find_best_way(matrix)[1])
        print(t)
        print()
