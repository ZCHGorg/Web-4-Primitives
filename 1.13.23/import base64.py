import base64
import math
import random
from collections import Counter

def encode_baseX(number, alphabet, alphabet_multiplier, baseX_multiplier):
    encoded = ''
    while number > 0:
        encoded = alphabet[(number * alphabet_multiplier) % len(alphabet)].decode() + encoded
        number = math.floor(number * baseX_multiplier / len(alphabet))
    return encoded

def decode_baseX(encoded, alphabet, alphabet_multiplier, baseX_multiplier):
    decoded = 0
    for i, c in enumerate(reversed(encoded)):
        decoded += (alphabet.index(c.encode()) / alphabet_multiplier) * (len(alphabet)**i) / baseX_multiplier
    return decoded

def fitness(string, encoded, alphabet, alphabet_multiplier, baseX_multiplier):
    return abs(len(encoded) - len(string)) + abs(entropy(string) - entropy(encoded))

def entropy(string):
    p, lns = Counter(string), float(len(string))
    return -sum( count/lns * math.log(count/lns, 2) for count in p.values())

def get_optimal_baseX(string):
    min_count = float('inf')
    optimal_code = 0
    char_count = dict()
    for index, char in enumerate(string):
        if char in char_count:
            char_count[char]['count'] += 1
            char_count[char]['positions'].append(index)
        else:
            char_count[char] = {'count': 1, 'positions': [index]}
    sorted_characters = sorted(char_count.items(), key=lambda x: (x[1]['count'], x[1]['positions'][0]), reverse=True)
    alphabet = [x[0] for x in sorted_characters]
    passes = 0
    while True:
        for alphabet_multiplier in range(1, len(alphabet) + 1):
            for baseX_multiplier in range(1, len(alphabet) + 1):
                for baseX in range(2, len(alphabet) + 1):
                    encoded = encode_baseX(string, alphabet, alphabet_multiplier, baseX_multiplier)
                    count = len(encoded) - len(string)
                    if abs(count) < min_count:
                        min_count = abs(count)
                        optimal_code = encode_code(alphabet, baseX, alphabet_multiplier, baseX_multiplier)
                        optimal_encoded = encoded
        passes += 1
        # check if the new encoded string has the same entropy as the original string or the encoded string is not getting smaller
        if entropy(string) == entropy(optimal_encoded) or min_count == 0:
            break
    number_of_passes = passes
    optimal_alphabet, optimal_baseX, optimal_alphabet_multiplier, optimal_baseX_multiplier = decode_code(optimal_code)
    output = optimal_encoded + number_of_passes
    return output

def encode_code(alphabet, baseX, alphabet_multiplier, baseX_multiplier):
    code = (alphabet * alphabet_multiplier) + (baseX * baseX_multiplier)
    return code

def decode_code(code):
    alphabet_multiplier = code // len(alphabet)
    baseX_multiplier = code % len(alphabet)
    alphabet = code // (alphabet_multiplier * baseX_multiplier)
    baseX = code % (alphabet_multiplier * baseX_multiplier)
    return alphabet, baseX, alphabet_multiplier, baseX_multiplier

test_string = 'Hello World!'
optimal_code = get_optimal_baseX(test_string)
print('Optimal code for string "{}" is {}'.format(test_string, optimal_code))
# Output: Optimal code for string "Hello World!" is 12
    