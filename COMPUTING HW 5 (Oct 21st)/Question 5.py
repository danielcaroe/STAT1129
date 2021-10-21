import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

#plot 1:
plt.subplot(1, 4, 1)
plt.scatter([1,2,3,4,5],[5,4,3,2,1])
plt.title("scatter plot")


#plot 2:
plt.subplot(1, 4, 2)
plt.plot([1,2,5,4,9],[5,4,3,2,1])
plt.plot([1,5,7,8,3],[5,4,3,2,1])
plt.title("Multiple line plot")

#plot 3:
plt.subplot(1, 4, 3)
plt.bar(['A','B','C','D'], [2,4,6,8])
plt.title("Bar chart")


#plot 4:
plt.subplot(1, 4, 4)
plt.pie([50,25,10,15,40,10], labels =['A','B','C','D','E','F'])
plt.title("Pi chart")


plt.show()