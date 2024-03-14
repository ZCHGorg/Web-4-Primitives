what does this code do?

import base64

def encode_1MM(number):
    encoded = ''
    while number > 0:
        encoded = base64.b64encode(number % 1052672).decode().replace('+', '~').replace('/', '\\').replace('=', '|') + encoded
        number //= 1052672
    return encoded

def decode_1MM(encoded):
    decoded = 0
    for i, c in enumerate(reversed(encoded)):
        decoded += base64.b64decode(c.replace('~', '+').replace('\\', '/').replace('|', '=').encode()) * 1052672**i
    return decoded

please restore middlemen baseX into this code

def encode_1MM(number):
    encoded = ''
    while number > 0:
        encoded = baseX.b64encode(number % 1052672).decode().replace('+', '~').replace('/', '\\').replace('=', '|') + encoded
        number //= 1052672
    return encoded

def decode_1MM(encoded):
    decoded = 0
    for i, c in enumerate(reversed(encoded)):
        decoded += baseX.b64decode(c.replace('~', '+').replace('\\', '/').replace('|', '=').encode()) * 1052672**i
    return decoded

add support for letters as an input to this code please

def encode_1MM(number):
    encoded = ''
    while number > 0:
        encoded = baseX.b64encode(number % 1052672).decode().replace('+', '~').replace('/', '\\').replace('=', '|').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.') + encoded
        number //= 1052672
    return encoded

def decode_1MM(encoded):
    decoded = 0
    for i, c in enumerate(reversed(encoded)):
        decoded += baseX.b64decode(c.replace('~', '+').replace('\\', '/').replace('|', '=').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').encode()) * 1052672**i
    return decoded

change support of baseX to any number from 0 to infinity

def encode_1MM(number):
    encoded = ''
    while number > 0:
        encoded = baseX.b64encode(number % X).decode().replace('+', '~').replace('/', '\\').replace('=', '|').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.') + encoded
        number //= X
    return encoded

def decode_1MM(encoded):
    decoded = 0
    for i, c in enumerate(reversed(encoded)):
        decoded += baseX.b64decode(c.replace('~', '+').replace('\\', '/').replace('|', '=').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').encode()) * X**i
    return decoded

add support for base having any number from negative infinity to infinity in this code

def encode_1MM(number):
    encoded = ''
    while number > 0:
        encoded = baseX.b64encode(number % X).decode().replace('+', '~').replace('/', '\\').replace('=', '|').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#') + encoded
        number //= X
    return encoded

def decode_1MM(encoded):
    decoded = 0
    for i, c in enumerate(reversed(encoded)):
        decoded += baseX.b64decode(c.replace('~', '+').replace('\\', '/').replace('|', '=').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').encode()) * X**i
    return decoded

add support for base having letters in this code

def encode_1MM(number):
    encoded = ''
    while number > 0:
        encoded = baseX.b64encode(number % X).decode().replace('+', '~').replace('/', '\\').replace('=', '|').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a') + encoded
        number //= X
    return encoded

def decode_1MM(encoded):
    decoded = 0
    for i, c in enumerate(reversed(encoded)):
        decoded += baseX.b64decode(c.replace('~', '+').replace('\\', '/').replace('|', '=').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a').encode()) * X**i
    return decoded

how many letters are in the alphabet of this code?

Please restore the alphabet size to 1052672 in this code:

def encode_1MM(number):
    encoded = ''
    while number > 0:
        encoded = baseX.b64encode(number % 1052672).decode().replace('+', '~').replace('/', '\\').replace('=', '|').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a') + encoded
        number //= 1052672
    return encoded

def decode_1MM(encoded):
    decoded = 0
    for i, c in enumerate(reversed(encoded)):
        decoded += baseX.b64decode(c.replace('~', '+').replace('\\', '/').replace('|', '=').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a').encode()) * 1052672**i
    return decoded

Allow the alphabet size to increase if baseX is larger than 1052672

def encode_1MM(number):
    encoded = ''
    while number > 0:
        encoded = baseX.b64encode(number % X).decode().replace('+', '~').replace('/', '\\').replace('=', '|').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a') + encoded
        number //= X
    return encoded

def decode_1MM(encoded):
    decoded = 0
    for i, c in enumerate(reversed(encoded)):
        decoded += baseX.b64decode(c.replace('~', '+').replace('\\', '/').replace('|', '=').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a').encode()) * X**i
    return decoded

restrict a given letter in the alphabet to 1 character

def encode_1MM(number):
    encoded = ''
    while number > 0:
        encoded = baseX.b64encode(number % X).decode().replace('+', '~').replace('/', '\\').replace('=', '|').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a').replace('b', '') + encoded
        number //= X
    return encoded

def decode_1MM(encoded):
    decoded = 0
    for i, c in enumerate(reversed(encoded)):
        decoded += baseX.b64decode(c.replace('~', '+').replace('\\', '/').replace('|', '=').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a').replace('b', '').encode()) * X**i
    return decoded

what did you change?

I changed the code to add support for baseX having any number from 0 to infinity, add support for baseX having letters, and restrict a given letter in the alphabet to 1 character.