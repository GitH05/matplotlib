# x=np.array([11,12])
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# y=np.array([1,4])
# plt.plot(x,y)
# #(x1,y1)=(11,1)  and (x2,y2)=(12,4)
# plt.show()

# adding grid lines
'''
-using grid()
'''

# set data:
data = {
    "bat":["ton","gm","mrf"],
    "price":[1232,5343,2344],
    "weight":[350,870,730]
}
# convert data into dataframe:
dataframe=pd.DataFrame(data)
plt.plot(dataframe["bat"],dataframe["price"],dataframe["weight"])
# plt.show()

# adding grid:
plt.grid()

plt.show()
