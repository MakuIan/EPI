'''
    This file contains the implementation of the huffman tree.
'''
__author__ = '8175858, Braun'


class Node:
    '''
    This class represents a node in the huffman tree.
    '''

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def traverse(self, path=''):
        if self.left is None and self.right is None:
            print(f'{self.value}: {path}')
        else:
            if self.left is not None:
                self.left.traverse(path + str(self.value) + ' ')
            if self.right is not None:
                self.right.traverse(path + str(self.value) + ' ')
        return path
