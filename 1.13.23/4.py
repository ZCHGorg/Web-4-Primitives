import math
import hashlib
import os

def optimize_alphabet_frequency_entropy(input_string):
frequency = {}
for char in input_string:
if char not in frequency:
frequency[char] = 0
frequency[char] += 1
entropy = 0
for count in frequency.values():
probability = count/len(input_string)
entropy += probability * math.log(probability, 2)
# sort the characters by their frequency and then by their entropy
alphabet = ''.join(sorted(frequency, key=lambda x: (-frequency[x], entropy)))
return len(alphabet), alphabet

def int_to_baseX(num, base, alphabet):
"""Convert an integer to a string in the given base using the given alphabet"""
if num == 0:
return alphabet[0]
digits = []
while num:
    num, rem = divmod(num, base)
    digits.append(alphabet[rem])
return ''.join(reversed(digits))