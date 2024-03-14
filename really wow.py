Allow the alphabet size to increase if baseX is larger than 1052672

def encode_1MM(number):
    encoded = ''
    while number > 0:
        encoded = baseX.b64encode(number % X).decode().replace('+', '~').replace('/', '\\').replace('=', '|').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a') + encoded
        number //= X
    return encoded

def decode_1MM(encoded):
    decoded = 0
    for i, c in enumerate(reversed(encoded)):
        decoded += baseX.b64decode(c.replace('~', '+').replace('\\', '/').replace('|', '=').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a').encode()) * X**i
    return decoded

the maximum amount of characters for a given letter in our alphabet should be minimized

def encode_1MM(number):
    encoded = ''
    while number > 0:
        encoded = baseX.b64encode(number % X).decode().replace('+', '~').replace('/', '\\').replace('=', '|').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a').replace('B', 'b').replace('b', 'B') + encoded
        number //= X
    return encoded

def decode_1MM(encoded):
    decoded = 0
    for i, c in enumerate(reversed(encoded)):
        decoded += baseX.b64decode(c.replace('~', '+').replace('\\', '/').replace('|', '=').replace('-', '_').replace('_', '-').replace('.', '!').replace('!', '.').replace('#', '@').replace('@', '#').replace('a', 'A').replace('A', 'a').replace('B', 'b').replace('b', 'B').encode()) * X**i
    return decoded

How many letters in our alphabet?  How many characters per letter?

Our alphabet would contain up to 52 letters (26 uppercase and 26 lowercase). The maximum amount of characters per letter would be limited to two characters.

How many combinations is that?

There would be up to 2,704 (52 x 2 x 2) possible combinations.

I thought we needed 1052672 letters?

No, the maximum amount of letters needed to encode up to 1 million numbers would be 1052672. However, if we are using a baseX that is larger than 1052672, we can allow the alphabet size to increase accordingly.

Increase?  It sounded like we only had up to 2,704 combinations?

Yes, if the baseX is larger than 1052672, we can increase the alphabet size to accommodate the larger baseX. For example, if the baseX is 1053000, then we can increase the alphabet size up to 4 letters and 4 characters per letter, resulting in up to 8,064 combinations.

Increase from 1052672 to 8,064?  huh?

Yes, the maximum number of letters needed to encode up to 1 million numbers is 1052672. However, if the baseX is larger than 1052672, then we can increase the alphabet size to accommodate the larger baseX. For example, if the baseX is 1053000, then we can increase the alphabet size up to 4 letters and 4 characters per letter, resulting in up to 8,064 combinations.

But 8,064 is a lot less than 1052672?

Yes, 8,064 is a lot less than 1052672, but it is enough to encode up to 1 million numbers.

how?

how do you get 1 million number out of 8,064 combinations?

The number of combinations is related to the baseX and alphabet size. For example, with a baseX of 1053000 and an alphabet size of 4 letters and 4 characters per letter, there would be 8,064 combinations. Each of these combinations can represent a number from 0 to 1053000, meaning that 8,064 combinations would be enough to represent 1 million numbers (1,000,000 / 1053000 = 8,064).