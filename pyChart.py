# plot a pie chart in Matplotlib

"""
Pychart: A pie chart display data in a pictorial nform , divided into slices.\
    to plot a pie chart in matplotlib, use the pie() method:

--parameter :
1.x= the wedge size are set
2.labels for each wedges
3.label with numeric vcalues
"""

import matplotlib.pyplot as plt
import  pandas as pd
import  numpy as np

# data of cricket
player = np.array(["Santosh","Krishna","Manjit","Monu","Shishir"])
run = np.array([98,89,88,79,95])

# plot a pie chart : pie()
plt.pie(run,labels=player,autopct='%1.2f%%')

# title
plt.title("Scorecard of the Series[449Runs]",fontsize='x-large')





# Display:
plt.show()