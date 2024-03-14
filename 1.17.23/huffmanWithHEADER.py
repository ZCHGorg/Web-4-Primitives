import string
from collections import Counter
from heapq import heappush, heappop, heapify
from cmath import exp, pi
import json

alphabet = string.ascii_letters + string.digits + string.punctuation
modulo_value = 1048576

def build_huffman_tree(input_string):
    # Count the frequency of each character
    freq = Counter(input_string)
    # Create a priority queue of leaves
    heap = [[weight, [char, ""]] for char, weight in freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

def encode_huffman(input_string,huffman_tree):
    encoded = ""
    for char in input_string:
        for pair in huffman_tree:
            if char == pair[0]:
                encoded += pair[1]
                break
    return encoded

def decode_huffman(encoded,huffman_tree):
    decoded = ""
    while encoded:
        for pair in huffman_tree:
            if encoded.startswith(pair[1]):
                decoded += pair[0]
                encoded = encoded[len(pair[1]):]
                break
    return decoded

import json

def encode_baseX_with_header(input_string, alphabet_size=1048576, base_size=256, alphabet_multiplier=1, base_multiplier=1):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    alphabet = alphabet[:alphabet_size] * alphabet_multiplier
    huffman_tree = build_huffman_tree(alphabet)
    encoded = ""
    number = 0
    for char in input_string:
        encoded_char = encode_huffman(char, huffman_tree)
        x = alphabet.index(char)
        number += exp(1j * x * pi / len(alphabet)) * (base_size ** base_multiplier)
    while number > 0:
        encoded = encoded_char + encoded
        number //= (base_size ** base_multiplier)
    # Serialize the Huffman tree to JSON and add it to the encoded data as the header
    header = json.dumps(huffman_tree)
    encoded = header + encoded
    return encoded

def decode_baseX_with_header(encoded_data, alphabet_size=1048576, base_size=256, alphabet_multiplier=1, base_multiplier=1):
    # Extract the header (the Huffman tree) from the encoded data
    header_size = encoded_data.index("}") + 1 # Assumes the Huffman tree is serialized to JSON
    header = json.loads(encoded_data[:header_size])
    encoded = encoded_data[header_size:]
    alphabet = string.ascii_letters + string.digits + string.punctuation
    alphabet = alphabet[:alphabet_size] * alphabet_multiplier
    huffman_tree = header
    decoded = ""
    number = 0
    for char in encoded:
        decoded_char = decode_huffman(char, huffman_tree)
        x = alphabet.index(decoded_char)
        number += exp(1j * x * pi / len(alphabet)) * (base_size ** base_multiplier)
    for multiplier in range(0, float('inf')):
        baseX = len(alphabet) ** multiplier
        if number > 0:
            decoded = decoded_char + decoded
            number //= baseX
    return decoded