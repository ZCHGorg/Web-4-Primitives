import base64
import math
import random
from collections import Counter

def generate_alphabet(string, min_output_size):
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

def generate_loop_ranges(string, min_output_size):
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

#example usage
string = 'da bears'
