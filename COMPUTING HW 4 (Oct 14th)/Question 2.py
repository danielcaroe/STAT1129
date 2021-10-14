#Part 1
import pandas
import numpy as np

x = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]])

for row in x:
    for column in row:
        print(column, end=' ')
    print()
#Part 2    
for i in x.flat:
    print(i, end=' ')
    