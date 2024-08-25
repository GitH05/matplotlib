# """legend in a graph is a box on the left and right displaying the data from the column legend generally helps the reader i understanding the graph
# -legend() is used to trwepresent the legend
# """


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# # set data:
# data = {
#     "bat":["ton","gm","mrf"],
#     "price":[1232,5343,2344],
#     "weight":[350,870,730]
# }
# # convert data into dataframe:
# dataframe=pd.DataFrame(data)
# plt.plot(dataframe["bat"],dataframe["price"])
# # plt.show()

# # # adding grid:
# # plt.grid()

# # plt.show()


# # add label
# plt.xlabel("Bat")
# # plt.xlabel("Bat price")
# plt.ylabel("Price")

# # show
# plt.show()



# data 
a =np.arange(5)
b=[1,2,3,4,5]
c=[6,7,8,9,10]

# create plot
fig=plt.figure()
axis=plt.subplot()

# k= marker
axis.plot(a,b,'k--',label='frequency')
axis.plot(a,c,'k:',label='Periods')

# create legend and set position/location
# and font-size:legend(fontsize = ' xx-small/x-small/small')
legen = axis.legend(loc = 'lower right', fontsize = 'small')

# set background-color; using buil;t-in function:Set_facecolor()
legen.get_frame().set_facecolor('orange')


# title
plt.title("Frequency and Periods",fontsize='xx-large')
# display
plt.show()