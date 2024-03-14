import hashlib
import os

def generate_random_number(seed=None, algorithm=None):
    if algorithm is None:
        algorithm = hashlib.sha256()
    if seed is None:
        seed = int.from_bytes(os.urandom(8), byteorder="big")
    algorithm.update(seed.to_bytes(8, byteorder="big"))
    return int.from_bytes(algorithm.digest(), byteorder="big")

def encode_baseX_hybrid_v3(input_string, base, alphabet, seed=None, algorithm=None):
    encoded = ""
    number = 0
    for char in input_string:
        number = number * 256 + ord(char)
    random_key = generate_random_number(seed=seed, algorithm=algorithm)
    number = number ^ random_key
    for multiplier in range(0, float('inf')):
        baseX = base ** multiplier
        if number > 0:
            encoded = alphabet[number % baseX] + encoded
            number //= baseX
    encoded = hex(random_key)[2:] + encoded
    return encoded

def decode_baseX_hybrid_v3(input_string, base, alphabet, seed=None, algorithm=None):
    decoded = ""
    random_key = int(input_string[:64], 16)
    input_string = input_string[64:]
    number = 0
    for char in input_string:
        number = number * len(alphabet) + alphabet.index(char)
    number = number ^ random_key
    for multiplier in range(0, float('inf')):
        baseX = base ** multiplier
        if number > 0:
            decoded = chr(number % baseX) + decoded
            number //= baseX
    return decoded
