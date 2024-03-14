import cmath

# Define the alphabet and base size
alphabet = string.ascii_letters + string.digits + string.punctuation
base = 1048576

# Define the encoding function using complex numbers
def encode_baseX_complex(input_string):
    encoded = ""
    number = 0
    for char in input_string:
        number += cmath.exp(alphabet.index(char)*(2j*cmath.pi/len(alphabet)))
    while number > 0:
        encoded = alphabet[int(number.real*len(alphabet)/(2*cmath.pi)) % base] + encoded
        number /= base
    return encoded

# Define the decoding function using complex numbers
def decode_baseX_complex(input_string):
    decoded = ""
    number = 0
    for char in input_string:
        number += cmath.exp(alphabet.index(char)*(2j*cmath.pi/base))
    for _ in range(0, float('inf')):
        baseX = len(alphabet) ** _
        if number > 0:
            decoded = chr(int(number.real*len(alphabet)/(2*cmath.pi)) % baseX) + decoded
            number /= baseX
    return
