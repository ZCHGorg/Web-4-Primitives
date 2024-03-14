import numpy as np

def fourier_transform(data):
    N = len(data)
    fourier = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            fourier[k] += data[n] * np.exp(-2j*np.pi*k*n/N)
    return fourier

import numpy as np

def fourier_transform_12phase(data, phi):
    N = len(data)
    fourier = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            fourier[k] += data[n] * np.exp(-2j*np.pi*k*n/N + 1j*phi)
    return fourier
