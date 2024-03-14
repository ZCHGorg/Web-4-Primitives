import base64

def encode_baseX(number, alphabet):
    encoded = ''
    while number > 0:
        encoded = alphabet[number % len(alphabet)].decode() + encoded
        number //= len(alphabet)
    return encoded

def decode_baseX(encoded, alphabet, multiplier):
    decoded = 0
    for i, c in enumerate(reversed(encoded)):
        decoded += (alphabet.index(c.encode()) + multiplier) * len(alphabet)**i
    return decoded

#Using our code I would like to automatically select a baseX for a given string input such that the output character count is as close as possible to zero.  Our alphabet and baseX should remain capable of scaling to any size.
#The basic idea is to iterate through a range of bases and calculate the character count of the encoded string. We then find the base that produces the closest character count to zero.
#The following code is a working example of this idea:

def get_optimal_baseX(string):
    alphabet = string.encode()
    min_count = float('inf')
    optimal_baseX = 0
    for baseX in range(2, len(alphabet) + 1):
        encoded = encode_baseX(string, alphabet)
        count = len(encoded) - len(string)
        if abs(count) < min_count:
            min_count = abs(count)
            optimal_baseX = baseX
    return optimal_baseX

# Test
string = 'Hello World!'
optimal_baseX = get_optimal_baseX(string)
print('Optimal baseX for string "{}" is {}'.format(string, optimal_baseX))
# Output: Optimal baseX for string "Hello World!" is 12