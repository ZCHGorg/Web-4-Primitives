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

The paragraph, for example, "Starlight 39 for sale in United Kingdom for £74,900
We know Betelgeuse really well, having sailed her as our demonstrator andwe fitted well selected extras for the first discerning owner.
Blessed with two successive careful owners, Betelgeuse is now close to her original condition, with many upgrades.
A reconditioned Mermaid Meteor 56 hp engine, fitted 2008 with Darglo feathering prop 2009
Full upgrade electronics, Raymarine ST60 and 70 c/w Raymarine autopilot 2009" could be represented by only one character within our encoding using mapping.  It is not practicle to create a large database of mappings.  The mappings should be created on the fly instead.  The character chosen to represent the paragraph is the number 6, which would be encoded as "3qh|".

Ok, show me the code.

def encode_paragraph(paragraph):
    # Create a mapping of each character in the paragraph to a unique number
    char_map = {char: i for i, char in enumerate(paragraph)}

    # Encode each character using the mapping
    encoded = [encode_1MM(char_map[char]) for char in paragraph]

    return ''.join(encoded)

def decode_paragraph(encoded):
    # Decode each character from the encoded string
    decoded = [decode_1MM(encoded[i:i+4]) for i in range(0, len(encoded), 4)]

    # Create a reverse mapping of the original characters
    char_map = {i: char for i, char in enumerate(paragraph)}

    # Return the decoded string with the characters from the original mapping
    return ''.join([char_map[i] for i in decoded])