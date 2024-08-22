'''pyplot is a sub module of matplotlib'''
import matplotlib.pyplot as plt
import numpy as np
# x point and y point : cordinate
x= np.array([9,2])
y= np.array([1,5])

# plot x and y using the pyplot module:
plt.plot(x,y)

# display figure:
plt.show()
