import numpy as np
from sklearn.manifold import TSNE

# Load data
data = ...

# Fit t-SNE model
tsne = TSNE(n_components=4).fit_transform(data)

# Compress the data using interweaving helixes
def interweave_helixes(data):
    compressed_data = []
    for i in range(0, len(data), 4):
        compressed_data.append(data[i])
        compressed_data.append(data[i+2])
        compressed_data.append(data[i+1])
        compressed_data.append(data[i+3])
    return np.array(compressed_data)

compressed_data = interweave_helixes(tsne)
