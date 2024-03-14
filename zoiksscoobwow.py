def encode_1MM_compress(number):
    if not isinstance(number, int):
        number = ''.join([str(baseX.b64decode(c.replace('~', '+').replace('\\', '/').replace('|', '=').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a').replace('B', 'b').replace('b', 'B').replace('C', 'c').replace('c', 'C').replace('d', 'D').replace('D', 'd').encode())) for c in number])
    #Encode the number
    encoded = ''
    while number > 0:
        encoded_char = baseX.b64encode(number % X).decode()
        if encoded_char != encoded[:len(encoded_char)]:
            encoded = encoded_char.replace('+', '~').replace('/', '\\').replace('=', '|').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a').replace('B', 'b').replace('b', 'B').replace('C', 'c').replace('c', 'C').replace('d', 'D').replace('D', 'd') + encoded
        number //= X
    #Compress the output
    compressed_encoded = ''
    last_char = ''
    count = 0
    for char in encoded:
        if char == last_char:
            count += 1
        else:
            if count > 0:
                compressed_encoded += str(count+1)
            compressed_encoded += char
            last_char = char
            count = 0
    if count > 0:
        compressed_encoded += str(count+1)
    return compressed_encoded

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
    return decoded

The code above allows for one pass of compression. If multiple passes of compression are desired, the encode_1MM_compress and decode_1MM_compress functions can be used in a loop to achieve the desired number of passes.  The number of passes should be determined automatically based on the size of the anticipated output.  The size before and after each pass can be compared and the optimal number of passes can be determined