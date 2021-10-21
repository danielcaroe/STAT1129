import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) # this is x-axis values
y1 = np.array([88, 92, 80, 89, 90, 80, 60, 88, 80, 84]) # this is the math marks
plt.scatter(x1, y1, color = 'red', label = "Math Marks")

x2 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
y2 = science_marks = np.array([75, 59, 69, 48, 65, 56, 32, 45, 20, 30]) # this is the science marks
plt.scatter(x2, y2, color = 'green', label = "Science Marks")

plt.title("Scatter Plot")
plt.xlabel("Marks Scored")
plt.ylabel("Marks Range")
plt.legend(loc = 'lower left')
            
plt.show()