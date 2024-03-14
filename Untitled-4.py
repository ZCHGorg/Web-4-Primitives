alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()-_+=[{]};:',\"<>?/\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1A\x1B\x1C\x1D\x1E\x1F\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2A\x2B\x2C\x2D\x2E\x2F\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3A\x3B\x3C\x3D\x3E\x3F\x40\x41"

def encode(number):
    encoded = ''
    while number > 0:
        encoded = alphabet[number % 4112] + encoded
        number //= 4112
    return encoded

def decode(encoded):
    decoded = 0
    for i, c in enumerate(reversed(encoded)):
        decoded += alphabet.index(c) * 4112**i
    return decoded

def encode_128(number):
    encoded = ''
    while number > 0:
        encoded = alphabet128[number % 128] + encoded
        number //= 128
    return encoded

def decode_128(encoded):
    decoded = 0
    for i, c in enumerate(reversed(encoded)):
        decoded += alphabet128.index(c) * 128**i
    return decoded

# Define new alphabet for base128
alphabet128 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()-_+=[{]};:',\"<>?/\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1A\x1B\x1C\x1D\x1E\x1F\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2A\x2B\x2C\x2D\x2E\x2F\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3A\x3B\x3C\x3D\x3E\x3F\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4A\x4B\x4C\x4D\x4E\x4F\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5A\x5B\x5C\x5D\x5E\x5F\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6A\x6B\x6C\x6D\x6E\x6F\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7A\x7B\x7C\x7D\x7E\x7F"

# Create new functions to encode/decode base128 numbers
def encode_128(number):
    encoded = ''
    while number > 0:
        encoded = alphabet128[number % 128] + encoded
        number //= 128
    return encoded

def decode_128(encoded):
    decoded = 0
    for i, c in enumerate(reversed(encoded)):
        decoded += alphabet128.index(c) * 128**i
    return decoded

# Create new functions to convert between base128 and base4112
def convert_128_to_4112(number):
    # Encode the base128 number
    encoded_128 = encode_128(number)
    
    # Decode the encoded base128 number into base4112
    decoded_4112 = decode(encoded_128)
    
    return decoded_4112

def convert_4112_to_128(number):
    # Encode the base4112 number
    encoded_4112 = encode(number)
    
    # Decode the encoded base4112 number into base128
    decoded_128 = decode_128(encoded_4112)
    
    return decoded_128