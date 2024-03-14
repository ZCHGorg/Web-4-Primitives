import math
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
    #count the frequency and position of characters in the input string
    char_count = dict()
    for index, char in enumerate(string):
        if char in char_count:
            char_count[char]['count'] += 1
            char_count[char]['positions'].append(index)
        else:
            char_count[char] = {'count': 1, 'positions': [index]}
    #sort the characters based on their frequency and position
    sorted_characters = sorted(char_count.items(), key=lambda x: (x[1]['count'], x[1]['positions'][0]), reverse=True)
    #generate the alphabet on-the-fly
    alphabet = [x[0] for x in sorted_characters]
    #implement the rest of the code
    for alphabet_multiplier in range(1, len(alphabet) + 1):
        for baseX_multiplier in range(1, len(alphabet) + 1):
            for baseX in range(2, len(alphabet) + 1):
                encoded = encode_baseX(string, alphabet, alphabet_multiplier, baseX_multiplier)
                code = encode_code(alphabet, baseX, alphabet_multiplier, baseX_multiplier)
                count = len(encoded) - len(string)
                if abs(count) < min_count:
                    min_count = abs(count)
                    optimal_code = code
    #decode the code to get the optimal values of alphabet, baseX, alphabet multiplier, and baseX multiplier
    optimal_alphabet, optimal_baseX, optimal_alphabet_multiplier, optimal_baseX_multiplier = decode_code(optimal_code)
    return optimal_alphabet, optimal_baseX, optimal_alphabet_multiplier, optimal_baseX_multiplier

def encode_code(alphabet, baseX, alphabet_multiplier, baseX_multiplier):
    code = (alphabet * alphabet_multiplier) + (baseX * baseX_multiplier)
    return code

def decode_code(code):
    alphabet_multiplier = code // 100
    baseX_multiplier = code % 100 // 10
    baseX = code % 10
    alphabet = code // (alphabet_multiplier * baseX_multiplier * baseX)
    return alphabet, baseX, alphabet_multiplier, baseX_multiplier