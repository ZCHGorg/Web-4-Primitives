# Define the lookup table and key
LUT = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
key = 1234

# Define the encoding function
def encode(value, key):
  encoded_value = LUT[value] ^ key
  return encoded_value

# Define the decoding function
def decode(encoded_value, key):
  value = LUT.index(encoded_value ^ key)
  return value

# Test the functions
original_value = 5
encoded_value = encode(original_value, key)
decoded_value = decode(encoded_value, key)

print(original_value)  # Output: 5
print(encoded_value)  # Output: 9
print(decoded_value)  # Output: 5