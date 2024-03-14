#What does this code do?
#This code implements a compression algorithm known as "1MM" (one millionth) encoding. It takes a number as input and encodes it into a compressed form using Huffman and LZW algorithms, then encodes it using a custom base1MM encoding. It also has a corresponding decode function which takes in a 1MM encoded string and decodes it back into its original number.

import collections
import base64
 
def encode_1MM(number):
    # Step 1 - convert our number into a data stream
    data_stream = []
    while number > 0:
        data_stream.append(number % 1052672)
        number //= 1052672
 
    # Step 2 - create a dictionary of symbols for each value
    symbol_dict = {}
    for i, value in enumerate(data_stream):
        symbol_dict[value] = chr(i + 65)
 
    # Step 3 - create a symbol stream
    symbol_stream = []
    for value in data_stream:
        symbol_stream.append(symbol_dict[value])
 
    # Step 4 - apply Huffman and LVW algorithms to the symbol stream
    huffman_codes = collections.defaultdict(int)
    lzw_codes = collections.defaultdict(int)
    curr_code = 0
    prev_symbol = symbol_stream[0]
    huffman_codes[prev_symbol] = 0
    for symbol in symbol_stream[1:]:
        if symbol not in huffman_codes:
            curr_code += 1
            huffman_codes[symbol] = curr_code
        if prev_symbol + symbol in lzw_codes:
            lzw_codes[prev_symbol + symbol] += 1
        else:
            lzw_codes[prev_symbol + symbol] = 1
        prev_symbol = symbol
 
    # Step 5 - compress the symbol stream
    compressed_stream = []
    for symbol in symbol_stream:
        encoded_symbol = huffman_codes[symbol]
        if encoded_symbol in lzw_codes and lzw_codes[encoded_symbol] > 1:
            compressed_stream.append(encoded_symbol)
        else:
            compressed_stream.append(symbol)
 
    # Step 6 - apply our base1MM encoding
    encoded = ''
    for symbol in compressed_stream:
        encoded = base64.b64encode(symbol).decode().replace('+', '~').replace('/', '\\').replace('=', '|') + encoded
    return encoded
 
def decode_1MM(encoded):
    # Step 1 - decode our base1MM encoded string
    decoded_stream = []
    for c in reversed(encoded):
        decoded_stream.append(base64.b64decode(c.replace('~', '+').replace('\\', '/').replace('|', '=').encode()))
 
    # Step 2 - create a dictionary of symbols for each value
    symbol_dict = {}
    for i, value in enumerate(decoded_stream):
        symbol_dict[value] = chr(i + 65)
 
    # Step 3 - create a symbol stream
    symbol_stream = []
    for value in decoded_stream:
        symbol_stream.append(symbol_dict[value])
 
    # Step 4 - apply Huffman and LVW algorithms to the symbol stream
    huffman_codes = collections.defaultdict(int)
    lzw_codes = collections.defaultdict(int)
    curr_code = 0
    prev_symbol = symbol_stream[0]
    huffman_codes[prev_symbol] = 0
    for symbol in symbol_stream[1:]:
        if symbol not in huffman_codes:
            curr_code += 1
            huffman_codes[symbol] = curr_code
        if prev_symbol + symbol in lzw_codes:
            lzw_codes[prev_symbol + symbol] += 1
        else:
            lzw_codes[prev_symbol + symbol] = 1
        prev_symbol = symbol
 
    # Step 5 - decompress the symbol stream
    decompressed_stream = []
    prev_symbol = symbol_stream[0]
    for symbol in symbol_stream[1:]:
        encoded_symbol = huffman_codes[symbol]
        if encoded_symbol in lzw_codes and lzw_codes[encoded_symbol] > 1:
            decompressed_stream.append(encoded_symbol)
        else:
            decompressed_stream.append(symbol)
 
    # Step 6 - decode the decompressed stream
    decoded = 0
    for i, c in enumerate(reversed(decompressed_stream)):
        decoded += base64.b64decode(c.encode()) * 1052672**i
    return decoded