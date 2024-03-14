What's missing?

def encode_1MM_compress(number):
    if not isinstance(number, int):
        number = ''.join([str(baseX.b64decode(c.replace('~', '+').replace('\\', '/').replace('|', '=').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a').replace('B', 'b').replace('b', 'B').replace('C', 'c').replace('c', 'C').replace('d', 'D').replace('D', 'd').encode())) for c in number])
    #Encode the number
    encoded = ''
    while number > 0:
        encoded_char = baseX.b64encode(number % X).decode()
        if encoded_char != encoded[:len(encoded_char)]:
            encoded = encoded_char.replace('+', '~').replace('/', '\\').replace('=', '

def decode_1MM_compress(compressed_encoded):
    if not isinstance(compressed_encoded, int):
        compressed_encoded = ''.join([str(baseX.b64decode(c.replace('~', '+').replace('\\', '/').replace('|', '=').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a').replace('B', 'b').replace('b', 'B').replace('C', 'c').replace('c', 'C').replace('d', 'D').replace('D', 'd').encode())) for c in compressed_encoded])
    #Decode the number
    decoded = 0
    count = 0
    for char in reversed(compressed_encoded):
        if char.isdigit():
            count = int(char)-1
        else:
            decoded += int(char) * X**count
            count = 0