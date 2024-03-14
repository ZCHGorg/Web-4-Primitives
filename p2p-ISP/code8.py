import string
from cmath import exp, pi

alphabet = string.ascii_letters + string.digits + string.punctuation
modulo_value = 1048576

def encode_baseX(input_string, alphabet_size=1048576, base_size=256, alphabet_multiplier=1, base_multiplier=1):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    alphabet = alphabet[:alphabet_size] * alphabet_multiplier
    encoded = ""
    number = 0
    for char in input_string:
        number += exp(alphabet.index(char)*(2j*pi/len(alphabet)))
    while number > 0:
        encoded = alphabet[int(number.real*len(alphabet)/(2*pi)) % (base_size ** base_multiplier)] + encoded
        number /= (base_size ** base_multiplier)
    return encoded

def decode_baseX(input_string):
    alphabet_size, base_size, alphabet_multiplier, base_multiplier = optimize_baseX(input_string)
    alphabet = string.ascii_letters + string.digits + string.punctuation
    alphabet = alphabet[:alphabet_size] * alphabet_multiplier
    decoded = ""
    number = 0
    for char in input_string:
        number += exp(alphabet.index(char)*(2j*pi/base_size**base_multiplier))
    for multiplier in range(0, float('inf')):
        baseX = len(alphabet) ** multiplier
        if number > 0:
            decoded = chr(int(number.real*len(alphabet)/(2*pi)) % baseX) + decoded
            number /= baseX
    return decoded

def optimize_baseX(input_string):
    best_size = float('inf')
    best_alphabet_size = 0
    best_base_size = 0
    best_alphabet_multiplier = 0
    best_base_multiplier = 0

    input_size = len(input_string)

    for alphabet_size in range(-float('inf'), float('inf')):
        for base_size in range(-float('inf'), float('inf')):
            for alphabet_multiplier in range(-float('inf'), float('inf')):
                for base_multiplier in range(-float('inf'), float('inf')):
                    encoded = encode_baseX(input_string, alphabet_size, base_size, alphabet_multiplier, base_multiplier)
                    if len(encoded) < best_size:
                        best_size = len(encoded)
                        best_alphabet_size = alphabet_size
                        best_base_size = base_size
                        best_alphabet_multiplier = alphabet_multiplier
                        best_base_multiplier = base_multiplier
    return best_alphabet_size, best_base_size, best_alphabet_multiplier, best_base_multiplier
