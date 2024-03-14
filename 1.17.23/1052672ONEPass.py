import string

alphabet = string.ascii_letters + string.digits + string.punctuation
modulo_value = 1052672

def encode_baseX(input_string):
    encoded = ""
    for char in input_string:
        position = alphabet.index(char)
        encoded += str(position).zfill(len(str(len(alphabet))))
    return encoded

def decode_baseX(input_string):
    decoded = ""
    for i in range(0, len(input_string), len(str(len(alphabet)))):
        position = int(input_string[i:i+len(str(len(alphabet)))])
        decoded += alphabet[position]
    return decoded

def encode_baseX(input_string, alphabet_size=1052672, base_size=256, alphabet_multiplier=1, base_multiplier=1):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    alphabet = alphabet[:alphabet_size] * alphabet_multiplier
    encoded = ""
    number = 0
    for char in input_string:
        number = number * len(alphabet) + alphabet.index(char)
    while number > 0:
        encoded = alphabet[number % (base_size ** base_multiplier)] + encoded
        number //= (base_size ** base_multiplier)
    return encoded

def decode_baseX(input_string):
    alphabet_size, base_size, alphabet_multiplier, base_multiplier = optimize_baseX(input_string)
    alphabet = string.ascii_letters + string.digits + string.punctuation
    alphabet = alphabet[:alphabet_size] * alphabet_multiplier
    decoded = ""
    number = 0
    for char in input_string:
        number = number * (base_size ** base_multiplier) + alphabet.index(char)
    for multiplier in range(0, float('inf')):
        baseX = len(alphabet) ** multiplier
        if number > 0:
            decoded = chr(number % baseX) + decoded
            number //= baseX
    return decoded

def optimize_baseX(input_string):
    best_size = float('inf')
    best_alphabet_size = 0
    best_base_size = 0
    best_alphabet_multiplier = 0
    best_base_multiplier = 0
    
    input_size = len(input_string)
    
    for alphabet_size in range(1, len(string.ascii_letters + string.digits + string.punctuation) + 1):
        for base_size in range(2, 257):
            for alphabet_multiplier in range(1, 10):
                for base_multiplier in range(1, 10):
                    encoded = encode_baseX(input_string, alphabet_size, base_size, alphabet_multiplier, base_multiplier)
                    if len(encoded) < best_size:
                        best_size = len(encoded)
                        best_alphabet_size = alphabet_size
                        best_base_size = base_size
                        best_alphabet_multiplier = alphabet_multiplier
                        best_base_multiplier = base_multiplier
                        
    # If the input size is small, we can decrease the alphabet size and base size
    if input_size < 100:
        best_alphabet_size = int(best_alphabet_size * 0.5)
        best_base_size = int(best_base_size * 0.5)
    # If the input size is large, we can increase the alphabet size and base size
    elif input_size > 1000:
        best_alphabet_size = int(best_alphabet_size * 1.5)
        best_base_size = int(best_base_size * 1.5)
    
    return best_alphabet_size, best_base_size, best_alphabet_multiplier, best_base_multiplier