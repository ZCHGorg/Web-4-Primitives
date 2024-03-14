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