import matplotlib.pyplot as plt
import numpy as np

x_cord = [0, 2, 4]
y1_cord = [1, 3, 5]
y2_cord = [5, 7, 9]
y3_cord = [9, 11, 13]

plt.plot(x_cord, y1_cord, linewidth = 1)
plt.plot(x_cord, y2_cord, linewidth = 2)
plt.plot(x_cord, y3_cord, linewidth = 3)

plt.show()