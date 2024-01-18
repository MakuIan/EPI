'''
gpr excercise 11
'''
__author__ = '8175858, Braun'
from huffmann_tree import Node

with open('table_GPR11.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    code = {}
    for line in range(1, len(lines)):
        split_line = lines[line].split()
        code[split_line[0]] = split_line[4]
    code.pop('22')
    code[' '] = '00'
    swapped_code = {value: key for key, value in code.items()}


def encode(text):
    '''
    encode text via huffman code   
    '''
    encoded_text = ''
    for letter in text.lower():
        if letter not in code:
            raise ValueError(f'letter not encodable: {letter}')
        encoded_text += code[letter]
    return encoded_text


def build_huffman_tree():
    def list_to_binary_tree(lst, index=0):
        if index < len(lst):
            node = Node(lst[index])
            node.left = list_to_binary_tree(lst, 2 * index + 1)
            node.right = list_to_binary_tree(lst, 2 * index + 2)
            return node
        return None
    root = Node(1)
    # left nodes
    root.left = Node(0.393)
    root.left.left = Node(0.206)
    root.left.right = Node(0.187)
    root.left.right.left = Node(0.112)
    root.left.right.right = Node(0.075)

    # right nodes
    right_nodes = [0.578,
                   0.411, 0.167,
                   0.243, 0.168, 0.121, 0.046,
                   0.131, 0.112, 0.094, 0.074, 0.074, 0.074, 0.028, 0.018,
                   0.075, 0.056, 0.056, 0.056, 0.047, 0.047, 0.037, 0.037, 0.037, 0.037, 0.028, 0.019, 0.019, 0.009, 0.009, 0.009]
    root.right = list_to_binary_tree(right_nodes)

    return root


def decode(encoded_text, tree):
    '''
    decode text via huffman code   
    '''
    decoded_text = ''
    bits = ''
    node = tree
    for bit in encoded_text:
        if bit == '0':
            bits += bit
            node = node.left
        elif bit == '1':
            bits += bit
            node = node.right
        if node.left is None and node.right is None:
            decoded_text += swapped_code[bits]
            node = tree
            bits = ''
    return decoded_text


if __name__ == '__main__':
    QUOTE = 'One Ring to rule them all, One Ring to find them, One Ring to bring them all, and in the darkness bind them'
    print(encode(QUOTE))
    print(code)
    # path = build_huffman_tree().traverse()
    # print(path)
    print(decode(encode(QUOTE), build_huffman_tree()))
