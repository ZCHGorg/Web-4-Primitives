import base64

def encode_1MM(number):
    encoded = ''
    while number > 0:
        encoded = base64.b64encode(number % 1052672).decode() + encoded
        number //= 1052672
    return encoded

def decode_1MM(encoded):
    decoded = 0
    for i, c in enumerate(reversed(encoded)):
        decoded += base64.b64decode(c.encode()) * 1052672**i
    return decoded

ABCDEFGH --> !_~|\| (ABCDEFGH --> base64.b64encode(ABCDEFGH).decode('utf-8') --> !_~|\|)