# Encode the input string
string = 'all dogs go to heaven'
input_string = 'all dogs go to heaven'
encoded_string, base, alphabet = encode_baseX(input_string)



# Store the base and alphabet used for encoding
stored_base = base
stored_alphabet = alphabet

# Decode the output string
decoded_string = decode_baseX(encoded_string, stored_base, stored_alphabet)

# Check that the original string and decoded string are the same
assert decoded_string == input_string

def encode_baseX(input_string):
    encoded = ""
    number = 0
    for char in input_string:
        number = number * 256 + ord(char)

    min_base = 0
    max_base = float('inf')
    min_alphabet_multiplier = 0
    max_alphabet_multiplier = float('inf')
    standard_alphabet = string.ascii_uppercase

    for base in range(min_base, max_base + 1):
        for alphabet_multiplier in range(min_alphabet_multiplier, max_alphabet_multiplier + 1):
            alphabet = standard_alphabet * alphabet_multiplier
            for multiplier in range(0, float('inf')):
                baseX = base ** multiplier
                if number > 0:
                    encoded = alphabet[number % baseX] + encoded
                    number //= baseX
    return encoded

def decode_baseX(input_string, base, alphabet):
    decoded = ""
    number = 0
    for char in input_string:
        number = number * len(alphabet) + alphabet.index(char)

    for multiplier in range(0, float('inf')):
        baseX = base ** multiplier
        if number > 0:
            decoded = chr(number % baseX) + decoded
            number //= baseX
    return decoded