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

The result of this encoding is base1MM output.  However, the resulting output is a string which is sometimes too long.  For this reason, we need to add functions which use the position of each letter within the output string, as well as the number of character within the output string, to further reduce the length of our output.

def encode_1MM_position(number):
    encoded = ''
    while number > 0:
        encoded = base64.b64encode(number % 1052672).decode().replace('+', '~').replace('/', '\\').replace('=', '|')[:i] + encoded
        number //= 1052672
        i = len(encoded)
    return encoded

def decode_1MM_position(encoded):
    decoded = 0
    i = 0
    for c in reversed(encoded):
        decoded += base64.b64decode(c.replace('~', '+').replace('\\', '/').replace('|', '=').encode()) * 1052672**i
        i += 1
    return decoded

The result of this encoding is base1MM position output. This output can be further reduced by using the number of characters in the encoded string as a factor in the encoding process.

def encode_1MM_position_character_count(number):
    encoded = ''
    while number > 0:
        encoded = base64.b64encode(number % 1052672).decode().replace('+', '~').replace('/', '\\').replace('=', '|')[:i + len(encoded)] + encoded
        number //= 1052672
        i = len(encoded)
    return encoded

def decode_1MM_position_character_count(encoded):
    decoded = 0
    i = 0
    for c in reversed(encoded):
        decoded += base64.b64decode(c.replace('~', '+').replace('\\', '/').replace('|', '=').encode()) * 1052672**(i + len(encoded))
        i += 1
    return decoded

The result of this encoding is base1MM position character count output. This output is much more concise and can be used to represent large numbers in a smaller amount of space.

The sentence, for example, "All dogs go to heaven" could be represented by only one character within our encoding using, for example, mapping.  As well as other techniques.  It is not practicle to create a large data set of mappings, this in mind.  Instead, we should create a mapping scheme which is called upon on demand to achieve the desired result of further reducing the size of our output.  This can be done by creating a short series of functions which will convert the output of the encode_1MM_position_character_count function into a string of more concise characters.

Correct, show me the code.

def encode_1MM_position_character_count_mapping(number):
    # Generate a mapping of characters to numbers
    mapping = {}
    for i in range(0, 10):
        mapping[str(i)] = i
    for i in range(0, 26):
        mapping[chr(ord('a') + i)] = i + 10
    encoded = ''
    while number > 0:
        encoded = mapping[base64.b64encode(number % 1052672).decode().replace('+', '~').replace('/', '\\').replace('=', '|')[:i + len(encoded)]] + encoded
        number //= 1052672
        i = len(encoded)
    return encoded

def decode_1MM_position_character_count_mapping(encoded):
    # Generate a mapping of characters to numbers
    mapping = {}
    for i in range(0, 10):
        mapping[str(i)] = i
    for i in range(0, 26):
        mapping[chr(ord('a') + i)] = i + 10
    decoded = 0
    i = 0
    for c in reversed(encoded):
        decoded += base64.b64decode(mapping[c].replace('~', '+').replace('\\', '/').replace('|', '=').encode()) * 1052672**(i + len(encoded))
        i += 1
    return decoded