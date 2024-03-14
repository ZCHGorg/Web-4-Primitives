def encode_1MM(number):
    if not isinstance(number, int):
        number = ''.join([str(baseX.b64decode(c.replace('~', '+').replace('\\', '/').replace('|', '=').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a').replace('B', 'b').replace('b', 'B').replace('C', 'c').replace('c', 'C').replace('d', 'D').replace('D', 'd').encode())) for c in number])
        
    encoded = ''
    while number > 0:
        #Check for repeating characters
        encoded_char = baseX.b64encode(number % X).decode()
        if encoded_char != encoded[:len(encoded_char)]:
            encoded = encoded_char.replace('+', '~').replace('/', '\\').replace('=', '|').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a').replace('B', 'b').replace('b', 'B').replace('C', 'c').replace('c', 'C').replace('d', 'D').replace('D', 'd') + encoded
        number //= X
    return encoded

def decode_1MM(encoded):
    if not isinstance(encoded, int):
        encoded = ''.join([str(baseX.b64decode(c.replace('~', '+').replace('\\', '/').replace('|', '=').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a').replace('B', 'b').replace('b', 'B').replace('C', 'c').replace('c', 'C').replace('d', 'D').replace('D', 'd').encode())) for c in encoded])
    decoded = 0
    for i, c in enumerate(reversed(encoded)):
        decoded += int(c) * X**i
    return decoded

The output has repeating numbers and letters which can be compressed.  The compression can occur by simply running through the algorithm again.  The number of passes can be determined by checking the before and after output size to determine whether another increment of passes is helpful