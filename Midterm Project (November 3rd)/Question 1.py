import matplotlib.pyplot as plt
import json

list1=[2,4,6,8,4,5,2,1,9,0,4,6,7,4,3,2,1,9,10,3,7,9,6,0,1,3,5,6,7,8,9,10,2,3,6,8,9,10,6,7,4,3]
dict1={}

for i in list1:
    if i not in dict1:  
        dict1[i]=1
    else:
        dict1[i]+=1     
        

list2=sorted(dict1.items())
for i in list2:
    print(i[0],":",i[1])
      
plt.bar(list(dict1.keys()), dict1.values(), color='b')
plt.show()

with open('frequency.json', 'w') as f:
    json.dump(dict1,f)
