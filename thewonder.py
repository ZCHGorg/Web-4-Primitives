import base64
import collections
import math
import random
import sys

X = 1052672

def encode_1MM(number, target_size=None):
    if not isinstance(number, int):
        number = ''.join([str(baseX.b64decode(c.replace('~', '+').replace('\\', '/').replace('|', '=').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a').replace('B', 'b').replace('b', 'B').replace('C', 'c').replace('c', 'C').replace('d', 'D').replace('D', 'd').encode())) for c in number])

    # Add information about the number of passes used for compression
    encoded = "1MM|"
    current_size = len(encoded)
    passes = 0
    while current_size > target_size:
        # Check for repeating characters
        encoded_char = baseX.b64encode(number % X).decode()
        if encoded_char != encoded[:len(encoded_char)]:
            encoded = encoded_char.replace('+', '~').replace('/', '\\').replace('=', '|').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a').replace('B', 'b').replace('b', 'B').replace('C', 'c').replace('c', 'C').replace('d', 'D').replace('D', 'd') + encoded
        number //= X
        current_size = len(encoded)
        passes += 1
    return f"{passes}| {encoded}"

def decode_1MM(encoded, target_size=None):
    if not isinstance(encoded, int):
        encoded = ''.join([str(baseX.b64decode(c.replace('~', '+').replace('\\', '/').replace('|', '=').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a').replace('B', 'b').replace('b', 'B').replace('C', 'c').replace('c', 'C').replace('d', 'D').replace('D', 'd').encode())) for c in encoded])

    # Check for the sentinel value at the beginning of the encoded string
    if not encoded.startswith("1MM|"):
        # Input string was not encoded using this approach, return the original string
        return encoded
    
    # Extract the number of passes used for compression
    passes = int(encoded[:encoded.index("|")])
    encoded = encoded[encoded.index("|") + 1:]
    
    decoded = 0
    for i, c in enumerate(reversed(encoded)):
        decoded += int(c) * X**i

    # Decompress by running the decoding algorithm multiple times until the desired size is reached
    while len(decoded) > target_size:
        decoded = decode_1MM(decoded, target_size)
        passes -= 1

    return decoded