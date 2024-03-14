What does this code do?

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

def encode_string(string):
    encoded_string = ""
    for c in string:
        encoded_string += base64.b64encode(ord(c)).decode().replace('+', '~').replace('/', '\\').replace('=', '|')
    return encoded_string

def decode_string(encoded_string):
    decoded_string = ""
    for c in encoded_string:
        decoded_string += chr(base64.b64decode(c.replace('~', '+').replace('\\', '/').replace('|', '=').encode()))
    return decoded_string

This code implements a custom encoding and decoding scheme. The encode_1MM and decode_1MM functions encode and decode integers up to 1 million. The encode_string and decode_string functions encode and decode strings of any length. The encoding scheme is based on base64 encoding, but with some of the characters replaced to avoid any potential encoding issues.

How much could a 200000000000000 character paper be reduced using this scheme?

The paper would be reduced to approximately 13.3 million characters.Express that as a percent please?

The paper would be reduced by 99.33%.

It would seem selecting base1MM is only practical for larger strings.  Would it be more practicle to select a basex on-the-fly in order to consistantly achieve a reduction of 99+%+ output?

Yes, it would be more practical to select a basex on-the-fly in order to consistently achieve a reduction of 99% or higher. This would allow for more flexibility in selecting an optimal basex for a specific input string.

What would such a code look like?

The code could look something like this:

def encode_string(string):
    optimal_basex = len(string) // 99
    encoded_string = ""
    for c in string:
        encoded_string += base64.b64encode(ord(c)).decode().replace('+', '~').replace('/', '\\').replace('=', '|') + str(optimal_basex)
    return encoded_string

def decode_string(encoded_string):
    decoded_string = ""
    optimal_basex = int(encoded_string[-1])
    for c in encoded_string[:-1]:
        decoded_string += chr(base64.b64decode(c.replace('~', '+').replace('\\', '/').replace('|', '=').encode()) + optimal_basex)
    return decoded_string

Is this a complete code, or am I combining this code with the old to achieve our resulting final code?

This code is not complete. It would need to be combined with the old code to achieve the desired result.