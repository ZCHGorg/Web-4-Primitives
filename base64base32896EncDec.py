import base64

alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()-_+=[{]};:',\"<>?/\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1A\x1B\x1C\x1D\x1E\x1F\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2A\x2B\x2C\x2D\x2E\x2F\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3A\x3B\x3C\x3D\x3E\x3F\x40\x41"

def encode(number):
    encoded = ''
    while number > 0:
        encoded = alphabet[number % 4112] + encoded
        number //= 4112
    return encoded

def decode(encoded):
    decoded = 0
    for i, c in enumerate(reversed(encoded)):
        decoded += alphabet.index(c) * 4112**i
    return decoded

def encode_64(number):
    encoded = ''
    while number > 0:
        encoded = base64.b64encode(number % 4112).decode() + encoded
        number //= 4112
    return encoded

def decode_64(encoded):
    decoded = 0
    for i, c in enumerate(reversed(encoded)):
        decoded += base64.b64decode(c.encode()) * 4112**i
    return decoded

def encode_8224(number):
    encoded = ''
    while number > 0:
        encoded = alphabet[number % 8224] + encoded
        number //= 8224
    return encoded

def decode_8224(encoded):
    decoded = 0
    for i, c in enumerate(reversed(encoded)):
        decoded += alphabet.index(c) * 8224**i
    return decoded

def encode_16448(number):
    encoded = ''
    while number > 0:
        encoded = alphabet[number % 16448] + encoded
        number //= 16448
    return encoded

def decode_16448(encoded):
    decoded = 0
    for i, c in enumerate(reversed(encoded)):
        decoded += alphabet.index(c) * 16448**i
    return decoded

def encode_32896(number):
    encoded = ''
    while number > 0:
        encoded = alphabet[number % 32896] + encoded
        number //= 32896
    return encoded

def decode_32896(encoded):
    decoded = 0
    for i, c in enumerate(reversed(encoded)):
        decoded += alphabet.index(c) * 32896**i
    return decoded