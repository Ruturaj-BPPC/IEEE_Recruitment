import numpy as np 
import matplotlib.pyplot as plt
numbers=np.random.normal(loc=0, scale=1, size=1000)

plt.scatter(range(len(numbers)), numbers,alpha=0.6)
plt.title("Scatter Plot of Normally Distributed Random Numbers")
plt.xlabel("Index")     
plt.ylabel("Value")
plt.show()
