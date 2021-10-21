import matplotlib.pyplot as plt
import numpy as np

mydic = {"Apples": 45, "Bananas":25, "Cherries":15, "Dates":20}

fruit_list = []

fruit_list.append("Apples")
fruit_list.append("Bananas")
fruit_list.append("Cherries")
fruit_list.append("Dates")

count_list = []

count_list.append(45)
count_list.append(25)
count_list.append(15)
count_list.append(20)

y = np.array([45, 25, 15, 20])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [.1, .1, .1, .1]

plt.subplot(1, 5, 1)
plt.pie(y, labels=mylabels, explode=myexplode)

plt.subplot(1, 5, 5)
plt.bar(mylabels, y)
print(fruit_list)
print(count_list)
plt.show()
