'''
gpr excercise 11
'''
__author__ = '8175858, Braun'

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


def decode(encoded_text):
    '''
    decode text via huffman code   
    '''
    decoded_text = ''
    bits = ''
    for bit in encoded_text:
        bits += bit
        if bits in swapped_code:
            decoded_text += swapped_code[bits]
            bits = ''
    return decoded_text


if __name__ == '__main__':
    QUOTE = 'One Ring to rule them all, One Ring to find them, One Ring to bring them all, and in the darkness bind them'
    print(encode(QUOTE))
    print(code)
    # path = build_huffman_tree().traverse()
    # print(path)
    print(decode(encode(QUOTE)))
