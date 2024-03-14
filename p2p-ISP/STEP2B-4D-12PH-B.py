import numpy as np

# Define the signal as a 4D complex array
signal = np.zeros((4,), dtype=complex)

# Define the 12-phase wave
phase = np.linspace(0, 2*np.pi, 12, endpoint=False)

# Add the 12-phase wave to the signal
for i in range(4):
    signal[i] = np.exp(1j*phase[i])
    
# Perform the Fourier transform on the 4D signal
fourier_transform = np.fft.fftn(signal)

# Print the result
print(fourier_transform)
