# import matplotlib.pyplot as plt

# def plot_2d_data(X, y, title = "Linear Data"):
#     plt.scatter(X[:,0], X[:,1],c=y)
#     plt

import matplotlib.pyplot as plt

def plot_2d_data(X, y, title="2D Data"):
    plt.figure(figsize=(6, 6))
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap="bwr", edgecolors="k")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.title(title)
    plt.grid(True)
    plt.show()
