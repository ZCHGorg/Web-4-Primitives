import math

# Transmitter parameters
Pt = 20 # transmit power in dBm
Gt = 5 # transmit antenna gain in dBi

# Receiver parameters
Gr = 5 # receive antenna gain in dBi
L = 2 # system loss factor

# Propagation parameters
f = 2.4e9 # frequency in Hz
c = 3e8 # speed of light in m/s
lambda_ = c/f # wavelength in meters

# Distance between transmitter and receiver
d = 100 # distance in meters

# Calculate the received power in dBm
Pr = Pt + Gt + Gr - 20*math.log10(lambda_/(4*math.pi*d)) - L

print("Received power:", Pr, "dBm")
