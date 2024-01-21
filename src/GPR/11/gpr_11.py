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
    print('GPR 11')
    print('-----')
    print('Tests')
    print('-----')
    Q1 = "o, r t b n o b, h a a o s h a i"
    Q2 = "s a t r s, a o a r f m t s u a l a s"
    Q3 = "h a t a a o t f r a d r e r e h u r a"
    Q4 = "u t u a b f e a b d n r o a t"
    Q5 = "h a t a a o t f r a d r e r e h u r a"
    quotes = (Q1, Q2, Q3, Q4, Q5)

    for i, quote in enumerate(quotes):
        print(f'quote {i+1}')
        print(f'quote: {quote}')

        print(f'encoded: {encode(quote)}')
        print(f'decoded: {decode(encode(quote))}')
        print('-----')

    print('-----')
    print('User Input')
    print('-----')
    quote = input('quote: ')
    try:
        print(f'encoded: {encode(quote)}')
        print(f'decoded: {decode(encode(quote))}')
    except ValueError as error:
        print(error)
