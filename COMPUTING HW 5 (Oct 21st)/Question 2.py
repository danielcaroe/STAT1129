import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 0, .2
s = np.random.normal(mu, sigma, 800)
plt.hist(s)
plt.show()