import base64
import math
import random
from collections import Counter
import numpy as np

def generate_alphabet(string, min_output_size=1):
    char_count = dict()
    for index, char in enumerate(string):
        if char in char_count:
            char_count[char]['count'] += 1
            char_count[char]['positions'].append(index)
        else:
            char_count[char] = {'count': 1, 'positions': [index]}
    sorted_characters = sorted(char_count.items(), key=lambda x: (x[1]['count'], x[1]['positions'][0]), reverse=True)
    alphabet = [x[0] for x in sorted_characters]
    alphabet = alphabet[:min_output_size]
    return alphabet

def generate_loop_ranges(string, min_output_size=1):
    population_size = 100
    num_generations = 100
    population = []
    for _ in range(population_size):
        population.append(np.random.randint(1, len(alphabet), size=(3,)))
    for _ in range(num_generations):
        population = sorted(population, key=lambda x: fitness(string, encode_baseX(string, alphabet, x[0], x[1], x[2]), x[0], x[1], x[2]))
        population = population[:population_size//2]
        for _ in range(population_size//2):
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = np.zeros((3,))
            for k in range(3):
                child[k] = parent1[k] if random.random() < 0.5 else parent2[k]
            population.append(child)
    return population[0]

def fitness(string, encoded, alphabet_multiplier, baseX_multiplier):
    return abs(len(encoded) - len(string)) + abs(entropy(string) - entropy(encoded))

def entropy(string):
    p, lns = Counter(string), float(len(string))
    return -sum( count/lns * math.log(count/lns, 2) for count in p.values())

def encode_code(alphabet, baseX, alphabet_multiplier, baseX_multiplier):
    code = alphabet + '-' + str(baseX) + '-' + str(alphabet_multiplier) + '-' + str(baseX_multiplier)
    encoded_code = base64.b64encode(code.encode())
    return encoded_code.decode()

def decode_code(encoded_code):
    decoded_code = base64.b64decode(encoded_code.encode()).decode()
    alphabet, baseX, alphabet_multiplier, baseX_multiplier = decoded_code.split('-')
    return alphabet, int(baseX), int(alphabet_multiplier), int(baseX_multiplier)

def encode_baseX(string, alphabet, alphabet_multiplier, baseX_multiplier):
    encoded = ''
    for char in string:
        encoded += alphabet[alphabet.index(char) * alphabet_multiplier % len(alphabet)]
    return encoded

def encode_baseX(string, alphabet, alphabet_multiplier, baseX_multiplier):
    encoded = ''
    for char in string:
        encoded += alphabet[alphabet.index(char) * alphabet_multiplier % len(alphabet)]
    return encoded

def decode_baseX(encoded, alphabet, alphabet_multiplier, baseX_multiplier):
    decoded = ""
    for char in encoded:
        decoded += alphabet[alphabet.index(char) // alphabet_multiplier]
    return decoded

def get_optimal_baseX(string, min_output_size):
    alphabet = generate_alphabet(string, min_output_size)
    alphabet_multiplier, baseX_multiplier, baseX = generate_loop_ranges(string, min_output_size)
    encoded = encode_baseX(string, alphabet, alphabet_multiplier, baseX_multiplier)
    code = encode_code(alphabet, baseX, alphabet_multiplier, baseX_multiplier)
    return alphabet, baseX, alphabet_multiplier, baseX_multiplier, encoded, code

X = get_optimal_baseX(string, min_output_size)

def encode_1MM(number, target_size=None):
    if not isinstance(number, int):
        number = ''.join([str(baseX.b64decode(c.replace('~', '+').replace('\\', '/').replace('|', '=').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a').replace('B', 'b').replace('b', 'B').replace('C', 'c').replace('c', 'C').replace('d', 'D').replace('D', 'd').encode())) for c in number])

    # Add information about the number of passes used for compression
    encoded = "1MM|"
    current_size = len(encoded)
    passes = 0
    while current_size > target_size:
        # Check for repeating characters
        encoded_char = baseX.b64encode(number % X).decode()
        if encoded_char != encoded[:len(encoded_char)]:
            encoded = encoded_char.replace('+', '~').replace('/', '\\').replace('=', '|').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a').replace('B', 'b').replace('b', 'B').replace('C', 'c').replace('c', 'C').replace('d', 'D').replace('D', 'd') + encoded
        number //= X
        current_size = len(encoded)
        passes += 1
    return f"{passes}| {encoded}"

def decode_1MM(encoded, target_size=None):
    if not isinstance(encoded, int):
        encoded = ''.join([str(baseX.b64decode(c.replace('~', '+').replace('\\', '/').replace('|', '=').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a').replace('B', 'b').replace('b', 'B').replace('C', 'c').replace('c', 'C').replace('d', 'D').replace('D', 'd').encode())) for c in encoded])

    # Check for the sentinel value at the beginning of the encoded string
    if not encoded.startswith("1MM|"):
        # Input string was not encoded using this approach, return the original string
        return encoded
    
    # Extract the number of passes used for compression
    passes = int(encoded[:encoded.index("|")])
    encoded = encoded[encoded.index("|") + 1:]
    
    decoded = 0
    for i, c in enumerate(reversed(encoded)):
        decoded += int(c) * X**i

    # Decompress by running the decoding algorithm multiple times until the desired size is reached
    while len(decoded) > target_size:
        decoded = decode_1MM(decoded, target_size)
        passes -= 1

    return decoded

input string = "Hello World"
min_output_size = 100

alphabet, baseX, alphabet_multiplier, baseX_multiplier, encoded, code = get_optimal_baseX(string, min_output_size)
print(alphabet, baseX, alphabet_multiplier, baseX_multiplier, encoded, code)

encoded = encode_1MM(string, min_output_size)
print(encoded)

# output = 