# Define the set of base1024 characters to be used for encoding and decoding
chars = [chr(i) for i in range(1024)]

# Define the set of rules for encoding and decoding data using imaginary numbers
def encode(data):
  # Convert the data to a complex number using imaginary numbers
  complex_num = complex(data)
  
  # Encode the real and imaginary parts of the complex number using the base1024 characters
  real_part_encoded = encode_number(complex_num.real, chars)
  imag_part_encoded = encode_number(complex_num.imag, chars)
  
  # Concatenate the encoded real and imaginary parts and return the result
  return real_part_encoded + imag_part_encoded

def decode(encoded_data):
  # Split the encoded data into the encoded real and imaginary parts
  real_part_encoded = encoded_data[:len(encoded_data)//2]
  imag_part_encoded = encoded_data[len(encoded_data)//2:]
  
  # Decode the real and imaginary parts using the base1024 characters
  real_part = decode_number(real_part_encoded, chars)
  imag_part = decode_number(imag_part_encoded, chars)
  
  # Convert the decoded real and imaginary parts to a complex number and return the result
  return complex(real_part, imag_part)

# Define a helper function for encoding and decoding numbers using the base1024 characters
def encode_number(number, base_chars):
  # Handle the special case of 0
  if number == 0:
    return base_chars[0]
  
  # Initialize the list of encoded digits
  encoded_digits = []
  
  # Divide the number by the base and add the remainder to the list of encoded digits
  while number > 0:
    encoded_digits.append(base_chars[number % 1024])
    number //= 1024
  
  # Reverse the list of encoded digits and return the result
  return ''.join(reversed(encoded_digits))

def decode_number(encoded_number, base_chars):
  # Initialize the decoded number to 0
  number = 0
  
  # Multiply the decoded number by the base and add the value of the encoded digit for each character in the encoded number
  for i, c in enumerate(encoded_number):
    number += base_chars.index(c) * (1024 ** (len(encoded_number) - i - 1))
  
  return number