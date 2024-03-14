from reedsolo import RSCodec

# Define the number of data bytes and parity bytes
n = 10
k = 5

# Initialize the codec
rs = RSCodec(n, k)

# Encode the data
data = [1, 2, 3, 4, 5]
encoded_data = rs.encode(data)

# Transmit the encoded data
# (in a real-world scenario, this would be over a noisy channel)

# Decode the data
decoded_data = rs.decode(encoded_data)

# Print the original data and the decoded data
print("Original data:", data)
print("Decoded data:", decoded_data)
