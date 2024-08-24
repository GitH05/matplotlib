# labels:
'''
x cordinate: xlabel()
y cordinate: ylabel()

'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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

# # adding grid:
# plt.grid()

# plt.show()


# add label
plt.xlabel("bat")
# plt.xlabel("Bat price")
plt.ylabel("Weight")

# show
plt.show()
