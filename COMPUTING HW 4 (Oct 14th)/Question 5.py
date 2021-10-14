import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 1, 2, 3, 4, 5])
ypoints = np.array([2, 4, 6, 14, 10, 12])

plt.plot(ypoints, marker = 's', linestyle = 'dashed', color = 'red', markerfacecolor = 'green', markersize = 10)
plt.show()