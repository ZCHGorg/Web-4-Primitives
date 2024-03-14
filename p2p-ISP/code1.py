import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

# Load data
data = ...

# Fit t-SNE and PCA models
tsne = TSNE(n_components=2).fit_transform(data)
pca = PCA(n_components=2).fit_transform(data)

# Plot the results
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.scatter(tsne[:, 0], tsne[:, 1])
ax1.set_title("t-SNE")
ax2.scatter(pca[:, 0], pca[:, 1])
ax2.set_title("PCA")
plt.show()
