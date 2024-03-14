def encode_1MM(number):
    encoded = ''
    while number > 0:
        encoded = baseX.b64encode(number % X).decode().replace('+', '~').replace('/', '\\').replace('=', '|').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a').replace('b', 'B').replace('B', 'b') + encoded
        number //= X
    return encoded

def decode_1MM(encoded):
    decoded = 0
    for i, c in enumerate(reversed(encoded)):
        decoded += baseX.b64decode(c.replace('~', '+').replace('\\', '/').replace('|', '=').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a').replace('b', 'B').replace('B', 'b').encode()) * X**i
    return decoded

What changed?

The code now supports two additional characters for encoding and decoding, 'b' and 'B'. This allows for a minimum of two characters in the alphabet of the code for no data loss.

How many letters in our alphabet?

At least two letters, 'b' and 'B'. Depending on the size of the base X, the alphabet size could be larger.







def encode_1MM(number):
    encoded = ''
    while number > 0:
        encoded = baseX.b64encode(number % X).decode().replace('+', '~').replace('/', '\\').replace('=', '|').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a').replace('B', 'b').replace('b', 'B') + encoded
        number //= X
    return encoded

def decode_1MM(encoded):
    decoded = 0
    for i, c in enumerate(reversed(encoded)):
        decoded += baseX.b64decode(c.replace('~', '+').replace('\\', '/').replace('|', '=').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a').replace('B', 'b').replace('b', 'B').encode()) * X**i
    return decoded