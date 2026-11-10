import matplotlib.pyplot as plt
import numpy as np


xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)

plt.title("Grafico")
plt.xlabel("Plano X")
plt.ylabel("Plano Y")

plt.show()